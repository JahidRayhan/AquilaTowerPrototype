from prophet import Prophet
import pandas as pd, numpy as np, json, datetime

# mock data
dates = pd.date_range(start="2025-10-01", end="2025-11-07")
sales = np.random.randint(80, 200, len(dates))
df = pd.DataFrame({"ds": dates, "y": sales})

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)[["ds", "yhat"]].tail(7)

result = [
    {"product_id": "P101",
     "date": str(row.ds.date()),
     "predicted_demand": int(row.yhat)}
    for _, row in forecast.iterrows()
]

json.dump(result, open("forecast_data.json", "w"), indent=2)
print("✅ Forecast generated successfully!")
