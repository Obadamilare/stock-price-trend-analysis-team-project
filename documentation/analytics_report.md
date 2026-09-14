# Stock Price Trend Analysis, Analytical Report

## Introduction

Stock markets generate large volumes of numerical data every trading day, but numbers alone do not tell a story. This report interprets the results produced by the Stock Price Trend Analysis System, built to answer a simple but important question. What happened to ALPHA, BETA, and GAMMA over ten trading days, and what does that movement actually mean.

## What Happened

Over the ten day observation period, the three stocks moved in noticeably different directions. ALPHA climbed steadily from a first closing price of 102.00 to a final close of 115.00, an overall gain of approximately 12.75 percent, classified as a strong upward trend. BETA moved in the opposite direction, falling from 151.00 to 134.00, a decline of approximately 11.26 percent, a strong downward trend. GAMMA also ended higher than it started, rising from 201.00 to 215.00, a gain of approximately 6.97 percent, but its path there was far less steady than ALPHA's.

## Which Stock Performed Strongest

ALPHA recorded the highest overall return of the three stocks, at approximately 12.75 percent. It also recorded the greatest number of positive trading days, six out of nine measured days, compared to BETA's one and GAMMA's five. This combination, consistent upward movement and the highest overall return, supports describing ALPHA as the strongest performer within the period analyzed.

## Which Stock Performed Weakest

BETA was the weakest performer, with a return of approximately negative 11.26 percent and eight negative trading days out of nine. Its decline was not a single sharp drop but a steady, sustained slide across nearly the entire observation window, closing lower on eight of the nine days measured after day one.

## Which Stock Showed the Greatest Volatility

Volatility in this project is measured using average daily range, the average gap between each day's high and low price. By that measure, GAMMA was clearly the most volatile stock, with an average daily range of 13.80, compared to ALPHA's 4.90 and BETA's 6.90. GAMMA's daily range grew noticeably wider as the period progressed, reaching a high low spread of 25.00 on its final trading day alone, its widest single day range in the dataset.

## What Happened During the Highest Volume Period

GAMMA also recorded the highest average trading volume of the three stocks, at 2,800 shares per day, and its single highest volume day, 4,200 shares, occurred on the final trading day, the same day it posted its largest single day price gain and its widest daily range. This is a pattern worth noting, unusually high volume occurring alongside a large positive price movement, but the dataset alone does not explain why this happened. It cannot confirm investor sentiment, news events, or any underlying cause, it can only describe that the pattern occurred.

## What Surprised Me

The most surprising pattern in this dataset was GAMMA. 
• Going in, I expected the stock with the highest overall return to also look the steadiest, since a strong finish usually suggests a smooth climb. ALPHA fit that expectation, a strong return with a consistently upward path. GAMMA did not. 
• Despite ending with a solid positive return, approximately 6.97 percent, it was also by far the most volatile of the three stocks, with an average daily range nearly three times wider than ALPHA's, and its single largest price swing happening on its very last trading day, the same day its trading volume also spiked to its highest point in the entire dataset.
• A positive result and high volatility showing up together in the same stock was not something I expected before running the numbers, it's a reminder that a good overall return can hide a genuinely bumpy road to get there, something a single overall return percentage on its own would never reveal.

## What This Dataset Cannot Tell Us

This analysis is based entirely on historical price and volume data. It cannot establish investor motivation or sentiment behind any price movement. It cannot predict future stock prices or guarantee that any observed trend will continue. It cannot speak to the underlying financial health, management quality, or fundamentals of any of these companies, since ALPHA, BETA, and GAMMA are simulated identifiers, not real listed companies. Most importantly, nothing in this report should be read as investment advice. These are observations drawn from a limited dataset, not recommendations.

## Why This Matters to Africa

African capital markets remain an important but still developing part of the continent's economic infrastructure. According to the OECD's Africa Capital Markets Report, African equity market capitalization grew to approximately USD 561 billion between 2000 and 2024, yet market activity remains concentrated in a small number of countries, with South Africa, Egypt, and Nigeria together accounting for more than 80 percent of capital raised across the region during the period studied. This concentration reflects a broader data and literacy gap, many potential investors, students, and researchers across the continent lack easy access to the tools and skills needed to interpret market data for themselves.

Exchanges such as the Nigerian Exchange and the Ghana Stock Exchange already publish historical price, volume, and market summary data, and organizations like the African Securities Exchanges Association work to make this information more accessible across the region. Nigeria's Securities and Exchange Commission has explicitly named financial literacy and investor education as priorities within its Capital Market Master Plan.

This project, small and built entirely from core Python fundamentals, is a demonstration of exactly the kind of skill that broader goal depends on, taking raw, unglamorous rows of numbers and turning them into something a person can actually read, question, and understand. It will not transform African capital markets on its own, but it represents the foundation of the analytical thinking those markets need more of, and it can be expanded meaningfully, into a tool using real NGX or GSE data, a financial literacy resource, or a research aid, once its core logic has been proven at this small scale.

## Conclusion

Given sixty seconds to summarize this analysis to a decision maker, the answer would be this. Across the ten days measured:
1. ALPHA grew steadily and consistently.
2. BETA declined steadily and consistently.  
3. GAMMA grew overall but with far more volatility and trading activity than the other two, especially toward the end of the period. 
These are patterns the data clearly supports. What caused them, investor behavior, external news, or something else entirely, is something this dataset cannot answer, and any decision maker acting on this report should treat these findings as a description of what happened, not an explanation of why, and certainly not a prediction of what happens next.
