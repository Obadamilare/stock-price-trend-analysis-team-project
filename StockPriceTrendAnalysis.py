# ==== TEAM CAPTAIN: Data entry and validation ====

def build_stock_data():
     raw_records = [
        # ALPHA
        {"date": "01-Aug", "stock": "ALPHA", "open": 100, "high": 103, "low": 98, "close": 102, "volume": 1200},
        {"date": "02-Aug", "stock": "ALPHA", "open": 102, "high": 105, "low": 101, "close": 104, "volume": 1350},
        {"date": "03-Aug", "stock": "ALPHA", "open": 104, "high": 106, "low": 102, "close": 103, "volume": 1100},
        {"date": "04-Aug", "stock": "ALPHA", "open": 103, "high": 107, "low": 102, "close": 106, "volume": 1500},
        {"date": "05-Aug", "stock": "ALPHA", "open": 106, "high": 109, "low": 104, "close": 108, "volume": 1650},
        {"date": "06-Aug", "stock": "ALPHA", "open": 108, "high": 110, "low": 106, "close": 107, "volume": 1400},
        {"date": "07-Aug", "stock": "ALPHA", "open": 107, "high": 111, "low": 105, "close": 110, "volume": 1800},
        {"date": "08-Aug", "stock": "ALPHA", "open": 110, "high": 113, "low": 108, "close": 112, "volume": 2100},
        {"date": "09-Aug", "stock": "ALPHA", "open": 112, "high": 114, "low": 109, "close": 111, "volume": 1900},
        {"date": "10-Aug", "stock": "ALPHA", "open": 111, "high": 116, "low": 110, "close": 115, "volume": 2300},

        # BETA
        {"date": "01-Aug", "stock": "BETA", "open": 150, "high": 153, "low": 147, "close": 151, "volume": 1000},
        {"date": "02-Aug", "stock": "BETA", "open": 151, "high": 154, "low": 149, "close": 153, "volume": 1100},
        {"date": "03-Aug", "stock": "BETA", "open": 153, "high": 155, "low": 148, "close": 149, "volume": 1700},
        {"date": "04-Aug", "stock": "BETA", "open": 149, "high": 151, "low": 145, "close": 147, "volume": 1900},
        {"date": "05-Aug", "stock": "BETA", "open": 147, "high": 150, "low": 143, "close": 145, "volume": 2100},
        {"date": "06-Aug", "stock": "BETA", "open": 145, "high": 148, "low": 141, "close": 143, "volume": 2300},
        {"date": "07-Aug", "stock": "BETA", "open": 143, "high": 146, "low": 139, "close": 140, "volume": 2500},
        {"date": "08-Aug", "stock": "BETA", "open": 140, "high": 144, "low": 136, "close": 138, "volume": 2800},
        {"date": "09-Aug", "stock": "BETA", "open": 138, "high": 142, "low": 134, "close": 136, "volume": 3000},
        {"date": "10-Aug", "stock": "BETA", "open": 136, "high": 140, "low": 132, "close": 134, "volume": 3200},

        # GAMMA
        {"date": "01-Aug", "stock": "GAMMA", "open": 200, "high": 204, "low": 196, "close": 201, "volume": 1500},
        {"date": "02-Aug", "stock": "GAMMA", "open": 201, "high": 206, "low": 198, "close": 203, "volume": 1600},
        {"date": "03-Aug", "stock": "GAMMA", "open": 203, "high": 208, "low": 197, "close": 199, "volume": 2100},
        {"date": "04-Aug", "stock": "GAMMA", "open": 199, "high": 205, "low": 193, "close": 202, "volume": 2300},
        {"date": "05-Aug", "stock": "GAMMA", "open": 202, "high": 210, "low": 195, "close": 207, "volume": 2700},
        {"date": "06-Aug", "stock": "GAMMA", "open": 207, "high": 212, "low": 200, "close": 204, "volume": 2900},
        {"date": "07-Aug", "stock": "GAMMA", "open": 204, "high": 215, "low": 198, "close": 210, "volume": 3200},
        {"date": "08-Aug", "stock": "GAMMA", "open": 210, "high": 218, "low": 203, "close": 206, "volume": 3600},
        {"date": "09-Aug", "stock": "GAMMA", "open": 206, "high": 214, "low": 199, "close": 201, "volume": 3900},
        {"date": "10-Aug", "stock": "GAMMA", "open": 201, "high": 220, "low": 195, "close": 215, "volume": 4200},
    ]

     stock_data = {}

     for record in raw_records:
        stock_name = record["stock"]
        day_record = {"date": record["date"],    #I can also use pop() here to remove the stock name from the dictionary.
                      "open": record["open"],
                      "high": record["high"],
                      "low": record["low"], 
                      "close": record["close"],
                      "volume": record["volume"],
                      }
        if stock_name not in stock_data:
            stock_data[stock_name] = []
        stock_data[stock_name].append(day_record)
  
     return stock_data



