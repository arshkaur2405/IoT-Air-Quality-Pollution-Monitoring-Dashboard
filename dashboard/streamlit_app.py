import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from streamlit_autorefresh import st_autorefresh

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Smart City Air Quality Command Center",
    page_icon="🌍",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="refresh"
)

# ==================================
# HEADER
# ==================================

st.markdown("""
# 🌍 Smart City Air Quality Command Center

### Industry-Oriented IoT Environmental Monitoring Platform
""")

st.markdown("---")

# ==================================
# LOAD DATA
# ==================================

try:

    df = pd.read_csv(
        "data/air_quality_log.csv"
    )

except:

    st.error(
        "No sensor data found. Run main.py first."
    )

    st.stop()

# ==================================
# LATEST RECORD
# ==================================

latest = df.iloc[-1]

aqi = latest["aqi"]
temp = latest["temperature"]
humidity = latest["humidity"]
gas = latest["gas_level"]
status = latest["status"]
alert = latest["alert"]

# ==================================
# STATUS COLOR
# ==================================

if status == "GOOD":

    status_color = "green"

elif status == "MODERATE":

    status_color = "orange"

elif status == "POOR":

    status_color = "red"

else:

    status_color = "darkred"

# ==================================
# KPI CARDS
# ==================================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🌫 AQI", aqi)

with col2:
    st.metric("🌡 Temperature", f"{temp} °C")

with col3:
    st.metric("💧 Humidity", f"{humidity}%")

with col4:
    st.metric("🧪 Gas Level", gas)

with col5:
    st.metric("🚨 Alert", alert)

st.markdown("---")

# ==================================
# STATUS BANNER
# ==================================

st.markdown(
    f"""
    <h2 style='color:{status_color};'>
    Current Status : {status}
    </h2>
    """,
    unsafe_allow_html=True
)

# ==================================
# AQI GAUGE
# ==================================

gauge = go.Figure(
    go.Indicator(
        mode="gauge+number",

        value=aqi,

        title={
            "text":
            "Air Quality Index"
        },

        gauge={
            "axis": {
                "range":
                [0, 500]
            },

            "steps": [

                {
                    "range":[0,100],
                    "color":"lightgreen"
                },

                {
                    "range":[100,200],
                    "color":"yellow"
                },

                {
                    "range":[200,300],
                    "color":"orange"
                },

                {
                    "range":[300,500],
                    "color":"red"
                }
            ]
        }
    )
)

st.plotly_chart(
    gauge,
    use_container_width=True
)

# ==================================
# CHARTS
# ==================================

st.subheader(
    "📈 Environmental Trends"
)

left, right = st.columns(2)

with left:

    fig_aqi = px.line(
        df,
        y="aqi",
        title="AQI Trend"
    )

    st.plotly_chart(
        fig_aqi,
        use_container_width=True
    )

with right:

    fig_temp = px.line(
        df,
        y="temperature",
        title="Temperature Trend"
    )

    st.plotly_chart(
        fig_temp,
        use_container_width=True
    )

left2, right2 = st.columns(2)

with left2:

    fig_humidity = px.line(
        df,
        y="humidity",
        title="Humidity Trend"
    )

    st.plotly_chart(
        fig_humidity,
        use_container_width=True
    )

with right2:

    fig_gas = px.line(
        df,
        y="gas_level",
        title="Gas Level Trend"
    )

    st.plotly_chart(
        fig_gas,
        use_container_width=True
    )

st.markdown("---")

# ==================================
# POLLUTION DISTRIBUTION
# ==================================

st.subheader(
    "📊 Pollution Distribution"
)

status_count = (
    df["status"]
    .value_counts()
    .reset_index()
)

status_count.columns = [
    "Status",
    "Count"
]

pie = px.pie(
    status_count,
    names="Status",
    values="Count"
)

st.plotly_chart(
    pie,
    use_container_width=True
)

# ==================================
# HISTOGRAM
# ==================================

st.subheader(
    "📉 AQI Frequency Distribution"
)

hist = px.histogram(
    df,
    x="aqi",
    nbins=20
)

st.plotly_chart(
    hist,
    use_container_width=True
)

# ==================================
# ANALYTICS
# ==================================

st.subheader(
    "📋 Analytics Summary"
)

a1, a2, a3, a4 = st.columns(4)

with a1:

    st.info(
        f"Average AQI : {round(df['aqi'].mean(),2)}"
    )

with a2:

    st.success(
        f"Minimum AQI : {df['aqi'].min()}"
    )

with a3:

    st.warning(
        f"Maximum AQI : {df['aqi'].max()}"
    )

with a4:

    st.error(
        f"Records : {len(df)}"
    )

# ==================================
# HEALTH RECOMMENDATIONS
# ==================================

st.subheader(
    "🏥 Health Advisory"
)

if status == "GOOD":

    st.success(
        "Air quality is safe."
    )

elif status == "MODERATE":

    st.warning(
        "Sensitive individuals should limit prolonged outdoor exposure."
    )

elif status == "POOR":

    st.warning(
        "Reduce outdoor activities and consider wearing masks."
    )

else:

    st.error(
        "Stay indoors. Avoid outdoor exposure."
    )

# ==================================
# DATA TABLE
# ==================================

st.subheader(
    "📂 Latest Records"
)

st.dataframe(
    df.tail(25),
    use_container_width=True
)

# ==================================
# DOWNLOAD
# ==================================

csv = df.to_csv(
    index=False
)

st.download_button(
    "⬇ Download CSV",
    csv,
    "air_quality_log.csv",
    "text/csv"
)

# ==================================
# SYSTEM HEALTH
# ==================================

st.markdown("---")

st.subheader(
    "⚙ System Health"
)

s1, s2, s3 = st.columns(3)

with s1:
    st.success("Sensor Engine Online")

with s2:
    st.success("Data Logger Active")

with s3:
    st.success("Dashboard Running")

# ==================================
# FOOTER
# ==================================

st.markdown("---")

st.caption(
    "Smart City Air Quality Command Center | IoT Course Project"
)
# ...