#SYSTEM MENU


while True:
    print("""
1. Analyse a stock
2. Compare stocks
3. View highest-performing stock
4. View lowest-performing stock
5. View trading-volume summary
6. Exit""" )
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
                        pass
                    elif response == 2:
                        #Call the functions to analyse ALPHA stocks
                        pass
                    elif response == 3:
                        #Call the functions to analyse GAMMA stocks
                        pass
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
            pass

        elif response == 4:
            #Write the code to view lowest-performing stock
            pass
        elif response == 5:
            #Write the code to view trading-volume summary
            pass
        elif response == 6:
            print("Program successfully terminated.")
            break
        else:
            print("Enter a valid number")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue



