import yfinance as yf
import plotly.graph_objects as go

# 시가총액 상위 10개 기업의 티커 목록
tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA', 'BRK-B', 'NVDA', 'V', 'META', 'TSM']

# 각 기업의 주식 데이터 다운로드
data = {ticker: yf.download(ticker, start="2020-01-01", end="2025-01-01") for ticker in tickers}

# Plotly를 사용하여 시각화
fig = go.Figure()

for ticker in tickers:
    fig.add_trace(go.Scatter(x=data[ticker].index,
                             y=data[ticker]['Adj Close'],
                             mode='lines',
                             name=ticker))

fig.update_layout(
    title='Global Top 10 Market Cap Companies Stock Prices (2020–2025)',
    xaxis_title='Date',
    yaxis_title='Adjusted Close Price (USD)',
    template='plotly_dark'
)

fig.show()