def validate_records(stock_data):
    issues = []

    for stock_name, records  in stock_data.items():      #Or, for stock_name in stock_data:
        for record in records:   #Or, for record in stock_data[stock_name] 
            if record["close"] <0:
                issues.append(f"{stock_name}{record["date"]} : close price not positive")

            if record["high"] <= record["low"]:
                issues.append(f"{stock_name}{record["date"]} : high is less than low")

            if record["high"] <= record["open"]:
                issues.append(f"{stock_name}{record["date"]} : high is less than open")

            if record["high"] <= record["close"]:
                issues.append(f"{stock_name}{record["date"]} : high is less than close")

            if record["low"] >= record["open"]:
                issues.append(f"{stock_name}{record["date"]} : low is greater than open")

            if record["low"] >= record["close"]:
                issues.append(f"{stock_name}{record["date"]} : low is greater than close")

            if record["volume"] <= 0:
                issues.append(f"{stock_name}{record["date"]} : volume is zero or negative")

    return issues

        


# ==== ENIOLA: Single stock analysis ====
def get_first_close(stock_data, stock_name):
    """
    Calculating the first close of selected stock.
    The close represent the price at which the stock ended at the trading day.

    Args:
    stock_data = Dictionary containing stock data.
    stock_name = Name of the selected stock.
    
    Return:
    The first closing price of the selected stock.
    """
    first_close = stock_data[stock_name][0]["close"] #[stock_name][0] means day one data for the selected stock name
    return first_close


def get_average_close(stock_data, stock_name):

    """
    Calculate the average closing price of selected stock.
    The close represent the price at which the stock ended at the trading day.

    Args:
    stock_data = Dictionary containing stock data.
    stock_name = Name of the selected stock.
    
    Return:
    The average closing price of the selected stock.
    """
    total_close = 0 # variable initialization

    for record in stock_data[stock_name]:
        # Add each day's closing price to the total close
        total_close += record["close"]

    average_close = total_close/ len(stock_data[stock_name])

    return average_close

def get_highest_close(stock_data, stock_name):

     """
    Calculate the highest closing price of selected stock.
    The close represent the price at which the stock ended at the trading day.

    Args:
    stock_data = Dictionary containing stock data.
    stock_name = Name of the selected stock.
    
    Return:
    The highest closing price of selected stock
    """
     highest_close = stock_data[stock_name][0]["close"] 

     for record in stock_data[stock_name]:
        # Compare each closing price to the current highest close
        if record["close"] > highest_close:
            highest_close = record["close"]
    
     return highest_close
    

def get_lowest_close(stock_data, stock_name):
    """
    Calculate the lowest closing price of selected stock.
    The close represent the price at which the stock ended at the trading day.

    Args:
    stock_data = Dictionary containing stock data.
    stock_name = Name of the selected stock.
    
    Return:
    The lowest closing price of selected stock
    """
    lowest_close = stock_data[stock_name][0]["close"] #[stock_data][0] means first close

    for record in stock_data[stock_name]:
        # Compare each closing price to the current lowest close
        if record["close"] < lowest_close:
            lowest_close = record["close"]
    

    return lowest_close

