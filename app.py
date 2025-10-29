# Here 3 tabs are being generated 
# Tab 1 consists of the metadata mentioning all the attributes and a submit button to add the data as well
# Tab 2 provides the lineage graph
# Tab 3 provides creative dashboards with fraud summary
import streamlit as st
import pandas as pd
from db import get_all_metadata, add_metadata, update_metadata, delete_metadata, init_db
from lineage import render_lineage_graph
from fraud_model import fraud_summary, predict_fraud

st.set_page_config(page_title="Insurance Metadata Catalog", layout="wide")

st.title("🏦 Insurance Metadata Catalog + Fraud Dashboard")

# Initialize DB
init_db()

tab1, tab2, tab3 = st.tabs(["📜 Metadata Catalog", "🧩 Data Lineage", "⚠️ Fraud Detection"])

# ---- TAB 1: METADATA ----
with tab1:
    st.subheader("Manage Metadata Assets")
    data = pd.DataFrame(get_all_metadata(), columns=["id", "name", "type", "tags", "owner_role"])
    st.dataframe(data, use_container_width=True)

    with st.form("add_form"):
        name = st.text_input("Asset Name")
        asset_type = st.selectbox("Asset Type", ["policy", "claim", "model"])
        tags = st.text_input("Tags (comma separated)")
        role = st.selectbox("Owner Role", ["Admin", "Analyst", "Viewer"])
        submitted = st.form_submit_button("Add Asset")
        if submitted:
            add_metadata(name, asset_type, tags, role)
            st.success("Asset added successfully!")
            st.experimental_rerun()

# ---- TAB 2: LINEAGE ----
with tab2:
    st.subheader("Data Lineage Graph")
    render_lineage_graph()

# ---- TAB 3: FRAUD DASHBOARD ----
with tab3:
    st.subheader("Claims Fraud Summary")
    stats, fig = fraud_summary("data/sample.csv")
    st.write(f"**Total Claims:** {stats['total_claims']}")
    st.write(f"**Flagged Suspicious:** {stats['flagged']}")
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("Predict Fraud for a Claim")
    amount = st.number_input("Enter claim amount", min_value=0.0, step=1000.0)
    ctype = st.selectbox("Claim Type", ["medical", "auto", "property"])
    score, label = predict_fraud(amount, ctype)
    st.metric("Fraud Score", f"{score:.2f}")
    st.metric("Prediction", label)
