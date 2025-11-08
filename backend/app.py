from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

app = FastAPI()
engine = create_engine("sqlite:///supplynext.db", echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class IoTData(Base):
    __tablename__ = "iot_data"
    id = Column(Integer, primary_key=True)
    product_id = Column(String)
    stock_level = Column(Integer)
    temperature = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)

class IoTInput(BaseModel):
    product_id: str
    stock_level: int
    temperature: float
    timestamp: str

from datetime import datetime

@app.post("/receive_data")
def receive_data(data: IoTInput):
    db = SessionLocal()
    # convert timestamp string to datetime object
    record = IoTData(
        product_id=data.product_id,
        stock_level=data.stock_level,
        temperature=data.temperature,
        timestamp=datetime.fromisoformat(data.timestamp)
    )
    db.add(record)
    db.commit()
    db.close()
    return {"status": "received"}


class ForecastItem(BaseModel):
    product_id: str
    date: str
    predicted_demand: int

@app.post("/forecast_update")
def forecast_update(items: List[ForecastItem]):
    print(f"Received {len(items)} forecast entries")
    return {"status": "forecast received"}

@app.get("/")
def home():
    return {"message": "Aquila Tower Backend is running 🚀"}