def get_daily_price_changes(stock_data, stock_name):
    """
    Calculate the daily price and percentage change for selected stock
    Compare each day closing price with the previous day
    Args:
    stock_data = Dictionary containing stock data.
    stock_name = Name of the selected stock to analyze.

    Returns:
    A list containing the date, price change, percentage change, and trend for each trading day.
    """
    # Get the price data for the selected stock
    stock = stock_data[stock_name]
    
    # Create an empty list to store daily results
    results = []
    
    # Start from the second trading day because the first trading day does not have a previous closing price to compare with
    for i in range (1, len(stock)):

        # Get previous closing price
        previous_close = stock[i -1]["close"]
        # Get current closing price
        current_close = stock[i]["close"]

        # Calculate the price change
        price_change = current_close - previous_close

        # Calculate the percentage price change
        percentage_change = (price_change/previous_close) * 100
        percentage_change = round(percentage_change,2)

        # Classify daily price movement based on percentage change
        if percentage_change > 2:
            trend = "Strong Increase"
        elif percentage_change > 0:
            trend = "Moderate Increase"
        elif percentage_change == 0:
            trend = "No Change"
        elif percentage_change >= -2:
            trend = "Moderate Decrease"
        else:
            trend = "Strong Decrease"

        # Store data analysis in a dictionary
        result ={
            "date": stock[i]["date"],
            "stock_name":stock_name,
            "close": current_close,
            "price_change": price_change,
            "percentage_change": percentage_change,
            "trend": trend
            }

        #Add the daily result to the result list
        results.append(result)

    return results

def print_daily_report(stock_data, stock_name):
    """Print the daily stock report in a table"""
    
    # Get daily price changes
    results = get_daily_price_changes(stock_data, stock_name)
    
    # Print the table headings
    print(f"{'DATE':<10}{'STOCK':<10}{'CLOSE':<10}{'CHANGE':<10}{'RETURN':<12}{'TREND':<20}")
    print("-" * 72)
    
    # Print the first day as START, no comparison possible
    first_day = stock_data[stock_name][0]
    print(f"{first_day['date']:<10}{stock_name:<10}{first_day['close']:<10}{'--':<10}{'--':<12}{'START':<20}")
    
    # Print each remaining day's result
    for result in results:
        print(f"{result['date']:<10}{stock_name:<10}{result['close']:<10}{result['price_change']:<+10}{str(result['percentage_change']) + '%':<12}{result['trend']:<20}")
     
def get_average_daily_range(stock_data, stock_name):

    """
    Calculate the average daily range of selected stock.

    Args:
    stock_data = Dictionary containing stock data.
    stock_name = Name of the selected stock.
    
    Return:
    The average daily range of selected stock
    """

    total_range = 0 # initialize total range to zero

    for record in stock_data[stock_name]:
        # Deduct low price from high price to get daily range
        daily_range = record["high"] - record["low"]
        # Add each daily range to the total range
        total_range += daily_range

    average_range = total_range/len(stock_data[stock_name])
    return average_range


# ==== VICTOR: Aggregate and volume ====
def get_overall_return(stock_data, stock_name):

    """this function is to calculate the overall return value 
    of the stock_data for each stock_name.
    
    Args:
    Stock_data = refers to the dataset provided for the stocks evaluation
    Stock_name = refers to the name of each given stock.
      
    Returns:
    The function is expected to return the overall_return_value
    od the stock_data depending on the stock_name selected. """

    first_close = stock_data[stock_name][0]["close"]
    final_close = stock_data[stock_name][-1]["close"]
    
    overall_change = final_close - first_close
    overall_return_value = (overall_change / first_close) * 100
    
    return overall_return_value

def classify_overall_trend(overall_return_value):

    """This function is to classify the overall_return_value into
    different trend classifications based on the result returned by 
    the overall_return_value.
    
    Args:
    overall_return_value = refers the to the percentage of the overall change
    in the stock market closing rates in the span of the selected days.
    
    Returns:
    This functions is expected to return the Trend classification of the
    overall_return_value based on the percentage change that occurred within
    the selected stock. """

    if overall_return_value > 5:
        trend = "STRONG UPWARD TREND"
    elif overall_return_value > 1:
        trend = "MODERATE UPWARD TREND"
    elif overall_return_value >= -1:
        trend = "RELATIVELY STABLE"
    elif overall_return_value >= -5:
        trend = "MODERATE DOWNWARD TREND"
    else:
        trend = "STRONG DOWNWARD TREND"
    
    return trend

def count_positive_negative_days(daily_change_list):
    """This function is to count the number of positive_days
    and negative_days, depending on the daily_change_list.
    And also to return the days there was no change.
    
    Args:
    daily_change_list = refers to the range at which the selected
    stock price changes per day.
    
    Returns :
    This function is expected to return the number of postive_days,
    negative_days, and days there were no change on the difference
    in the selected stock prices per day."""

    positive_days = 0
    negative_days = 0
    no_change = 0

    for record in daily_change_list:
        if record ["price_change"] > 0:
            positive_days += 1

        elif record ["price_change"] < 0 :
            negative_days += 1

        else:
            no_change += 1

    
    
    return {
            "positive_days" :positive_days,
            "negative_days" :negative_days,
            "no_change" : no_change 
    }



