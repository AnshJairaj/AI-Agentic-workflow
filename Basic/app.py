import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from data import SCENARIOS

from workflows import *

st.set_page_config(
    page_title="Enterprise Agentic AI",
    layout="wide"
)
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Scenario Details"
    ]
)

st.title(
    "Enterprise Agentic AI Workflows"
)
if page == "🏠 Home":

    st.markdown("""
    ## Enterprise Agentic AI Workflow Simulator

    This project demonstrates how Agentic AI can automate enterprise business processes using multiple collaborating AI agents.

    ### Key Concepts Demonstrated

    - Sequential Orchestration
    - Parallel Orchestration
    - Hierarchical Orchestration
    - Multi-Agent Collaboration

    ### Business Areas Covered

    - Learning & Development
    - Recruitment
    - IT Service Desk
    - Procurement
    - Employee Services
    """)

    st.info(
        "Use the left sidebar to open Scenario Details."
    )

    st.stop()

scenario = st.sidebar.selectbox(
    "Select Scenario",
    list(SCENARIOS.keys())
)

info = SCENARIOS[scenario]

st.header("Problem Statement")
st.info(info["problem"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("Agents")

    for agent in info["agents"]:
        st.success(agent)

with col2:
    st.subheader("Expected Outputs")

    for out in info["output"]:
        st.write("📌", out)

st.subheader("Workflow Diagram")

workflow = " ➜ ".join(info["workflow"])

st.markdown(
    f"""
    <div style="
        padding:20px;
        border-radius:15px;
        background-color:#0E1117;
        border:2px solid #1F77B4;
        text-align:center;
        font-size:22px;
        font-weight:bold;
        color:white;
        margin-bottom:20px;
    ">
    {workflow}
    </div>
    """,
    unsafe_allow_html=True
)
st.subheader("🎯 Orchestration Pattern")

if scenario == "AI-Powered Learning & Development":
    pattern = "Hierarchical + Parallel + Sequential"

elif scenario == "Smart Recruitment & Hiring":
    pattern = "Hierarchical + Parallel + Sequential"

elif scenario == "IT Service Desk Automation":
    pattern = "Hierarchical + Parallel"

elif scenario == "Procurement & Vendor Selection":
    pattern = "Hierarchical + Parallel + Sequential"

else:
    pattern = "Hierarchical + Sequential"


st.markdown(
    f"""
    <div style="
        background: linear-gradient(90deg,#003366,#00509e);
        padding:20px;
        border-radius:15px;
        color:white;
        text-align:center;
        font-size:24px;
        font-weight:bold;
        margin-bottom:20px;
        box-shadow:0px 6px 12px rgba(0,0,0,0.3);
    ">
        {pattern}
    </div>
    """,
    unsafe_allow_html=True
)
if st.button("Run Workflow"):

    with st.spinner(
        "Executing Agents..."
    ):

        if scenario == \
                "AI-Powered Learning & Development":

            results = run_learning_workflow()

        elif scenario == \
                "Smart Recruitment & Hiring":

            results = run_recruitment_workflow()

        elif scenario == \
                "IT Service Desk Automation":

            results = run_it_workflow()

        elif scenario == \
                "Procurement & Vendor Selection":

            results = run_procurement_workflow()

        else:

            results = run_leave_workflow()

    st.success(
        "Workflow Completed"
    )

    df = pd.DataFrame(results)

    st.dataframe(
        df,
        use_container_width=True
    )
    st.markdown("---")

st.caption(
    "Agentic AI Workflow Automation | Tata Steel Internship Project"
)