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
        "1. Why This Guide Exists",
        "2. Structuring a Good Prompt",
        "3. Case Study: Divorce",
        "4. Case Study: Probate",
        "5. Community Feedback"
    ])
    st.markdown("---")
    st.write("**Version 1.0 (Beta)**")

# --- MODULE 1: MISSION ---
if choice == "1. Why This Guide Exists":
    st.title("🚀 Why This Guide Exists")
    st.markdown("""
    Middle-income earners in Singapore often face a justic gap: 
    they earn too much for state-subsidised legal aid but struggle to afford full-service law firm fees.
    As a result, many individuals proceeded as Self-Represented Persons (SRPs), for which they must understand legal principles, comply with procedural rules, and represent themselves in court hearings, 
    while being held to the same standards as lawyers. 
    In the past, many would have given up as those seem like impossible mission with too much time and cost involved.
    The rise of generative AI changes everything. Using AI for legal research is not prohibited provided you assume full responsiblity for verifying information submitted to the Court. 
    But do you know how to use it effectively and reduce the time taken to find what you need and actually understand it?
    More importantly, how do you even know the information is correct and without knowing it, are you willing to risk including wrong information in your court documents?
    
    ### Our Mission
    This Guide aims to provide a **Knowledge Infrastructure** that empowers you to use generative AI 
    more effectively at the initial stage of your case so that you could save your limited financial resources for high-level legal strategy and advocacy.
    
    ### How This Guide Works
    It teaches you to:
    1. **Craft:** Build high-quality prompts using the CTFR framework.
    2. **Refer:** Use only authoritative Singaporean legal sources.
    3. **Check:** Verify every AI response against trusted primary checklists.
    """)

# --- MODULE 2: FRAMEWORK & PRIVACY ---
elif choice == "2. Structuring a Good Prompt":
    st.title("Structuring a Good Prompt using the CTFR Framework")
    st.write("A prompt is only as good as its structure. Follow the **Context-Task-Format-Reference** framework to structure a good prompt.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Context")
        st.info("""
        **Tell your story.**
        It is a good idea to include the following:
        * Who are you? Who is involved?
        * What happened? 
        * When did it happen?
        * Where did it happen?
        """)
        st.write("""
        **Example:** 
        
        I am starting an action in Singapore Court to challenge the validity of my father's Will against the Executor named in the Will. My father passed away recently leaving a Will dated 1 January 2026. 
        
        At the time of execution, my father was suffering from dementia and hence lacked the necessary testamentary capacity. 
        The Executor maintained the Will is valid and that my father was of sound mind when executing the Will. 
        """)

        st.error("**MANDATORY REDACTION**")
        st.write("""
        Before inputting data into AI, you **must** remove personal data and sensitive information including:
        * NRIC / Passport Numbers
        * Residential Addresses
        * Bank Account & Financial Details
        """)
        st.success("**Anonymisation Tip:** Use placeholders like '[Deceased Name]' or '[Property Address]' to keep the context without risking your data privacy.")

    with col2:
        st.subheader("Task")
        st.info("""
        **Specify what do you want from the AI.** 
        
        Use **action verbs** such as 'Explain', 'Summarise', 'Draft' for better results.
        """)
        st.write("**Example: Draft** the court documents to be filed with the Singapore Court and **highlight** any missing information that I need to provide.")

        st.subheader("Format")
        st.info("**The output style (e.g., 'A 3-column table').**")

        st.subheader("Reference")
        st.info("**The source of truth (e.g., 'Family Justice Rules 2024').**")

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

# --- MODULE 5: COMMUNITY FEEDBACK ---
elif choice == "5. Community Feedback":
    st.title("Community Feedback")
    
    st.markdown("""
    Legal AI is only safe when it is **verified**. This page facilitates the 
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
    