def get_volume_summary(stock_data, stock_name):

    """This function is to get the summary of the volume analysis of
    the stock_data, depending on the stock_name selected.
    
    Args: 
    Stock_data = refers to the given dataset of the stocks provided
    Stock_name = refers to the name of each given stock.
    
    Returns:
    this function is to return the summary of the volume calculations;
    that is, the total_volume, average_volume,highest_volume and lowest_volume."""


    stock = stock_data[stock_name]
    total_volume = 0

    # a for loop is deployed below for the program...
    # ...to be able to go through all the records under volume. 
    for record in stock:
        total_volume += record["volume"]

    average_volume = total_volume / len(stock)

    highest_volume = stock[0]["volume"]
    lowest_volume = stock[0]["volume"]

    for record in stock:
        if record["volume"] > highest_volume:
            highest_volume = record["volume"]

        if record["volume"] < lowest_volume:
            lowest_volume = record["volume"]

    return {
        "total_volume" :total_volume, 
        "average_volume" :average_volume, 
        "highest_volume" :highest_volume,
        "lowest_volume" : lowest_volume
    }


# ==== FRANKLYN: Comparison and report ====

def compare_stocks(stock_data):
    """
    Processes all stock data to:
    1. Compute summary metrics for ALPHA,BETA,and GAMMA
    2. Print individula stock summary reports
    3. Generate a multi-stock comparison table
    4. Print automated answers to the comparative questions
    """
    stock_summaries =  {}

    # iterating through the stocks
    for stock_name, raw_records in stock_data.items():
        first_close = get_first_close(stock_data, stock_name)
        final_close = raw_records[-1]["close"]
        average_close = get_average_close(stock_data,stock_name)
        highest_close = get_highest_close(stock_data,stock_name)
        lowest_close = get_lowest_close(stock_data,stock_name)

        overall_change = final_close - first_close
        overall_return = get_overall_return(stock_data,stock_name)
        trend = classify_overall_trend(overall_return)

        # build a daily price change list
        daily_price_change = get_daily_price_changes(stock_data, stock_name)

        #get count days number
        count_dictionary = count_positive_negative_days(daily_price_change)
        positive_days = count_dictionary["positive_days"]
        negative_days = count_dictionary["negative_days"]
        no_change_days = count_dictionary["no_change"]

        # calculating for volume metrics and average daily range
        volume_summary = get_volume_summary(stock_data, stock_name)
        average_volume = volume_summary["average_volume"]
        avg_daily_range = get_average_daily_range(stock_data, stock_name)

        # storing the metrics in a dictionary
        stock_summaries[stock_name] = {
            "first_close": first_close,
            "final_close": final_close,
            "average_close": average_close,
            "highest_close": highest_close,
            "lowest_close": lowest_close,
            "overall_change": overall_change,
            "overall_return": overall_return,
            "positive_days": positive_days,
            "negative_days": negative_days,
            "no_change_days": no_change_days,
            "average_volume": average_volume,
            "average_daily_range": avg_daily_range,
            "trend": trend
        }

    # ==========================================
    # Multi-Stock Comparison Table
    # ==========================================
    print("=" * 115)
    print(" MULTI-STOCK COMPARISON TABLE ")
    print("=" * 115)
    headers = f"{'STOCK':<8} | {'FIRST':<8} | {'FINAL':<8} | {'AVG CLOSE':<10} | {'HIGH':<8} | {'LOW':<8} | {'RETURN (%)':<11} | {'AVG VOL':<10} | {'TREND':<22}"
    print(headers)
    print("-" * 115)

    for stock_name, summary in stock_summaries.items():
        row = (
                f"{stock_name:<8} | "
                f"{summary['first_close']:<8.2f} | "
                f"{summary['final_close']:<8.2f} | "
                f"{summary['average_close']:<10.2f} | "
                f"{summary['highest_close']:<8.2f} | "
                f"{summary['lowest_close']:<8.2f} | "
                f"{summary['overall_return']:<11.2f} | "
                f"{summary['average_volume']:<10.2f} | "
                f"{summary['trend']:<22}"
            )
        print(row)
    print("=" * 115)
    print("\n\n")

    return stock_summaries


        

