python
import pandas as pd
import plotly.express as px
from flask import Flask, render_template

# Load the dataset
data = pd.read_excel('Daily Bulletins March 31.xlsx')

# Data cleaning and transformation
data['Percentage Change'] = data['Percentage Change'].str.rstrip('%').astype('float') / 100.0

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    # Summary for Market Overview Panel
    total_market_cap = data['Market Capitalization'].sum()
    total_trades = data['Trades'].sum()
    total_volume = data['Volume'].sum()
    total_trading_value = data['Trading Value'].sum()

    # Generate visualizations
    market_cap_fig = px.pie(data, values='Market Capitalization', names='Market', title='Market Capitalization Distribution')
    trade_volume_fig = px.bar(data, x='Company', y='Volume', title='Trading Volume by Company')

    return render_template('index.html', 
                           total_market_cap=total_market_cap, 
                           total_trades=total_trades, 
                           total_volume=total_volume, 
                           total_trading_value=total_trading_value,
                           market_cap_fig=market_cap_fig.to_html(full_html=False), 
                           trade_volume_fig=trade_volume_fig.to_html(full_html=False))

if __name__ == '__main__':
    app.run(debug=True)
