
# Stock Price Trend Analysis System

## Project Overview
This project is a Python based system that analyzes historical stock price data for three simulated African market stocks, ALPHA, BETA, and GAMMA, across ten trading days. It was built as part of the SmartBizCrux Technologies Python Study Group, under Coach Amaefule Chukwuemeka Timothy, using only core Python fundamentals, variables, data types, operators, conditions, loops, nested loops, and user defined functions. No external libraries such as Pandas, NumPy, or Matplotlib were used.

## Business Problem
Imagine being hired as a Junior Data Analyst at an African financial research and market intelligence firm. Management wants to understand historical price movements across selected listed companies and needs answers to questions such as which stock performed strongest, which was most volatile, and what the overall trend looked like across the observation period. This project answers those questions using Python.

## Project Objectives
The program is designed to:
- Store and process multiple stock price observations
- Calculate price changes, percentage changes, and daily trend classification
- Identify overall return and classify overall trend for each stock
- Measure volatility using average daily price range
- Analyze trading volume patterns
- Compare three stocks side by side
- Present findings through a menu driven, interactive report system

## Industry Context
Capital markets give businesses and governments access to funding while giving investors ownership opportunities. According to the OECD's Africa Capital Markets Report, African equity market capitalization grew substantially between 2000 and 2024, reaching approximately USD 561 billion, yet African capital markets remain underrepresented globally, with market activity concentrated in a small number of countries, South Africa, Egypt, and Nigeria together account for more than 80 percent of capital raised in the region. This project is a small demonstration of the kind of data literacy skill needed to help close that gap.

## Dataset
The dataset consists of 30 simulated trading records, ten days each for ALPHA, BETA, and GAMMA, covering 01 August to 10 August. Each record includes date, open, high, low, close, and volume. The data was provided directly by Coach Timothy as part of the study group case study and typed manually into the program, since file handling and Pandas have not yet been introduced at this stage of the course.

## Data Dictionary

| Column | Meaning | Data Type |
|---|---|---|
| Date | Trading date | String |
| Stock | Stock identifier | String |
| Open | Opening price | Float |
| High | Highest price during the session | Float |
| Low | Lowest price during the session | Float |
| Close | Closing price | Float |
| Volume | Number of shares traded | Integer |

## Methodology
Data is stored in a dictionary keyed by stock name, with each value being a list of ten day dictionaries. Functions were divided among five team members, each responsible for a distinct set of calculations, single stock analysis, aggregates and volume, multi stock comparison, and data entry and validation. Every calculation function returns a value rather than printing directly, keeping calculation logic separate from display logic. All display and reporting happens through dedicated report functions and the main menu loop.

## Python Concepts Applied
Variables, data types, strings, arithmetic operators, comparison operators, logical operators, conditional statements, for loops, while loops, nested loops, dictionaries, lists, user defined functions, user input handling, formatted output using f strings, and error handling using try and except.

## Key Findings
ALPHA recorded the highest overall return among the three stocks, approximately 12.75 percent, moving from a first close of 102.00 to a final close of 115.00, classified as a strong upward trend. BETA recorded the lowest return, approximately negative 11.26 percent, moving from 151.00 to 134.00, classified as a strong downward trend. GAMMA also posted a positive return, approximately 6.97 percent, but showed the highest average daily price range, 13.80, and the highest average trading volume, 2,800 shares, indicating it experienced the most active and volatile trading of the three stocks over the period.

## African Market Relevance
This project reflects a small scale version of the kind of analysis real African market participants perform daily. Exchanges such as the Nigerian Exchange and the Ghana Stock Exchange publish historical price data, trading volumes, and market summaries that analysts use to track performance. The African Securities Exchanges Association works to promote capital market development and data accessibility across the continent, and Nigeria's Securities and Exchange Commission has identified financial literacy and technology adoption as priorities in its Capital Market Master Plan. Skills like the ones demonstrated in this project, turning raw price data into structured insight, directly support that broader goal of improving financial literacy and data driven decision making in African markets.

## Limitations
This analysis is based on a small simulated dataset of thirty records and does not reflect real market behavior. The trend classification thresholds used, such as what counts as a strong or moderate increase, are project specific rules, not universal financial market standards. The dataset cannot explain why prices or volumes moved the way they did, it can only describe what happened. It also cannot predict future price movement or offer investment advice of any kind.

## Future Improvements
Future versions of this project could replace the manually entered dataset with real historical data imported from a CSV file or a market data API, incorporate Pandas and NumPy for more efficient data handling, add data visualization using Matplotlib, calculate moving averages, and eventually be developed into an interactive dashboard.

## How to Run
1. Ensure Python 3 is installed on your machine.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program with `python StockPriceTrendAnalysis.py`
5. Follow the on screen menu to analyze individual stocks, compare stocks, or view volume summaries.


## Snapshots



## Author
Adekogbon Obadamilare Testimony, Team Captain, together with the Stock Price Trend Analysis team, SmartBizCrux Python Study Group.

