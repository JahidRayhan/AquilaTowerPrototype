import streamlit as st
import pandas as pd, sqlite3, time, numpy as np, plotly.express as px
from datetime import datetime
st.set_page_config(page_title="Aquila Tower", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header & Branding
st.image("team_logo.png", width=100)
st.title("📦 Aquila Tower – AI-Powered Supply Chain Control Tower")
st.caption("Developed by Team Nexus Innovators")

# Real-time refresh loop
placeholder = st.empty()
for _ in range(120):  # 6 minutes of updates
    with placeholder.container():
        con = sqlite3.connect("../backend/supplynext.db")
        df = pd.read_sql("SELECT * FROM iot_data ORDER BY timestamp DESC LIMIT 10", con)
        con.close()

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Live IoT Data Feed")
            st.dataframe(df)
            low = df[df["stock_level"] < 50]
            if not low.empty:
                st.error(f"⚠️ Low stock alert for: {', '.join(low['product_id'])}")

        with col2:
            st.subheader("🤖 AI Forecast (Next 7 Days)")
            try:
                fc = pd.read_json("../ai_engine/forecast_data.json")
            except:
                fc = pd.DataFrame({
                    "date": pd.date_range(datetime.now(), periods=7),
                    "predicted_demand": np.random.randint(120, 240, 7)
                })
            fig = px.line(fc, x="date", y="predicted_demand", markers=True)
            st.plotly_chart(fig, use_container_width=True)

        st.caption("🔄 Auto-refreshing every 3 seconds...")
        time.sleep(3)
