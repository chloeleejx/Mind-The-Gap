import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mind the Gap | Agile Knowledge Hub", layout="wide")

# Sidebar Navigation
with st.sidebar:
    st.title("🧭 Navigation")
    choice = st.radio("Go to:", [
        "1. Home: Fast-Track Roadmap",
        "2. The Architect (CTFR Framework)",
        "3. Case Study: Divorce",
        "4. Case Study: Probate",
        "5. The Auditor: Community Feedback"
    ])
    st.markdown("---")
    st.write("**Version 1.0 (Beta)**")
    st.caption("Focus: Agile Access to Justice")

# --- MODULE 1: HOME & FAST-TRACK ---
if choice == "1. Home: Fast-Track Roadmap":
    st.title("⚖️ Mind the Gap: Agile Knowledge Hub")
    st.subheader("Empowering the 'Legal Middle' through Rapid Iteration")
    
    st.markdown("""
    Instead of a slow, static rollout, our solution follows an **Agile Deployment Model**. 
    We provide the core framework today and expand based on real-world user demand.
    """)

    st.info("### 🚀 Our 4-Month Fast-Track Timeline")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Month 1**")
        st.caption("Deploy MVR (Minimum Viable Repository) with Divorce & Probate.")
    with col2:
        st.write("**Month 2**")
        st.caption("Soft Launch with Legal Clinics; collect 'Community Prompts'.")
    with col3:
        st.write("**Month 3**")
        st.caption("Analyze traffic to prioritize the next Area of Law.")
    with col4:
        st.write("**Month 4**")
        st.caption("Full Integration with official Singapore Law portals.")

    st.divider()
    st.subheader("🗳️ What should we build next?")
    st.write("We build what the community needs. Vote for the next module:")
    st.button("Small Claims Tribunal (SCT)")
    st.button("Employment Disputes")
    st.button("Personal Injury / Torts")

# --- MODULE 2: CTFR FRAMEWORK ---
elif choice == "2. The Architect (CTFR Framework)":
    st.title("🏗️ The CTFR Framework")
    st.write("The engine behind high-quality AI outputs. We teach users to architect, not just ask.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        **1. Context:** Define your legal standing.
        **2. Task:** Define the specific document or research goal.
        **3. Format:** Define the layout (e.g., Form 162 style).
        **4. Reference:** Direct AI to Singapore Statutes Online.
        """)
    with col_b:
        st.error("⚠️ **MANDATORY DATA PRIVACY**")
        st.write("Never input NRICs or bank details. Use our 'Anonymisation Protocol' below.")
        st.code("Prompt: 'Replace all NRIC numbers with [NRIC] before processing.'")

# --- MODULES 3 & 4: CASE STUDIES (Existing content remains here) ---
elif choice == "3. Case Study: Divorce":
    st.title("📑 Area of Law: Divorce")
    st.write("Focusing on the Women's Charter and 2024 Practice Directions.")
    st.code("CONTEXT: I am seeking a divorce... REFERENCE: Women's Charter 1961...")

elif choice == "4. Case Study: Probate":
    st.title("📜 Area of Law: Probate")
    st.write("Navigating Form 162 and the Intestate Succession Act.")
    st.code("CONTEXT: I am an executor... REFERENCE: Family Justice Rules 2024...")

# --- MODULE 5: THE AUDITOR & FEEDBACK ---
elif choice == "5. The Auditor: Community Feedback":
    st.title("🔍 The Auditor & Community Loop")
    
    st.markdown("""
    Legal AI is only safe when it is **Verified**. This page facilitates the 
    'Crowdsourced Audit' to keep the repository accurate.
    """)

    with st.expander("📢 Report a 'Hallucination' or AI Error"):
        st.text_input("Which AI tool were you using?")
        st.text_area("What was the incorrect information provided?")
        st.button("Submit for Legal Review")

    st.success("### How to Verify (The 3-Step Audit)")
    st.write("1. **Statutory Check:** Does the Section Number exist on Singapore Statutes Online?")
    st.write("2. **Form Check:** Does the layout match the SGCourts PDF templates?")
    st.write("3. **Date Check:** Is the AI using rules from before the 2024 updates?")
