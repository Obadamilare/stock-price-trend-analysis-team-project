# ==== PERSON 4: Aggregate and volume ====
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

        else:
            lowest_volume = record["volume"]

    return {
        "total_volume" :total_volume, 
        "average_volume" :average_volume, 
        "highest_volume" :highest_volume,
        "lowest_volume" : lowest_volume
    }