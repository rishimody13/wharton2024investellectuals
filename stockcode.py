import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si
import time
# Define the list of stocks to collect data for

#stocks = ['VUG', 'VOO', 'VGT']

stocks = ['AAPL', 'TSLA', 'MSFT', 'GOOGL','NVDA', 'META', 'NFLX', 'INTC', 'AMZN', 'ORCL'] # Insert list of symbols to analyze





# Create an empty dataframe to store the data
stock_data = pd.DataFrame(columns=['Stock', 'Price', 'Momentum','PE Ratio'])

# Loop through each stock and collect the data
for stock in stocks:
    
    #Collect data using yfinance
    stock_price = yf.Ticker(stock).history(period="1d")["Close"][0]
    historical_data = yf.Ticker(stock).history(period="1y")
    start_price = historical_data["Close"][0]
    end_price = historical_data["Close"][-1]
    momentum = end_price - start_price

    # MCAP -> market_cap = (stock_info['marketCap'])/1000000000
    
    #FIRST ALTERNATIVE FOR PE
    quote = si.get_quote_table(stock)
    
    pe_ratio = quote["PE Ratio (TTM)"]
    
    #OTHER ALTERNTIVE FOR PE
    # attempt = 1
    # time.sleep(3)
    # error = False
    # try:
    #     val = si.get_stats_valuation(stock)
    #     print(f"{stock} loaded on first attempt")
    # except:
    #     error = True
    #     attempt += 1
    #     while error == True:
    #         print(f"Sleeping {attempt*10}s")
    #         time.sleep(attempt*10)
    #         try:
    #             x = si.get_stats_valuation(stock)
    #             error = False
    #             print(f"{stock}, succesful on attempt {attempt}")
    #         except:
    #             attempt += 1
    #             print(f"{stock}, failed. Attempt {attempt}") 
    # # val = si.get_stats_valuation(stock)
    # val = val.iloc[:,:2]
    # val.columns = ["Attribute", "Recent"]
    # pe_ratio = float(val[val.Attribute.str.contains("Trailing P/E")].iloc[0,1])
     

    # Add the data to the dataframe
    
    stock_data = stock_data.append({'Stock': stock, 'Price': stock_price,  'Momentum': momentum, 'PE Ratio': pe_ratio}, ignore_index=True)

       
# Export the data to an excel sheet
stock_data.to_excel('stockdata.xlsx', index=False)

#GRAPHING

# Generate a graph of the stock price over 5 months for each stock
def fivemonthpricechange():
    for stock in stocks:
        # Collect the data using yfinance
        stock_df = yf.download(stock, period='5mo', interval='1d')
        
        # Plot the data
        plt.plot(stock_df['Close'], label=stock)
        
    # Add labels and legend to the graph
    plt.title('Stock Price over 5 Months')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

    # Show the graph
    plt.show()


#generate graphs for percentage change
def sixmonthpercentagechange():
    for stock in stocks:
        # Collect the data using yfinance
        stock_df = yf.download(stock, period='6mo', interval='1d')
        
        # Calculate the percentage change
        stock_df['Percentage Change'] = (stock_df['Close'] - stock_df['Close'].iloc[0]) / stock_df['Close'].iloc[0] * 100
        
        # Plot the percentage change
        plt.plot(stock_df.index, stock_df['Percentage Change'], label=stock)

    # Add labels and legend to the graph
    plt.title('Percentage Price Change Over 6 months')
    plt.xlabel('Date')
    plt.ylabel('Percentage Change')
    plt.legend()

    # Show the graph
    plt.show()

fivemonthpricechange()
