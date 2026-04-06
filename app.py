import streamlit as st

st.set_page_config(page_title="Mind the Gap | Probate Repository", layout="wide")

# Custom Styling for a Professional Look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("🧭 Navigation")
    choice = st.radio("Select a Module", [
        "1. Home: The Mission",
        "2. The Architect: CTFR Framework",
        "3. The Vault: Trusted References",
        "4. The Auditor: Verification Samples"
    ])

if choice == "1. Home: The Mission":
    st.title("⚖️ Mind the Gap: Probate Digital Repository")
    st.subheader("Bridging the Justice Gap for Singapore's Middle-Income Earners")
    st.write("""
    This repository is a structured guide to using Generative AI safely and effectively 
    for probate matters in Singapore. We don't provide the AI—we provide the **Expertise** to use it.
    """)
    st.info("**Key Pillars:** Architecture (Prompting), Authority (References), and Audit (Verification).")

elif choice == "2. The Architect: CTFR Framework":
    st.header("🏗️ The CTFR Framework")
    st.write("To get accurate legal research, your prompt must have these four ingredients:")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Context", "Who are you?")
    col2.metric("Task", "What is the goal?")
    col3.metric("Format", "How should it look?")
    col4.metric("Reference", "Which law applies?")

    st.subheader("Sample Master Prompt for Probate")
    st.code("""
    CONTEXT: I am the surviving spouse of a deceased person in Singapore. No Will was left.
    TASK: List the documents required to apply for Letters of Administration.
    FORMAT: A bulleted list categorized by 'Court Forms' and 'Supporting Evidence'.
    REFERENCE: Family Justice Rules 2024 and Intestate Succession Act.
    CONSTRAINT: Do not provide legal advice; provide procedural guidance only.
    """, language="markdown")

elif choice == "3. The Vault: Trusted References":
    st.header("📚 The Reference Vault")
    st.write("Always instruct your AI tool to prioritize these specific Singaporean sources:")
    
    with st.expander("Probate & Administration"):
        st.write("- **Probate and Administration Act 1934**")
        st.write("- **Intestate Succession Act 1967** (For cases with no Will)")
        st.write("- **Family Justice Rules 2024** (For correct procedure)")
        st.link_button("View on Singapore Statutes Online", "https://sso.agc.gov.sg/")

elif choice == "4. The Auditor: Verification Samples":
    st.header("🔍 The Auditor: Spotting AI Errors")
    st.write("Compare the AI draft against the official 'Ground Truth'.")
    
    tab1, tab2 = st.tabs(["Sample Output Analysis", "Verification Checklist"])
    
    with tab1:
        st.error("❌ Common AI Error Sample")
        st.write("**AI Output:** 'You must file a Petition for Probate.'")
        st.warning("**The Auditor's Catch:** In Singapore, under the 2024 Rules, we file an **Originating Application (Form 162)**, not a 'Petition'.")
    
    with tab2:
        st.checkbox("Does the AI mention the 2024 Family Justice Rules?")
        st.checkbox("Has the AI included any fictional NRICs or addresses?")
        st.checkbox("Does the output match the templates on the Singapore Courts website?")
