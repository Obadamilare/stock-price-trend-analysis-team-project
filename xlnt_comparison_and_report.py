# ==== PERSON 5: Comparison and report ====
# importing functions from other branches
from bola_single_stock import (get_first_close,get_average_close,get_lowest_close,get_highest_close,average_daily_range)
from vicky_aggregate_and_volume import (get_overall_return,get_volume_summary,classify_overall_trend,count_positive_negative_days)

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
    for symbol, raw_records in stock_data.items():
        first_close = get_first_close(stock_data,symbol)
        final_close = raw_records[-1]["close"]
        average_close = get_average_close(stock_data,symbol)
        highest_close = get_highest_close(stock_data,symbol)
        lowest_close = get_lowest_close(stock_data,symbol)

        overall_change = final_close - first_close
        overall_return = get_overall_return(stock_data,symbol)
        trend = classify_overall_trend(overall_return)

        # build a daily price change list
        daily_price_change = [
            {"price_change": raw_records[i]["close"] - raw_records[i - 1]["close"]}
            for i in range(1, len(raw_records))
        ]
        positive_days, negative_days, no_change_days = count_positive_negative_days(daily_price_change)

        # calculating for volume metrics and average daily range
        volume_summary = get_volume_summary(stock_data, symbol)
        average_volume = volume_summary["average_volume"]
        avg_daily_range = average_daily_range(stock_data, symbol)

        # storing the metrics in a dictionary
        stock_summaries[symbol] = {
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

        # printing the individual stock report
        print("*" * 50)
        print(f" STOCK PRICE TREND ANALYSIS SYSTEM ({symbol}) ".center(50, "*"))
        print("*" * 50)
        print()
        print(f"First Closing Price: {first_close:.2f}")
        print(f"Final Closing Price: {final_close:.2f}")
        print(f"Average Closing Price: {average_close:.2f}")
        print()
        print(f"Highest Closing Price: {highest_close:.2f}")
        print(f"Lowest Closing Price: {lowest_close:.2f}")
        print()
        print(f"Overall Price Change: {overall_change:.2f}")
        print(f"Overall Return: {overall_return:.2f}%")
        print()
        print(f"Positive Days: {positive_days}")
        print(f"Negative Days: {negative_days}")
        print(f"No Change Days: {no_change_days}")
        print()
        print(f"Average Daily Range: {avg_daily_range:.2f}")
        print(f"Average Trading Volume: {average_volume:.2f}")
        print()
        print(f"Overall Trend: {trend}")
        print("*" * 50)
        print("\n")

    # ==========================================
    # Multi-Stock Comparison Table
    # ==========================================
    print("=" * 115)
    print(" MULTI-STOCK COMPARISON TABLE ".center(115, "="))
    print("=" * 115)
    headers = f"{'STOCK':<8} | {'FIRST':<8} | {'FINAL':<8} | {'AVG CLOSE':<10} | {'HIGH':<8} | {'LOW':<8} | {'RETURN (%)':<11} | {'AVG VOL':<10} | {'TREND':<22}"
    print(headers)
    print("-" * 115)

    for symbol, summary in stock_summaries.items():
        row = (
            f"{symbol:<8} | "
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
    print("\n")

    # ==========================================
    # Comparative Questions Answers
    # ==========================================
    # identifying top performers using max/min key evaluations
    question_1 = max(stock_summaries.items(), key=lambda x: x[1]["overall_return"])
    question_2 = min(stock_summaries.items(), key=lambda x: x[1]["overall_return"])
    question_3 = max(stock_summaries.items(), key=lambda x: x[1]["average_close"])
    question_4 = max(stock_summaries.items(), key=lambda x: x[1]["average_daily_range"])
    question_5 = max(stock_summaries.items(), key=lambda x: x[1]["average_volume"])
    question_6 = max(stock_summaries.items(), key=lambda x: x[1]["positive_days"])
    question_7 = max(stock_summaries.items(), key=lambda x: x[1]["average_daily_range"])

    print("=" * 70)
    print(" COMPARATIVE QUESTIONS & ANSWERS ".center(70, "="))
    print("=" * 70)
    print(f"1. Highest overall return        : {question_1[0]} ({question_1[1]['overall_return']:.2f}%)")
    print(f"2. Lowest return                 : {question_2[0]} ({question_2[1]['overall_return']:.2f}%)")
    print(f"3. Highest average closing price : {question_3[0]} ({question_3[1]['average_close']:.2f})")
    print(f"4. Largest daily price range     : {question_4[0]} ({question_4[1]['average_daily_range']:.2f})")
    print(f"5. Highest average volume        : {question_5[0]} ({question_5[1]['average_volume']:.2f})")
    print(f"6. Greatest number of positive days: {question_6[0]} ({question_6[1]['positive_days']} days)")
    print(f"7. Most volatile (by Range)      : {question_7[0]} ({question_7[1]['average_daily_range']:.2f})")
    print("=" * 70)

    return stock_summaries

from ifeanyichukwu_data_collection import build_stock_data

stock_data = build_stock_data()
compare_stocks(stock_data)


        