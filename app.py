"""
Climate Data Story — Interactive Dashboard
A data storytelling dashboard built with Streamlit.

Structure follows the Hook → Evidence → Meaning narrative framework
from Part 1 of the tutorial.

Run locally:  streamlit run app.py
"""

import streamlit as st
import pandas as pd
import altair as alt

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Page Config
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.set_page_config(
    page_title="Climate Data Story",
    page_icon="🌍",
    layout="wide"
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Data Layer (cached)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@st.cache_data
def load_data():
    """Load and clean the Berkeley Earth dataset (runs only once)."""
    df = pd.read_csv("data/ddbb_surface_temperature_countries.csv")
    df = df.dropna(subset=["Anomaly"])
    return df


@st.cache_data
def get_annual_data(df, country):
    """Aggregate monthly records into annual averages for a country."""
    country_data = df[df["Country"] == country]
    annual = country_data.groupby("Years").agg({
        "Anomaly": "mean",
        "Temperature": "mean"
    }).reset_index()
    annual.columns = ["Year", "Anomaly", "Temperature"]
    return annual


@st.cache_data
def get_decade_data(annual_df):
    """Calculate decade averages from annual data."""
    df = annual_df.copy()
    df["Decade"] = (df["Year"] // 10) * 10
    return df.groupby("Decade")["Anomaly"].mean().reset_index()


df = load_data()
countries = sorted(df["Country"].unique())

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Sidebar Controls
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.sidebar.title("🌍 Climate Explorer")
st.sidebar.markdown("Explore temperature trends by country and time period.")

selected_country = st.sidebar.selectbox(
    "Select Country",
    countries,
    index=countries.index("South Korea") if "South Korea" in countries else 0
)

year_range = st.sidebar.slider(
    "Year Range",
    min_value=1900,
    max_value=2020,
    value=(1900, 2020)
)

st.sidebar.markdown("---")
st.sidebar.subheader("Chart Options")
show_trend = st.sidebar.checkbox("Show Trend Line", value=True)
show_ma = st.sidebar.checkbox("Show Moving Average", value=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Prepare Data
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
annual = get_annual_data(df, selected_country)
annual_filtered = annual[
    (annual["Year"] >= year_range[0]) &
    (annual["Year"] <= year_range[1])
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HOOK — Key Metrics
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.title(f"Climate Story: {selected_country}")

col1, col2, col3, col4 = st.columns(4)

latest = annual_filtered.iloc[-1]
avg_anomaly = annual_filtered["Anomaly"].mean()
hottest = annual_filtered.loc[annual_filtered["Anomaly"].idxmax()]
coldest = annual_filtered.loc[annual_filtered["Anomaly"].idxmin()]

with col1:
    st.metric("Latest Anomaly", f"{latest['Anomaly']:.2f}°C")
with col2:
    st.metric("Period Average", f"{avg_anomaly:.2f}°C")
with col3:
    st.metric(f"Hottest ({int(hottest['Year'])})", f"{hottest['Anomaly']:.2f}°C")
with col4:
    st.metric(f"Coldest ({int(coldest['Year'])})", f"{coldest['Anomaly']:.2f}°C")

st.markdown("---")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EVIDENCE — Tabbed Charts
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
tab1, tab2, tab3 = st.tabs(["📈 Time Series", "🌡️ Warming Stripes", "📊 Decades"])

# ── Tab 1: Time Series ──
with tab1:
    plot_data = annual_filtered.copy()
    plot_data["MA_10"] = plot_data["Anomaly"].rolling(10, center=True).mean()

    base = alt.Chart(plot_data).encode(x=alt.X("Year:Q", title="Year"))

    # Data points
    points = base.mark_circle(size=40, opacity=0.6, color="steelblue").encode(
        y=alt.Y("Anomaly:Q", title="Temperature Anomaly (°C)"),
        tooltip=["Year:Q", alt.Tooltip("Anomaly:Q", format=".2f")]
    )
    layers = [points]

    # Optional: Moving average (red line)
    if show_ma:
        ma = base.mark_line(color="#e74c3c", strokeWidth=2.5).encode(y="MA_10:Q")
        layers.append(ma)

    # Optional: Trend line (green dashed)
    if show_trend:
        trend = base.transform_regression("Year", "Anomaly").mark_line(
            color="#27ae60", strokeDash=[5, 5], strokeWidth=2
        ).encode(y="Anomaly:Q")
        layers.append(trend)

    # Reference: baseline at 0°C
    baseline = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(
        color="gray", strokeDash=[3, 3]
    ).encode(y="y:Q")
    layers.append(baseline)

    # Reference: Paris Agreement 1.5°C target
    paris = alt.Chart(pd.DataFrame({"y": [1.5]})).mark_rule(
        color="red", strokeWidth=2
    ).encode(y="y:Q")
    layers.append(paris)

    chart = alt.layer(*layers).properties(height=450).interactive()
    st.altair_chart(chart, use_container_width=True)
    st.caption("Gray dashed line = baseline (0°C anomaly). Red line = Paris Agreement 1.5°C target.")

# ── Tab 2: Warming Stripes ──
with tab2:
    stripes = alt.Chart(annual_filtered).mark_rect().encode(
        x=alt.X("Year:O", axis=alt.Axis(labels=False, ticks=False, title=None)),
        color=alt.Color(
            "Anomaly:Q",
            scale=alt.Scale(scheme="redblue", reverse=True, domain=[-2, 2]),
            legend=alt.Legend(title="Anomaly (°C)", orient="bottom")
        ),
        tooltip=["Year:O", alt.Tooltip("Anomaly:Q", format=".2f")]
    ).properties(
        height=180,
        title=f"Warming Stripes: {selected_country}"
    )
    st.altair_chart(stripes, use_container_width=True)
    st.caption("Each vertical stripe = one year. Blue → Red = cooler → warmer than baseline.")

# ── Tab 3: Decade Comparison ──
with tab3:
    decade_avg = get_decade_data(annual_filtered)

    bars = alt.Chart(decade_avg).mark_bar().encode(
        x=alt.X("Decade:O", title="Decade"),
        y=alt.Y("Anomaly:Q", title="Average Anomaly (°C)"),
        color=alt.condition(
            alt.datum.Anomaly > 0,
            alt.value("#e74c3c"),
            alt.value("#3498db")
        ),
        tooltip=["Decade:O", alt.Tooltip("Anomaly:Q", format=".3f")]
    ).properties(height=400)

    st.altair_chart(bars, use_container_width=True)
    st.caption("Red = warmer than baseline. Blue = cooler than baseline.")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MEANING — Auto-Generated Narrative
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown("---")
st.header("📖 Data Story")

mid = (year_range[0] + year_range[1]) // 2
early_avg = annual_filtered[annual_filtered["Year"] < mid]["Anomaly"].mean()
recent_avg = annual_filtered[annual_filtered["Year"] >= mid]["Anomaly"].mean()
change = recent_avg - early_avg

trend_text = (
    "The warming trend is accelerating — recent decades are markedly warmer than earlier ones."
    if change > 0
    else "The data shows a complex pattern that warrants closer regional analysis."
)

st.markdown(f"""
### Climate Summary: {selected_country}

**Hook**: In **{int(latest['Year'])}**, {selected_country}'s temperature anomaly reached
**{latest['Anomaly']:.2f}°C** above the historical baseline.

**Evidence**: Over {year_range[0]}–{year_range[1]}, the average anomaly was **{avg_anomaly:.2f}°C**.
The hottest year on record was **{int(hottest['Year'])}** at **{hottest['Anomaly']:.2f}°C**.
Comparing the first half ({year_range[0]}–{mid}) to the second half ({mid}–{year_range[1]}),
the average anomaly shifted by **{change:+.2f}°C**.

**Meaning**: {trend_text}
""")

# ── Paris Agreement Tracker ──
st.subheader("Paris Agreement Tracker")

progress_val = min(latest["Anomaly"] / 1.5, 1.0)
col_a, col_b = st.columns([3, 1])
with col_a:
    st.progress(max(0.0, progress_val))
with col_b:
    st.write(f"**{progress_val * 100:.0f}%** of 1.5°C")

if latest["Anomaly"] >= 1.5:
    st.error("⚠️ This country has exceeded the 1.5°C threshold.")
else:
    remaining = 1.5 - latest["Anomaly"]
    st.success(f"✅ {remaining:.2f}°C remaining before 1.5°C threshold")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ACTION — Download
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown("---")

csv = annual_filtered.to_csv(index=False)
st.download_button(
    label="📥 Download Filtered Data (CSV)",
    data=csv,
    file_name=f"{selected_country.replace(' ', '_')}_climate_{year_range[0]}_{year_range[1]}.csv",
    mime="text/csv"
)

st.caption("Data: Berkeley Earth Surface Temperature Study | Built with Streamlit")
