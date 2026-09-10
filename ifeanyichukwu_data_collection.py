# ==== PERSON 2: Data entry and validation ====

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
            if records["close"] <0:
                issues.append(f"{stock_name}{records["date"]} : close price not positive")

            if records["high"] <= records["low"]:
                issues.append(f"{stock_name}{records["date"]} : high is less than low")

            if records["high"] <= records["open"]:
                issues.append(f"{stock_name}{records["date"]} : high is less than open")

            if records["high"] <= records["close"]:
                issues.append(f"{stock_name}{records["date"]} : high is less than close")

            if records["low"] >= records["open"]:
                issues.append(f"{stock_name}{records["date"]} : low is greater than open")

            if records["low"] >= records["close"]:
                issues.append(f"{stock_name}{records["date"]} : low is greater than close")

            if records["volume"] <= 0:
                issues.append(f"{stock_name}{records["date"]} : volume is zero or negative")

        return issues

        
        

    


    