def answer_comparative_questions(stock_summaries):
    
    # Comparative Questions Answers
    

    # Getting the first stock as the starting point
    first_stock = list(stock_summaries.keys())[0]

    # Initial values for comparison
    highest_return_stock = first_stock
    highest_return = stock_summaries[first_stock]["overall_return"]

    lowest_return_stock = first_stock
    lowest_return = stock_summaries[first_stock]["overall_return"]

    highest_average_stock = first_stock
    highest_average = stock_summaries[first_stock]["average_close"]

    largest_range_stock = first_stock
    largest_range = stock_summaries[first_stock]["average_daily_range"]

    highest_volume_stock = first_stock
    highest_volume = stock_summaries[first_stock]["average_volume"]

    most_positive_stock = first_stock
    most_positive_days = stock_summaries[first_stock]["positive_days"]

    # Compare all the stocks
    for stock_name, summary in stock_summaries.items():

        # Highest overall return
        if summary["overall_return"] > highest_return:
            highest_return = summary["overall_return"]
            highest_return_stock = stock_name

        # Lowest overall return
        if summary["overall_return"] < lowest_return:
            lowest_return = summary["overall_return"]
            lowest_return_stock = stock_name

        # Highest average closing price
        if summary["average_close"] > highest_average:
            highest_average = summary["average_close"]
            highest_average_stock = stock_name

        # Largest average daily price range
        if summary["average_daily_range"] > largest_range:
            largest_range = summary["average_daily_range"]
            largest_range_stock = stock_name

        # Highest average volume
        if summary["average_volume"] > highest_volume:
            highest_volume = summary["average_volume"]
            highest_volume_stock = stock_name

        # Greatest number of positive days
        if summary["positive_days"] > most_positive_days:
            most_positive_days = summary["positive_days"]
            most_positive_stock = stock_name


    # Display comparative questions and answers
    print("=" * 70)
    print(" COMPARATIVE QUESTIONS & ANSWERS ")
    print("=" * 70)

    print(f"1. Highest overall return          : "
        f"{highest_return_stock} ({highest_return:.2f}%)")

    print(f"2. Lowest return                   : "
        f"{lowest_return_stock} ({lowest_return:.2f}%)")

    print(f"3. Highest average closing price   : "
        f"{highest_average_stock} ({highest_average:.2f})")

    print(f"4. Largest daily price range       : "
        f"{largest_range_stock} ({largest_range:.2f})")

    print(f"5. Highest average volume           : "
        f"{highest_volume_stock} ({highest_volume:.2f})")

    print(f"6. Greatest number of positive days : "
        f"{most_positive_stock} ({most_positive_days} days)")

    print(f"7. Most volatile (by range)         : "
        f"{largest_range_stock} ({largest_range:.2f})")

    print("=" * 70)


    return None
    


# ==== TEAM CAPTAIN: Remaing Functions and Menu ====

def get_highest_performing_stock(stock_data):
    best_stock = None
    best_return = None
    

    for stock_name in stock_data:
        current_return = get_overall_return(stock_data, stock_name)
        if best_return is None or current_return > best_return:
            best_return = current_return
            best_stock = stock_name 
    best_overall_trend = classify_overall_trend(best_return)
    return best_stock, best_return, best_overall_trend


    
def get_lowest_performing_stock(stock_data):
    worst_stock = None
    worst_return = None
    

    for stock_name in stock_data:
        current_return = get_overall_return(stock_data, stock_name)
        if worst_return is None or current_return < worst_return:
            worst_return = current_return
            worst_stock = stock_name 
    worst_overall_trend = classify_overall_trend(worst_return)
    return worst_stock, worst_return, worst_overall_trend



