stocks = [

    {
        "name": "Company A",
        "symbol": "CMPA",
        "sector": "Technology",
        "current_price": 100.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 98.0,
                    "close": 100.0,
                    "high": 101.0,
                    "low": 97.0
                },
                "volume": 12000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 97.0,
                    "close": 98.0,
                    "high": 99.0,
                    "low": 96.0
                },
                "volume": 15000
            }
        ],
        "locations": ["New York", "London"]
    },

    {
        "name": "Company B",
        "symbol": "CMPB",
        "sector": "Finance",
        "current_price": 200.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 198.0,
                    "close": 200.0,
                    "high": 202.0,
                    "low": 196.0
                },
                "volume": 18000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 196.0,
                    "close": 198.0,
                    "high": 199.0,
                    "low": 195.0
                },
                "volume": 17000
            }
        ],
        "locations": ["Tokyo", "Singapore"]
    },

    {
        "name": "Company C",
        "symbol": "CMPC",
        "sector": "Healthcare",
        "current_price": 300.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 295.0,
                    "close": 300.0,
                    "high": 302.0,
                    "low": 294.0
                },
                "volume": 22000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 294.0,
                    "close": 295.0,
                    "high": 296.0,
                    "low": 293.0
                },
                "volume": 21000
            }
        ],
        "locations": ["Berlin", "Paris"]
    }

]

n=    {
        "name": "Company D",
        "symbol": "HDFC",
        "sector": "BANK",
        "current_price": 500,

        "locations": ["odisha", "sudan"]
    }



# print(stocks)
# print(type(stocks))
# print(len(stocks))

# print(stocks[1].get('current_price'))

# stocks.append(n)
# print(stocks)

stocks[0].get('historical_data').pop(1)
print(stocks)