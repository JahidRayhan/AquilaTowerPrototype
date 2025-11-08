````markdown
# ⚙️ Setup Instructions — Aquila Tower  
*AI-Powered Central Control Tower for Smart Supply Chains*  

---

## 🧩 Prerequisites
- **Python 3.10 or later** (Prophet works best ≤ 3.11)  
- **Git** installed on your system  
- Basic familiarity with terminal / command prompt  

---

## 🪴 1️⃣ Clone the Repository
```bash
git clone https://github.com/JahidRayhan/AquilaTower.git
cd AquilaTower
````

---

## 🧱 2️⃣ Create & Activate a Virtual Environment

```bash
python -m venv venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

---

## 📦 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you plan to use the **voice-input feature**, ensure PortAudio is installed:

```bash
# Linux
sudo apt install portaudio19-dev
# macOS (Homebrew)
brew install portaudio
```

---

## 🚀 4️⃣ Start the Backend (FastAPI + SQLite)

```bash
cd backend
uvicorn app:app --reload
```

* Visit **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** → interactive API page
* A file named `supplynext.db` will be created automatically

---

## 🔄 5️⃣ Run the IoT Data Simulator

Open a **new terminal** (keep backend running):

```bash
cd iot_sim
python iot_simulator.py
```

This script sends live random factory data to the backend every 5 seconds.

---

## 🤖 6️⃣ Generate AI Forecast (Prophet or Fallback)

Open another terminal:

```bash
cd ai_eng
python ai_engine.py
```

This creates `forecast_data.json` — the AI’s 7-day demand prediction file.

---

## 🖥️ 7️⃣ Launch the Dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

Dashboard opens at: **[http://localhost:8501](http://localhost:8501)**
Displays:

* 📊 *Live IoT Feed* (stock + temperature)
* 📈 *AI Forecast* (next 7 days)
* ⚠️ *Low Stock Alerts*

---

## 🎙️ 8️⃣ Optional: Try Voice Commands

```bash
cd iot_sim
python voice_input.py
```

Say commands like **“check stock”** or **“show forecast”**.
*(Requires microphone access)*

---

## ✅ 9️⃣ Complete End-to-End Flow

1. IoT Simulator → sends data to Backend
2. Backend → stores data in SQLite
3. AI Engine → generates forecast
4. Dashboard → visualizes data & alerts
