import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the list of stocks to collect data for
# BEGIN: 8j7f6h3d4k5s

stocks = ['AAPL'] # Insert list of symbols to analyze



# END: 8j7f6h3d4k5s

# Create an empty dataframe to store the data
stock_data = pd.DataFrame(columns=['Stock', 'Price', 'Momentum','PE Ratio'])

# Loop through each stock and collect the data
for stock in stocks:
   
    #Collect data using yfinance
    stock_price = yf.Ticker(stock).history(period="1d")["Close"][0]
    historical_data = yf.Ticker(stock).history(period="1mo")
    start_price = historical_data["Close"][0]
    end_price = historical_data["Close"][-1]
    momentum = end_price - start_price
    # momentum = stock_info['momentum']
    # market_cap = (stock_info['marketCap'])/1000000000
    
    # pe_ratio = stock_info["trailingPE"]
    current_price = stock.history(period="1d")["Close"][0]
    # Estimate the EPS using historical data (e.g., last 4 quarters)
    historical_data = stock.history(period="1y")
    average_earnings = historical_data["Close"].mean()
    # Calculate the P/E ratio
    pe_ratio = current_price / average_earnings
    

    

    # Add the data to the dataframe
    
    stock_data = stock_data.append({'Stock': stock, 'Price': stock_price,  'Momentum': momentum, 'PE Ratio': pe_ratio}, ignore_index=True)
# 'PE Ratio': pe_ratio
# 'Market Cap (Billions)': market_cap
       
# Export the data to an excel sheet
stock_data.to_excel('gitstockdata.xlsx', index=False)

#GRAPHING

# Generate a graph of the stock price over 5 months for each stock
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

# from alpha_vantage.timeseries import TimeSeries
# from alpha_vantage.fundamentaldata import FundamentalData
# import pandas as pd
# # Replace with your Alpha Vantage API key
# api_key = '0M44PX1Q9E2MYH14'
# stock_data = pd.DataFrame(columns=['Stock', 'Price', 'PE Ratio', 'Momentum', 'Market Cap'])
# # Define the stock symbol
# stocks= ['GOOGL']  # Replace with the symbol of the stock you want to analyze

# # Initialize the Alpha Vantage TimeSeries and FundamentalData objects
# ts = TimeSeries(key=api_key, output_format='pandas')
# fd = FundamentalData(key=api_key, output_format='pandas')


# # Get real-time stock price
# for stock in stocks:
#     price_data, _ = ts.get_quote_endpoint(symbol=stock)
#     current_price = price_data['05. price'].values[0]

#     # Get historical data for the past month to calculate momentum
#     historical_data, _ = ts.get_monthly(symbol=stock)
#     start_price = historical_data.iloc[-2]['4. close']
#     end_price = historical_data.iloc[-1]['4. close']
#     momentum = end_price - start_price

#     # Retrieve P/E ratio and market cap using an alternative source
#     overview_data, _ = fd.get_company_overview(symbol=stock)
#     pe_ratio = overview_data['PERatio'].values[0]
#     market_cap = (overview_data['MarketCapitalization'].values[0])/1000000000

#     stock_data = stock_data.append({'Stock': stock, 'Price': current_price, 'PE Ratio': pe_ratio, 'Momentum': momentum,  "Market Cap": market_cap}, ignore_index=True)

#     # print(f"Stock Symbol: {stock}")
#     # print(f"Current Price: {current_price}")
#     # print(f"Momentum (1 month): {momentum}")
#     # print(f"P/E Ratio: {pe_ratio}")
#     # print(f"Market Cap: {market_cap}")

# # Note: Be sure to replace 'YOUR_API_KEY' with your actual Alpha Vantage API key.
# stock_data.to_excel('gitstockdata.xlsx', index=False)