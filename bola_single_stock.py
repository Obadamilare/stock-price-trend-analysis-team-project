# ==== PERSON 3: Single stock analysis ====
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
     highest_close = stock_data[stock_name][0]["close"] #[stock_data][0] means first close

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
    
    print("Lowest Closing Price:",lowest_close)
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
        current_close = stock[i][:"close"]

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
    print(f"{first_day['date']:<10}{stock_name:<10}{first_day['close']:<10}{'--':<10}{'START':<12}{'--':<20}")
    
    # Print each remaining day's result
    for result in results:
        print(f"{result['date']:<10}{stock_name:<10}{result['close']:<10}{result['change']:<+10}{str(result['percentage_change']) + '%':<12}{result['trend']:<20}")
     
def average_daily_range(stock_data, stock_name):

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

