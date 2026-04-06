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

# --- MODULE 2: FRAMEWORK & PRIVACY ---
elif choice == "2. The CTFR Framework & Privacy":
    st.title("🏗️ The CTFR Framework")
    st.write("A prompt is only as good as its structure. We use the **Context-Task-Format-Reference** model[cite: 24].")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("The Four Pillars")
        st.info("**Context:** Your role (e.g., 'I am an applicant in a contested divorce')[cite: 102].")
        st.info("**Task:** Specific goal (e.g., 'Summarize the steps for a trial')[cite: 103].")
        st.info("**Format:** The output style (e.g., 'A 3-column table')[cite: 112].")
        st.info("**Reference:** The source of truth (e.g., 'Family Justice Rules 2024')[cite: 112].")
    
    with col2:
        st.subheader("🛡️ Privacy & Anonymisation")
        st.error("**MANDATORY REDACTION**")
        st.write("""
        Before inputting data into AI, you **must** remove[cite: 51]:
        * NRIC / Passport Numbers
        * Residential Addresses
        * Bank Account & Financial Details
        """)
        st.success("**Anonymisation Tip:** Use placeholders like '[Deceased Name]' or '[Property Address]' to keep the context without risking your data privacy[cite: 51, 54].")

# --- MODULE 3: DIVORCE ---
elif choice == "3. Case Study: Divorce":
    st.title("📑 Area of Law: Divorce")
    
    tab1, tab2, tab3 = st.tabs(["Sample Prompt", "Trusted Sources", "Verification Checklist"])
    
    with tab1:
        st.subheader("Initial Research Prompt")
        st.code("""
        CONTEXT: I am seeking a divorce in Singapore. My spouse does not agree.
        TASK: Explain the 'Normal Track' process and the '1-Fact' requirement.
        FORMAT: Plain English summary with a step-by-step timeline.
        REFERENCE: Women's Charter 1961 and Singapore Courts (judiciary.gov.sg).
        """, language="markdown")
        st.caption("This prompt helps users understand the 'irretrievable breakdown' of marriage[cite: 158].")

    with tab2:
        st.subheader("Primary References")
        st.write("* **Women's Charter 1961** (Section 95: Grounds for Divorce) [cite: 190]")
        st.write("* **Family Justice Courts Practice Directions 2024** [cite: 198]")
        st.write("* **MSF Family Assist Portal** [cite: 147]")

    with tab3:
        st.subheader("Audit Your AI Output")
        st.checkbox("Did the AI mention the 3-year marriage rule? [cite: 130]")
        st.checkbox("Did it distinguish between 'Interim' and 'Final' Judgment? [cite: 140, 141]")
        st.checkbox("Did it mention the Mandatory Co-Parenting Programme (if children are involved)? [cite: 126]")

# --- MODULE 4: PROBATE ---
elif choice == "4. Case Study: Probate":
    st.title("📜 Area of Law: Probate")
    
    tab1, tab2, tab3 = st.tabs(["Sample Prompt", "Trusted Sources", "Verification Checklist"])

    with tab1:
        st.subheader("Drafting Court Documents")
        st.code("""
        CONTEXT: I am challenging a Will in Singapore due to my father's lack of capacity (dementia).
        TASK: Draft the content for a Summons (Form 154) and an Affidavit (Form 54).
        FORMAT: Legal drafting style suitable for the Family Justice Courts.
        REFERENCE: Family Justice Courts Practice Directions 2024.
        """, language="markdown")
        st.caption("Using AI for initial drafting reduces the billable hours lawyers spend on basic admin tasks[cite: 38].")

    with tab2:
        st.subheader("Primary References")
        st.write("* **Probate and Administration Act 1934**")
        st.write("* **Intestate Succession Act 1967** (If no Will exists)")
        st.write("* **Family Justice Rules 2024** [cite: 246]")

    with tab3:
        st.subheader("Audit Your AI Output")
        st.checkbox("Is the document titled 'Originating Application' rather than 'Petition'? [cite: 231]")
        st.checkbox("Has the AI flagged 'Missing Information' like specific medical dates? [cite: 284, 287]")
        st.checkbox("Does the draft follow the 2024 Practice Direction numbering? [cite: 236]")

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
