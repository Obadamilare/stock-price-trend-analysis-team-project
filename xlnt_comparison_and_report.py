# ==== PERSON 5: Comparison and report ====

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
        print(" MULTI-STOCK COMPARISON TABLE ".center(115, "="))
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


        
    # ==========================================
    # Comparative Questions Answers
    # ==========================================

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
    print(" COMPARATIVE QUESTIONS & ANSWERS ".center(70, "="))
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


    return stock_summaries
    






        