def build_stock_analysis_report(stock_data, stock_name):
    first_close = get_first_close(stock_data, stock_name)
    final_close = stock_data[stock_name][-1]["close"]
    overall_price_change = final_close - first_close
    
    overall_return_value = get_overall_return(stock_data, stock_name)
    overall_trend = classify_overall_trend(overall_return_value)
    
    daily_change_list = get_daily_price_changes(stock_data, stock_name)
    positive_negative_days = count_positive_negative_days(daily_change_list)
    
    volume_data = get_volume_summary(stock_data, stock_name)

    print(f"""
        {"="*50}
            STOCK PRICE TREND ANALYSIS SYSTEM
        {"="*50}

        Stock: {stock_name}

        First Closing price: {first_close:.2f}
        Final Closing Price: {final_close:.2f}
        Average Closing Price: {get_average_close(stock_data, stock_name):.2f}

        Highest Closing Price: {get_highest_close(stock_data, stock_name):.2f}
        Lowest Closing Price: {get_lowest_close(stock_data, stock_name):.2f}

        Overall Price Change: {overall_price_change:.2f}
        Overall Return: {overall_return_value:.2f}%

        Positive Days: {positive_negative_days["positive_days"]}
        Negative Days: {positive_negative_days["negative_days"]}
        No Change days: {positive_negative_days["no_change"]}

        Average Daily Range: {get_average_daily_range(stock_data, stock_name):.2f}
        Average Trading Volume: {volume_data["average_volume"]:.2f}

        Overall Trend: 
        {overall_trend}
        {"="*50}
                """)
    return None


#SYSTEM MENU
stock_data = build_stock_data()
issues = validate_records(stock_data)


if issues:
    print("DATA VALIDATION FAILS.")
    for issue in issues:
        print(issue)
        
else:
    print("DATA VALIDATED SUCCESSFULLY. \n")

    while True:
        print("""
    1. Analyse a stock
    2. Compare stocks
    3. View highest-performing stock
    4. View lowest-performing stock
    5. View trading-volume summary
    6. Exit
              \n""" )
        try:
            response = int(input("Enter a number: "))
            if response == 1:
                while True:
                    print(""" 
    1. Analyse ALPHA
    2. Analyse BETA
    3. Analyse GAMMA
    4. Back """)
                    try:
                        response = int(input("Enter a number: "))
                        if response == 1:
                            #Call the functions to analyse ALPHA stocks
                            stock_name = "ALPHA"
                            print("="*50)
                            print("ANALYSE STOCK ALPHA")
                            print("="*50)
                            print_daily_report(stock_data, stock_name)


                            print("\n\n")
                            build_stock_analysis_report(stock_data, stock_name)
                            
                            
                        elif response == 2:
                            #Call the functions to analyse BETA stocks
                            stock_name = "BETA"
                            
                            print("="*50)
                            print("ANALYSE STOCK BETA")
                            print("="*50)
                            print_daily_report(stock_data, stock_name)

                            print("\n\n")
                            build_stock_analysis_report(stock_data, stock_name)

                        elif response == 3:
                            #Call the functions to analyse GAMMA stocks
                            stock_name = "GAMMA"
                            
                            print("="*50)
                            print("ANALYSE STOCK GAMMA")
                            print("="*50)
                            print_daily_report(stock_data, stock_name)

                            print("\n\n")
                            build_stock_analysis_report(stock_data, stock_name)

                        elif response == 4:
                            break
                        else:
                            print("Enter a valid number.")
                            continue
                    except ValueError:
                        print("Enter a valid number.")
                        continue
            elif response == 2:
                #Call the function to compare all the stocks
                stock_summaries = compare_stocks(stock_data)

                answer_comparative_questions(stock_summaries)
                
            elif response == 3:
                #Write the code to view highest-performing stock
                best_stock, best_return, best_overall_trend = get_highest_performing_stock(stock_data)
                print(f"""
HIGHEST PERFORMING STOCK:
                      
STOCK NAME: {best_stock}
BEST RETURN:{best_return:.2f}%
TREND: {best_overall_trend}""")

            elif response == 4:
                #Write the code to view lowest-performing stock
                worst_stock, worst_return, worst_overall_trend = get_lowest_performing_stock(stock_data)
                print(f"""
LOWEST PERFORMING STOCK:
                      
STOCK NAME: {worst_stock}
BEST RETURN:{worst_return:.2f}%
TREND: {worst_overall_trend}""")


            elif response == 5:
                #Write the code to view trading-volume summary
                print("="*50)
                print("TRADING VOLUME SUMMARY")
                print("="*50)
                for stock_name in stock_data:
                    volume_data = get_volume_summary(stock_data, stock_name)
                    print(f"""
STOCK: {stock_name}
TOTAL VOLUME: {volume_data["total_volume"]}
AVERAGE VOLUME: {volume_data["average_volume"]:.2f}
HIGHEST VOLUME: {volume_data["highest_volume"]:.2f}
LOWEST VOLUME: {volume_data["lowest_volume"]:.2f} \n""")

                
            elif response == 6:
                print("Program successfully terminated.")
                break
            else:
                print("Enter a valid number")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

    




    


