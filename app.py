import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mind the Gap | Knowledge Hub", layout="wide")

# Custom CSS for professional branding
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stAlert { border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("⚖️ Mind the Gap")
    st.markdown("---")
    choice = st.radio("Navigation", [
        "1. Our Mission & Guide Overview",
        "2. The CTFR Framework & Privacy",
        "3. Case Study: Divorce",
        "4. Case Study: Probate",
        "5. The Auditor: Community Feedback"
    ])
    st.markdown("---")
    st.write("**Version 1.0 (Beta)**")
    st.caption("Focus: Agile Access to Justice")

# --- MODULE 1: MISSION ---
if choice == "1. Our Mission & Guide Overview":
    st.title("🚀 Why This Guide Exists")
    st.markdown("""
    Singapore's **'Legal Middle'**—individuals with a median monthly income of ~$5,775—often fall into a gap: 
    they earn too much for state-subsidised legal aid but struggle to afford full-service law firm fees[cite: 6, 9].
    
    ### Our Mission
    To provide a **Knowledge Infrastructure** that empowers Self-Represented Persons (SRPs) to use Generative AI 
    as a 'paralegal' tool. This reduces administrative costs, allowing users to save their limited 
    financial resources for high-level legal strategy and advocacy[cite: 22, 38].

    ### How This Guide Works
    This hub does not replace lawyers. It teaches you to:
    1. **Architect:** Build high-quality prompts using the CTFR framework[cite: 24].
    2. **Reference:** Use only authoritative Singaporean legal sources[cite: 30].
    3. **Audit:** Verify every AI response against trusted primary checklists[cite: 63].
    """)

# --- MODULE 2: FRAMEWORK & PRIVACY ---
elif choice == "2. The CTFR Framework & Privacy":
    st.title("Structuring a Good Prompt using the CTFR Framework")
    st.write("A prompt is only as good as its structure.Follow the **Context-Task-Format-Reference** framework to structure a good prompt.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("The Four Pillars")
        st.info("""
        **Context:** Tell AI your story using the 5W1H. 
        Examples of information to include:
        * Who are you? Who is involved?
        * What happened? 
        * When did it happen?
        """)
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
    
