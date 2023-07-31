import requests
import math
from bs4 import BeautifulSoup, Comment
import pandas as pd
from datetime import datetime

def scrape_nba_season_data(year):
    months = ['october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june']
    all_data = []

    for month in months:
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games-{month}.html"
        response = requests.get(url)

        # Check if the page contains data
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the table containing game data
            table = soup.find('table', {'id': 'schedule'})

            # Extract table headers if this is the first month
            if not all_data:
                headers = [th.text for th in table.find_all('th', {'scope': 'col'})]

            # Extract table rows
            rows = table.find_all('tr')[1:]

            # Extract data from table cells
            data = []
            for row in rows:
                cells = row.find_all(['td', 'th'])
                row_data = [cell.text for cell in cells]


                data.append(row_data)

            all_data.extend(data)

    # Create a pandas DataFrame
    df = pd.DataFrame(all_data, columns=headers)

    # Keep only the desired columns
    desired_indices = [0, 2, 3, 4, 5]
    df = df.iloc[:, desired_indices]
    df.columns = ['Date', 'Away_Team', 'Away_PTS', 'Home_Team', 'Home_PTS']

    return df


years = [2023]
game_data = pd.concat([scrape_nba_season_data(year) for year in years], ignore_index=True)

game_data.to_csv('nba_game_data.csv', index=False)

#Next, gather some team stats

url = "https://www.basketball-reference.com/leagues/NBA_2023.html"
response = requests.get(url)

# Read tables from the HTML page using Pandas
tables = pd.read_html(response.text, header=None)

# Find the advanced stats table by checking the column names at multiple levels
for table in tables:
    if ("Unnamed: 1_level_0", "Team") in table.columns and ("Offense Four Factors", "ORB%") in table.columns:
        adv_stats_df = table
        break

# Clean up the multi-level column headers
adv_stats_df.columns = adv_stats_df.columns.droplevel(0)


# Save the DataFrame as a CSV file
adv_stats_df.to_csv("advanced_stats.csv", index=False)

#Per Game Stats
for table in tables:
    if "PTS" in table.columns and "G" in table.columns and "MP" in table.columns:
        if all(table["MP"] < 250):
            per_game_stats_df = table
            break

# Add headers for the per game stats table
headers = ["Rk", "Team", "G", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
per_game_stats_df.columns = headers

# Save the DataFrames as CSV files
per_game_stats_df.to_csv("per_game_stats.csv", index=False)

# Sort each CSV file to only contain relevant variables
# Keep the specified columns in the advanced stats DataFrame
adv_stats_df = adv_stats_df[["Team", "W", "L", "SOS", "SRS", "ORtg", "DRtg", "NRtg", "Pace"]]

# Keep the specified columns in the per game stats DataFrame
per_game_stats_df = per_game_stats_df[["Team", "G", "PTS"]]

# Merge the DataFrames on the "Team" column
combined_df = adv_stats_df.merge(per_game_stats_df, on="Team")

# Save the combined DataFrame as a CSV file
combined_df.to_csv("combined_stats.csv", index=False)



def predict_winning_team(date):
    nba_game_data = pd.read_csv("nba_game_data.csv")
    combined_stats = pd.read_csv("combined_stats.csv")

    # Convert the date string to the appropriate format
    current_year = datetime.now().year
    date = datetime.strptime(f"{current_year} {date}", "%Y %b %d").strftime("%a, %b %-d, %Y")

    # Filter the game data for the given date
    todays_games = nba_game_data[nba_game_data["Date"] == date]
    # print("Games today:\n", todays_games)

    # Create an empty DataFrame to store the game predictions
    game_predictions = pd.DataFrame(columns=["Away Team", "Home Team", "Predicted Winner", "Predicted Score"])

    for index, row in todays_games.iterrows():
        away_team = row["Away_Team"]
        home_team = row["Home_Team"]

        # Get the team stats from the combined_stats DataFrame
        away_team_stats = combined_stats[combined_stats["Team"] == away_team].iloc[0]

        home_team_stats = combined_stats[combined_stats["Team"] == home_team].iloc[0]
        # print("Away team data:\n", away_team_stats)

        # Calculate score predictions for each team
        # Home Court Advantage Multiplier:
        HCA = 1.03

        away_team_predicted_score = (1 + (float(away_team_stats["SOS"])/100))*( ( ( math.log( ( away_team_stats["W"] / ( away_team_stats["L"] + away_team_stats["W"] ) ) / (.5) ) ) * (.1) ) + 1 ) * (float(away_team_stats["PTS"]) * (float(home_team_stats["DRtg"]) / float(away_team_stats["ORtg"])))
        home_team_predicted_score = HCA * ((1 + (float(home_team_stats["SOS"])/100))*( ( ( math.log( ( home_team_stats["W"] / ( home_team_stats["L"] + home_team_stats["W"] ) ) / (.5) ) ) * (.1) ) + 1 ) * (float(home_team_stats["PTS"]) * (float(away_team_stats["DRtg"]) / float(home_team_stats["ORtg"]))))

        # Compare the predicted scores and determine the winning team
        if away_team_predicted_score > home_team_predicted_score:
            predicted_winner = away_team
        elif home_team_predicted_score > away_team_predicted_score:
            predicted_winner = home_team
        else:
            predicted_winner = "Tie"

        predicted_score = f"{away_team_predicted_score:.2f} - {home_team_predicted_score:.2f}"
        # print("Predicted score difference:", predicted_score)

        # Edit the game and its prediction to the game_predictions DataFrame
        new_row = pd.DataFrame({
            "Away Team": [away_team],
            "Home Team": [home_team],
            "Predicted Winner": [predicted_winner],
            "Predicted Score": [predicted_score]
        })

        game_predictions = pd.concat([game_predictions, new_row], ignore_index=True)

    predicted_scores = game_predictions['Predicted Score'].str.split(' - ', expand=True)
    away_predicted_scores = predicted_scores[0].astype(float)
    home_predicted_scores = predicted_scores[1].astype(float)

    # Calculate the total predicted score
    total_predicted_score = away_predicted_scores + home_predicted_scores

    # Add the total predicted score column to the DataFrame
    game_predictions['Total Predicted Score'] = total_predicted_score

    # Display the game_predictions DataFrame
    print(game_predictions)

# Call the function with a date
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
predict_winning_team("Apr 9")

