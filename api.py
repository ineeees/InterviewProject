from flask import Flask, request, jsonify
import yfinance as yf
from flask_caching import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'SimpleCache'
cache = Cache(app)

@app.route('/api/stats', methods=['GET'])
@cache.cached(timeout=60)  
def get_stock_stats():
    ticker = request.args.get('ticker')
    start_date = request.args.get('start', '2020-01-01')
    end_date = request.args.get('end', '2023-01-01')
    
    if not ticker:
        return jsonify({'error': 'Ticker is required'}), 400

    stock_data = yf.download(ticker, start=start_date, end=end_date)

    if stock_data.empty:
        return jsonify({'error': 'No data found for the given ticker and date range'}), 404

   
    stats = {
        'ticker': ticker,
        'start_date': start_date,
        'end_date': end_date,
        'high': float(stock_data['High'].max()), 
        'low': float(stock_data['Low'].min()),   
        'average': float(stock_data['Close'].mean()),  
        'last_close': float(stock_data['Close'].iloc[-1])
    }

    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
