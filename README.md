# 📦 SupplyNext Nexus
### AI-Powered Central Control Tower for Smart Supply Chains

---

## 🚀 Overview
**SupplyNext Nexus** is an intelligent control platform integrating IoT, ERP, and AI analytics for real-time supply chain visibility.  
It collects live factory data, forecasts product demand, and alerts managers before stock shortages occur.

---

## 🧠 Key Features
- 🌐 **IoT Integration:** Simulated live factory data (stock, temperature)
- ⚙️ **FastAPI Backend:** Receives and stores IoT data in SQLite
- 🤖 **AI Engine (Prophet):** Predicts next 7 days of product demand
- 📊 **Dashboard (Streamlit):** Displays live IoT feed, AI forecast, and alerts
- 🎙️ **Voice Command Support:** Simple voice input for demo interaction
- 💻 **Auto-Refresh & Branding:** Smooth 3s updates with your team logo and color theme

---

## 🧩 Project Structure
SupplyNext-Nexus/
├── backend/ # FastAPI backend server
│ ├── app.py
│ └── supplynext.db
├── iot_simulator/ # Simulated IoT devices
│ ├── iot_simulator.py
│ └── voice_input.py
├── ai_engine/ # AI forecasting module
│ ├── ai_engine.py
│ └── forecast_data.json
├── dashboard/ # Visualization dashboard
│ ├── dashboard_app.py
│ ├── team_logo.png
│ └── style.css
└── README.md
└── requirements.txt