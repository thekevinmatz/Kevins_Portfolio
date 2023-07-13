# Kevin Matz - Analyst Portfolio

Welcome to my data analyst portfolio! Here you can find a selection of my projects and experiences in a variety of analyses, completed through my education, for my freelance Data Analyst work, and through other various side projects. Feel free to reach out if you have any questions about my work!

# About Me

- 🔭 I just completed Master of Science in Economics
- 🌱 I'm currently furthering my skills in SQL
- 📫 How to reach me: [LinkedIn](https://www.linkedin.com/in/kevin-matz/) | [Email](mailto:kevinmatz@tamu.edu)
- 💡 Fun fact: I'm an avid musician and guitar player!

# Projects

To help you navigate through my portfolio, I have organized my projects by the software used. Please feel free to click on the links below to jump directly to the section that interests you the most!

- [Most Recent Project](#most-recent-project)
- [R Projects](#r-projects)
- [Excel and Google Sheets Projects](#excel-and-google-sheets-projects)
- [Statistical Analysis Presentations](#statistical-analysis-presentations)
- [Python Projects](#python-projects)


## Most Recent Project

### Dynamic Financial Dashboard - Excel

As a freelance data analyst and Excel specialist, I recently had the opportunity to create a comprehensive trading dashboard for a client. The project, designed to track and analyze trading data, demonstrates my ability to utilize complex Excel formulas and tools to deliver effective business solutions.

I built this dashboard in Microsoft Excel, employing advanced functions such as INDEX, OFFSET, COUNTA, VLOOKUP, SUMIF, and dynamic array formulas. The interface provides a user-friendly layout, making it easy for the client to input and monitor their trade data, while the back-end seamlessly handles complex calculations and data management tasks. 

**Screenshot:**

![JPG](https://github.com/thekevinmatz/Kevins_Portfolio/blob/8e82ddb2fc59c6eee0c35c68d6f44827975811c8/Financial%20Dashboard%20Example%20Screenshot.png "JPG")

Key features of the dashboard include:

**Data recording and analysis:** The 'Trade Data Recording' tab allows users to input each trade's details, while the 'Trade Analysis' tab generates a dynamic display of the most recent 20 trades (or 'batches') based on the recorded data.

**Real-time P&L tracking:** The dashboard provides a line chart that automatically updates to display the P&L of each trade. A running total of P&L is also calculated and charted to provide a clear overview of the trading performance over time.

**Trading statistics:** The dashboard includes a variety of key trading statistics, including total number of trades, win rate, average win/loss, and expectancy, which are all updated in real-time.

**Conditional formatting:** Visual cues were provided through the use of conditional formatting in order to enhance data clarity and user interaction.

**Error handling:** I implemented error-handling functions to ensure that any blank cells or other potential data issues wouldn't disrupt the dashboard's performance.

The provided screenshot is an example of the dashboard in use, with the numbers shown being purely illustrative. To protect my client's privacy, the data used are generated and not based on actual trading performance. Furthermore, the dashboard's design and features have been altered in certain ways to further secure confidential information.

With this project, I have showcased my abilities in data analysis, problem-solving, and Excel mastery, all crucial skills for a data analyst role. I strive to combine these skills with my strong understanding of business operations to deliver solutions that enhance decision-making and improve performance.

*Please note: For privacy and security reasons, the actual dashboard has not been shared. The screenshot provided is a altered copy and does not contain real data or sensitive information.*

## R Projects

### Statistical Simulations and Visualizations in R

In this project, I performed a series of statistical simulations using R to explore the behavior of t-statistics and R-squared values under different conditions. This work leveraged my understanding of statistical theory, particularly around the behavior of these metrics in the context of random walks and autoregressive processes.

**Objective**

The primary objective of this project was to gain insights into how certain statistical metrics behaved under various conditions. To achieve this, I used simulation techniques to generate data under specific conditions and then ran statistical analyses on this simulated data.

**Methods**

The project used several statistical simulation techniques. Firstly, I generated random walks and ran linear regressions on them. From these regressions, I extracted the t-statistics and R-squared values and analyzed their behavior. 

For instance, I utilized the following R code to generate a random walk and then run a linear regression on it:

```R
set.seed(123)
e <- rnorm(100)
Y <- numeric(100)
Y[1] <- e[1]
for (t in 2:100) {
  Y[t] <- Y[t - 1] + e[t]
}
fit <- lm(Y ~ 1 + X)
b1 <- coef(fit)[2]
R2 <- summary(fit)$r.squared
t_stat <- b1 / summary(fit)$coef[2, 2]
```

After exploring the behavior of t-statistics and R-squared values in this basic setup, I conducted further simulations to assess their behavior under different sample sizes:

```R
T_vec <- c(50, 100, 200)
fraction_reject_null_vec <- numeric(length(T_vec))

for (i in seq_along(T_vec)) {
  T <- T_vec[i]
  reps <- 1000
  t_stat_vec <- numeric(reps)
  for (j in 1:reps) {
    e <- rnorm(T)
    Y <- numeric(T)
    Y[1] <- e[1]
    for (t in 2:T) {
      Y[t] <- Y[t - 1] + e[t]
    }
    fit <- lm(Y ~ 1 + X)
    t_stat_vec[j] <- coef(summary(fit))[2, 3]
  }
  fraction_reject_null_vec[i] <- mean(abs(t_stat_vec) > 1.96)
}
```

**Results**

The results from these simulations provided insightful observations about the behavior of the t-statistics and R-squared values under different conditions. For example, the fraction of times that the null hypothesis is rejected was observed to approach 5% as the sample size increases, demonstrating the convergence of the t-test under these conditions. This project served as a practical exploration of statistical theory, and its results offered a valuable perspective on the behavior of key statistical metrics.

The full R Markdown file for this project, containing all code and additional commentary, can be viewed [here](https://github.com/thekevinmatz/Kevins_Portfolio/blob/fa68eb46ffe69df29cb7ee4f526f2ae333488356/Statistical%20Simulations%20and%20Visualizations%20in%20R.Rmd)

---

### Statistical Analysis of Real GDP Growth and Interest Rate Spread

This project was completed as part of my coursework and focuses on the statistical analysis of Real GDP growth and the Interest Rate Spread.

**Project Description**

The primary aim of this project was to analyze the relationship between Real GDP growth and the Interest Rate Spread. The data used in this project were retrieved from the Federal Reserve Economic Data (FRED) using the Quandl API.

**Key Tasks**

1. **Data Retrieval:** I retrieved and processed weekly data on the Interest Rate Spread from 1986 to 2022. I also fetched quarterly Real GDP data and computed the annualized growth rate.

2. **Statistical Analysis:** Using R, I conducted autoregressive analyses on the Real GDP data with up to eight lags to ascertain the potential influence of past GDP growth rates on the current GDP growth rate.

3. **Model Evaluation:** I evaluated the models based on their summary statistics and the Akaike Information Criterion (AIC). I noted potential endogeneity and the influence of uncorrelated factors that could affect the yield spread's predictability.

4. **In-sample Fit:** I compared the fitted values from the best model against the actual realizations of the Real GDP growth, plotting them over time.

5. **Forecasting:** I discussed the forecasting ability of the best model if it had been estimated about ten years ago. I also compared it against a forecast based on the sample mean and found a statistically significant difference between the two predictive methods.

**Key Findings**

The models, while not perfect, provided valuable insights into the relationships between the variables and allowed for reasonable forecasting. The best model leveraged the lag effect to accurately predict the next quarter, proving superior to a forecast based on the sample mean. However, the need for continuous improvement of forecasting methods to better account for the evolving nature of economic factors and the statistical nature of the data was highlighted.

**Tools and Libraries Used**

This project was completed using R with the following libraries:

- `fredr` for retrieving data from FRED
- `forecast` for conducting autoregressive analyses
- `ggplot2` for data visualization
- `xts` for handling time-series data
- `Quandl` for data retrieval from Quandl

The full code, along with more detailed findings from this project, can be found [here](https://github.com/thekevinmatz/Kevins_Portfolio/blob/2961d52474c4f8bad46ded2b19372dd7a917c1c0/Statistical%20Analysis%20of%20Real%20GDP%20Growth%20and%20Interest%20Rate%20Spread.Rmd).

## Excel and Google Sheets Projects

### Dynamic Financial Dashboard - Excel | *COPY OF MOST RECENT PROJECT*

As a freelance data analyst and Excel specialist, I recently had the opportunity to create a comprehensive trading dashboard for a client. The project, designed to track and analyze trading data, demonstrates my ability to utilize complex Excel formulas and tools to deliver effective business solutions.

I built this dashboard in Microsoft Excel, employing advanced functions such as INDEX, OFFSET, COUNTA, VLOOKUP, SUMIF, and dynamic array formulas. The interface provides a user-friendly layout, making it easy for the client to input and monitor their trade data, while the back-end seamlessly handles complex calculations and data management tasks. 

**Screenshot:**

![JPG](https://github.com/thekevinmatz/Kevins_Portfolio/blob/8e82ddb2fc59c6eee0c35c68d6f44827975811c8/Financial%20Dashboard%20Example%20Screenshot.png "JPG")

Key features of the dashboard include:

**Data recording and analysis:** The 'Trade Data Recording' tab allows users to input each trade's details, while the 'Trade Analysis' tab generates a dynamic display of the most recent 20 trades (or 'batches') based on the recorded data.

**Real-time P&L tracking:** The dashboard provides a line chart that automatically updates to display the P&L of each trade. A running total of P&L is also calculated and charted to provide a clear overview of the trading performance over time.

**Trading statistics:** The dashboard includes a variety of key trading statistics, including total number of trades, win rate, average win/loss, and expectancy, which are all updated in real-time.

**Conditional formatting:** Visual cues were provided through the use of conditional formatting in order to enhance data clarity and user interaction.

**Error handling:** I implemented error-handling functions to ensure that any blank cells or other potential data issues wouldn't disrupt the dashboard's performance.

The provided screenshot is an example of the dashboard in use, with the numbers shown being purely illustrative. To protect my client's privacy, the data used are generated and not based on actual trading performance. Furthermore, the dashboard's design and features have been altered in certain ways to further secure confidential information.

With this project, I have showcased my abilities in data analysis, problem-solving, and Excel mastery, all crucial skills for a data analyst role. I strive to combine these skills with my strong understanding of business operations to deliver solutions that enhance decision-making and improve performance.

*Please note: For privacy and security reasons, the actual dashboard has not been shared. The screenshot provided is a altered copy and does not contain real data or sensitive information.*

## Statistical Analysis Presentations

### Statistical Analysis to Determine the Effects of Covid-19 on Student Scores
A project from my Masters program where I used **SAS and Excel** to lead analysis and visualization. While the title states "...the Effects of Covid-19...", it does not necessarily mean the effects of the actual disease itself, but also the implications and results of Covid-19 policies, social trends, and overall public reaction, which may have negatively affected students.
- Goal: Find a measurable change (if any) in standardized test passing rates for Texas students before and after COVID-19.
- Hypothesis: There will indeed be a measurable and statistically significant **decrease in students' passing rates because of COVID-19**. These decreases will be amplified across minority groups, and economically disadvantaged students.
- **Data:** For this project, my team was given multiple extensive data sets concerning standardized test scores, totalling ~20 Million unique data points covering ALL SCHOOLS in Texas which represents ALL STUDENTS. The standardized test that is required across all students in Texas is the STAAR Test, and these datasets we were given contained incredibly descriptive information reflecting the scores and passing rates for the entire population of Texan students. When combined, these datasets contained key information on student performance by school, as well as demographic information about each school's students and the school itself.

**Results**

![JPG](https://github.com/thekevinmatz/Kevins_Portfolio/blob/main/Statistical%20Analysis%20to%20Determine%20the%20Effects%20of%20Covid-19%20on%20Student%20Scores.jpg "JPG")

- Visual Analysis
  - Purely based on visual analysis, and on the diferences between passing rates before and after COVID-19, **there is a noticable decrease in student passing rates**
    - For all students, Math section passing rates suffered substantially more than other subjects
    - Passing rates for minorities seemed to suffer more
    - Economically disadvantaged students also suffered significantly more than not economically disadvantaged students

<img width="932" alt="Statistical Significant Difference - COVID-19 DATA" src="https://user-images.githubusercontent.com/129996508/230223565-ec52ec87-20bf-4e37-9d0d-384bcd27fa25.png">

- Statistical Analysis
  - Based on visual differences and difference between mean values, student passing rates suffered after COVID-19
  - However, to conclude a true effect from COVID-19, statistical analysis is required
  - In the image above, a statistically significant decrease in each of the 36 variables was recorded when measuring passing rates before and after COVID-19
    - Each "YES" Represents the statistical significance at the 99% confidence level, for each of the 36 variables that were studied
  - t-Tests
    - Lastly, we conducted Two-Sample t-Tests Assuming Equal variances comparing average pass rates in 2019 and 2021 for each subject and found that **the difference in mean passing rates for all students in each subject was statistically significant at the 99% level.**

**Limitations**

- While this analysis revealed some interesting differences from before and after Covid-19, there were some limitations to the study:
  - First, there was some misssing data from certain schools
    - Some schools had in-depth demographic missing
    - A few schools had one or more subjects missing as well
  - Second, the data year range could potentially over-exaggerate the results
    - Because the data provided is only from the years before and after Covid-19, the large difference in passing rates could potentially be because the year after was one of the worst years for passing rates in general
    - This would have to be solved by measuring data from years before and years after the pandemic, which we did not have access to
  - Lastly, the average passing rate was determined by the passing rate for each school
    - This is an issue because each school has a different amount of students, and some lower performaning, small schools would be measured the same as a higher performing, big school
  - Overall, these discrepansies were likely minimal, in terms of affecting the overall results, as this large sample size would likely cover any potential misrepresentations of the data
  
**Conclusion**

- Men and Women
  - Women suffered worse in terms of passing rates as opposed to their male counterparts, even though they had higher scores overall
- Ethnicities
  - Hispanic students witnessed the highest decrease in their passing rates
  - African American students witnessed the second highest reduction
- Economically Disadvantaged Students
  - Economically Disadvantaged students witnessed a significantly higher reduction in passing rates
  - **Being economically disadvantaged could have nearly doubled your chance of failing** in the year after the pandemic
  
**Overall, the statistical findings overwhelmingly indicated that the pandemic had negative effects on all students and their passing rates for standardized tests**

---

### The Effects of an Aging Population on GDP Growth Rate in the Developed World
Another project from my Masters degree, where me and a group of colleagues saught to discover the effects of an aging population in the developed world, and whether or not it could lead to a decrease in future GDP growth.
- Goal: To present a rational and data driven analysis to capture the effect an aging population has on the growth of a country’s per-capita economic output
- H<sub>0</sub>: The change in the population of 65+ has a negative effect on GDP per-capita growth.
- H<sub>1</sub>: The change in the population of 65+ has no effect on GDP per-capita growth.
- Data:
  - The World Bank’s “World Development Indicators” database 
  - The St. Louis Federal Reserve Economic Database (FRED) 
  - OECD Data 
  - Population data from several of the census bureau's of developed countries (USA, Canada, Australia, New Zealand, Western Europe, Japan, and South Korea)

**<a href="https://github.com/thekevinmatz/Kevins_Portfolio/blob/main/The%20Effects%20of%20an%20Aging%20Population%20on%20GDP%20Growth%20Rate%20in%20the%20Developed%20World.pdf">PDF Presentation</a>**

**Conclusion**

- Because the variable for a nation’s aging population (65<sub>it</sub>) is negative and statistically significant at a 95% confidence interval for all of our regressions, we fail to reject the null hypothesis that the change in the population of 65+ has a negative effect on GDP per-capita growth. 
- We can conclude that, in the scope of our model, **as a developed country’s population ages, they can expect to see a decline in their GDP Per Capita growth rate moving forward.**

## Python Projects

More coming soon...


# Education

- Master of Science in Economics, Texas A&M University, May 2023
- Bachelor of Science in Economics, Texas A&M University, May 2023

# Work Experience

Data Analyst | Michael Pagan (Contracted via Upwork) – Remote | June 2023 – Present

-	Engineered a comprehensive Excel-based trading dashboard incorporating 55 dynamic variables and 31 unique KPI’s for enhanced data tracking, providing a real-time overview of trading performance that automatically updates with new data
-	Employed formulas to segment each group of 20 trades as a distinct batch, in addition to the most recent 20 trades recorded
-	Automated integrations for 1000+ new weekly data points, reducing calculation and interpretation times by nearly 81%
-	Introduced 7 live time-series charts and graphs that offer at-a-glance insights into trends and patterns over time, catering to client’s need for quick decision-making on recently inputted data
-	Ensured data integrity by standardizing variable formats with automatic formulas that output data in a requested format


Data Analyst | Instrumentl (Contracted via Upwork) – Remote | December 2022 – June 2023

- Designed data dashboards in Google Sheets utilizing pivot tables, complex formulas, and a custom calculator to enable clients to convert 30,000+ live data points to a visually appealing sales team performance monitor
- Built a data tracking solution by implementing Excel formulas and macros to generate real-time, interactive graphs to monitor company growth and decrease visuals needed by 75%
- Developed predictive conversion calculators, improving capability to evaluate current and future sales team performance
- Improved efficiency by reducing errors in yearly survey data sets by 10.4% through proper handling of missing data and standardizing variable formats, ensuring accurate and consistent analysis
- Presented methodology behind data analysis in a transparent and accessible manner, providing detailed explanations of statistical models, algorithms, and data sources used, fostering client trust and confidence in analytical processes


Owner | VictoryFW - Houston, TX | February 2021 - June 2023 

- Direct online sportswear brand management, supervising all aspects tied to product sales and corresponding processe
- Analyzed consumer and competitor behavior leading to a switch from paid social media ads to influencer marketing, which began driving 55% of total sales thereafter
- Researched and identified new product trends and categories to grow product offerings and business scale, resulting in a 27% YoY increase in web sales conversion rate
- Increased website sessions from search by 163% YoY through SEO techniques based on competitor data


# Certifications

Data Analyst Associate Certificate, Data Camp, July 2023		     	   
- Exhibited proficiency in data cleaning, visualization, and statistical analysis with R on a complex dataset in a practical exa
- Identified that 6% of claims had unusual handling times, suggesting an opportunity for process optimization


Data Analysis with Python, Coursera, January 2023
- Mastered data manipulation and exploratory analysis, built a Scikit-Learn predictive model for predictive real estate pricing


# Contact Me

For any inquiries or collaborations, please feel free to reach me at:

- [LinkedIn](https://www.linkedin.com/in/kevin-matz/)
- [Email](mailto:kevinmatz@tamu.edu)
