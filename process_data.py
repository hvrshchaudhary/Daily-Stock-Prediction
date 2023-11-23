import pandas as pd

def process_data(json_data):
    data = json_data['Time Series (Daily)']
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index = pd.to_datetime(df.index)
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": int})
    return df
