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

    # The individual stock reports
    for symbol, raw_records in stock_data.items():
        first_close = raw_records[0]["close"]
        final_close = raw_records[-1]["close"]

        average_close = sum(r["close"] for r in raw_records) / len(raw_records)
        highest_close = max(r["close"] for r in raw_records)
        lowest_close = min(r["close"] for r in raw_records)

        overall_change = final_close - first_close
        overall_return = (overall_change / first_close) * 100

        positive_days = 0
        negative_days = 0
        no_change_days = 0
        for i in range(1, len(raw_records)):
            daily_price_change = raw_records[i]["close"] - raw_records[i - 1]["close"]
            if daily_price_change > 0:
                positive_days += 1
            elif daily_price_change < 0:
                negative_days += 1
            else:
                no_change_days += 1

        average_range = sum(r["high"] - r["low"] for r in raw_records) / len(raw_records)
        average_volume = sum(r["volume"] for r in raw_records) / len(raw_records)

        # for the overall trend classification
        if overall_return > 5:
            trend = "STRONG UPWARD TREND"
        elif overall_return > 1:
            trend = "MODERATE UPWARD TREND"
        elif overall_return >= -1:
            trend = "RELATIVELY STABLE"
        elif overall_return >= -5:
            trend = "MODERATE DOWNWARD TREND"
        else:
            trend = "STRONG DOWNWARD TREND"

        # storing the parameters for comparison using stock summaries
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
            "average_range": average_range,
            "average_volume": average_volume,
            "trend": trend
        }

        # individual output format
        print("="*58)
        print("STOCK PRICE TREND ANALYSIS SYSTEM".center)
        print("="*58)
        print()
        print(f"""
        Stock: {symbol}

        First Closing Price: {first_close:.2f}
        Final Closing Price: {final_close:.2f}
        Average Closing Price: {average_close:.2f}

        Highest Closing Price: {highest_close:.2f}
        Lowest Closing Price: {lowest_close:.2f}

        Overall Price Change: {overall_change:.2f}
        Overall Return: {overall_return:.2f}

        Posistive Days: {positive_days:.2f}
        Negative Days: {negative_days:.2f}
        No Change Days: {no_change_days:.2f}

        Average Daily Range: {average_range:.2f}
        Average Trading Volume: {average_volume}

        Overall Trend:
        {trend} """)
        print()
        print("="*58)
        

        

        
        
    