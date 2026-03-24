
# ─────────────────────────────────────────────────────────
# WaterWatch 
# ─────────────────────────────────────────────────────────

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ─── PAGE CONFIG ─────────────────────────────────────────
st.set_page_config(
    page_title="WaterWatch Nagpur",
    page_icon="🚰",
    layout="wide"
)

# ─── CUSTOM CSS (Professional Styling) ───────────────────
st.markdown("""
<style>
.metric-card {
    background-color: #f0f8ff;
    padding: 15px;
    border-radius: 10px;
}
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

# ─── HEADER ─────────────────────────────────────────────
st.markdown("""
<h1 style='text-align:center;color:#1a6ebd;'>🚰 WaterWatch — Nagpur NMC</h1>
<h4 style='text-align:center;color:gray;'>AI-Powered Ward-Level Water Scarcity Forecasting</h4>
<hr>
""", unsafe_allow_html=True)

# ─── LOAD DATA ──────────────────────────────────────────
@st.cache_data
def load_data():
    risk = pd.read_csv("ward_risk_predictions.csv")
    importance = pd.read_csv("feature_importance.csv")
    return risk, importance

risk_df, importance_df = load_data()

# ─── SIDEBAR FILTERS ─────────────────────────────────────
st.sidebar.title("🎛️ Controls")

zones = st.sidebar.multiselect(
    "Select Zone",
    sorted(risk_df["zone"].unique()),
    default=risk_df["zone"].unique()
)

risk_levels = st.sidebar.multiselect(
    "Select Risk Level",
    ["🔴 High", "🟡 Medium", "🟢 Low"],
    default=["🔴 High", "🟡 Medium", "🟢 Low"]
)

filtered_df = risk_df[
    (risk_df["zone"].isin(zones)) &
    (risk_df["risk_level"].isin(risk_levels))
]

st.sidebar.markdown("---")

# ─── KPI METRICS ────────────────────────────────────────
st.subheader("📊 Nagpur Overview")

total = len(filtered_df)
high = len(filtered_df[filtered_df["risk_level"] == "🔴 High"])
medium = len(filtered_df[filtered_df["risk_level"] == "🟡 Medium"])
low = len(filtered_df[filtered_df["risk_level"] == "🟢 Low"])
tankers = int(filtered_df["tankers_needed"].sum())

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Wards", total)
c2.metric("🔴 High Risk", high)
c3.metric("🟡 Medium Risk", medium)
c4.metric("🟢 Low Risk", low)
c5.metric("🚛 Tankers", tankers)

# ─── ALERT ──────────────────────────────────────────────
if high > 0:
    st.error(f"⚠️ {high} wards predicted HIGH water scarcity risk")

# ─── TABS ───────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "🗺️ Risk Map",
    "📊 Analytics",
    "🚛 Tanker Planning",
    "📋 Data Table"
])

# ─── TAB 1 : RISK HEATMAP ───────────────────────────────
with tab1:
    st.subheader("Ward Risk Score")

    fig = px.bar(
        filtered_df.sort_values("risk_score", ascending=False),
        x="ward_name",
        y="risk_score",
        color="risk_level",
        color_discrete_map={
            "🔴 High": "red",
            "🟡 Medium": "orange",
            "🟢 Low": "green"
        },
        text="risk_score"
    )
    fig.update_layout(height=450, xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)

# ─── TAB 2 : ANALYTICS ──────────────────────────────────
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Root Cause Indicators")

        fig2 = px.bar(
            importance_df,
            x="importance",
            y="feature",
            orientation="h",
            color="importance",
            color_continuous_scale="Reds"
        )
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        st.subheader("Zone Risk Comparison")

        zone_summary = filtered_df.groupby("zone").agg(
            avg_risk=("risk_score", "mean")
        ).reset_index()

        fig3 = px.bar(
            zone_summary,
            x="zone",
            y="avg_risk",
            color="avg_risk",
            color_continuous_scale="RdYlGn_r",
            text="avg_risk"
        )
        st.plotly_chart(fig3, use_container_width=True)

# ─── TAB 3 : TANKER ─────────────────────────────────────
with tab3:
    st.subheader("Tanker Allocation")

    fig4 = px.bar(
        filtered_df.sort_values("tankers_needed", ascending=False),
        x="ward_name",
        y="tankers_needed",
        color="risk_level",
        text="tankers_needed",
        color_discrete_map={
            "🔴 High": "red",
            "🟡 Medium": "orange",
            "🟢 Low": "green"
        }
    )

    st.plotly_chart(fig4, use_container_width=True)

# ─── TAB 4 : TABLE ──────────────────────────────────────
with tab4:
    st.subheader("Detailed Ward Data")

    st.dataframe(
        filtered_df.sort_values("risk_score", ascending=False),
        use_container_width=True
    )

    st.download_button(
        "📥 Download CSV",
        filtered_df.to_csv(index=False),
        file_name="waterwatch_predictions.csv",
        mime="text/csv"
    )

# ─── FOOTER ─────────────────────────────────────────────
st.markdown("""
<hr>
<p style='text-align:center;color:gray;'>
🚰 WaterWatch | Nagpur NMC | AI Water Scarcity Forecast
</p>
""", unsafe_allow_html=True)

