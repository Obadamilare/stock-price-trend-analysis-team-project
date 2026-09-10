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
    worst_overall_trend = classify_overall_trend(worst__return)
    return worst_stock, worst_return, worst_overall_trend



def build_stock_analysis_report(stock_data, stock_name):
    first_close = get_first_close(stock_data, stock_name)
    final_close = stock_data[stock_name][-1]["close"]
    overall_price_change = final_close - first_close
    
    overall_return_value = overall_return(stock_data, stock_name)
    overall_trend = classify_overall_trend(overall_return_value)
    
    daily_change_list = daily_price_changes(stock_data, stock_name)
    positive_negative_days = count_positive_negative_days(daily_change_list)
    
    volume_data = get_volume_summary(stock_data, stock_name)

    print(f"""
        {"="*50}
            STOCK PRICE TREND ANALYSIS SYSTEM
        {"="*50}

        Stock: {stock_name}

        First Closing price: {first_close}
        Final Closing Price: {final_close}
        Average Closing Price: {get_average_close(stock_data, stock_name)}

        Highest Closing Price: {get_highest_close(stock_data, stock_name)}
        Lowest Closing Price: {get_lowest_close(stock_data, stock_name)}

        Overall Price Change: {overall_price_change}
        Overall Return: {overall_return_value:.2f}%

        Positive Days: {positive_negative_days["positive_days"]}
        Negative Days: {positive_negative_days["negative_days"]}
        No Change days: {positive_negative_days["no_change"]}

        Average Daily Range: {average_daily_range(stock_data, stock_name)}
        Average Trading Volume: {volume_data["average_volume"]}

        Overall Trend: 
        {overall_trend}
        {"="*50}
                """)
    return None


#SYSTEM MENU
#Calling all functions
stock_data = build_stock_data()
issues = validate_records(stock_data)

print(stock_data)


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
                            print_daily_report(stock_data, stock_name)
                            
                            
                        elif response == 2:
                            #Call the functions to analyse BETA stocks
                            stock_name = "BETA"
                            print_daily_report(stock_data, stock_name)
                        elif response == 3:
                            #Call the functions to analyse GAMMA stocks
                            stock_name = "GAMMA"
                            print_daily_report(stock_data, stock_name)
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
                pass
            elif response == 3:
                #Write the code to view highest-performing stock
                best_stock, best_return, best_overall_trend = get_highest_performing_stock(stock_data)
                print(f"""
                      HIGHEST PERFORMING STOCK:
                        STOCK NAME: {best_stock}
                        BEST RETURN:{best_return}
                        TREND: {best_overall_trend}""")

            elif response == 4:
                #Write the code to view lowest-performing stock
                worst_stock, worst_return, worst_overall_trend = get_lowest_performing_stock(stock_data)
                print(f"""
                      LOWEST PERFORMING STOCK:
                        STOCK NAME: {worst_stock}
                        BEST RETURN:{worst_return}
                        TREND: {worst_overall_trend}""")


            elif response == 5:
                #Write the code to view trading-volume summary
                for stock_name in stock_data:
                    volume_data = get_volume_summary(stock_data, stock_name)
                    print(f"""
                            STOCK: {stock_name}
                            TOTAL VOLUME: {volume_data["total_volume"]}
                            AVERAGE VOLUME: {volume_data["average_volume"]: .2f}
                            HIGHEST VOLUME: {volume_data["highest_volume"]}
                            LOWEST VOLUME: {volume_data["lowest_volume"]} \n""")

                
            elif response == 6:
                print("Program successfully terminated.")
                break
            else:
                print("Enter a valid number")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

    




    


