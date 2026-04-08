import streamlit as st
import pandas as pd # For handling the library data

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
        "3. Reference Library",
        "4. Prompt Library & Community Hub"
    ])
    st.markdown("---")
    st.write("**Version 1.0 (Beta)**")

# --- MOCK DATA FOR THE LIBRARY ---
# In a real app, this would come from a database.
prompt_data = [
    {"Area": "Divorce", "Use Case": "Legal Research", "Likes": 24, "Prompt": "CONTEXT: I am seeking a divorce... TASK: Explain the 1-fact requirement..."},
    {"Area": "Probate", "Use Case": "Legal Drafting", "Likes": 15, "Prompt": "CONTEXT: I am an executor... TASK: Draft Form 162 for Originating Application..."},
    {"Area": "Divorce", "Use Case": "Summarisation", "Likes": 38, "Prompt": "CONTEXT: I have a 20-page mediation report... TASK: Summarize the key custody disputes..."},
]
df = pd.DataFrame(prompt_data)

# --- MODULE 1: MISSION ---
if choice == "1. Why This Guide Exists":
    st.title("Why This Guide Exists")
    
    # Using a container to group the problem statement
    with st.container():
        st.markdown("""
        Middle-income earners in Singapore often face a **justice gap**: 
        they earn too much for state-subsidised legal aid but struggle to afford full-service law firm fees.
        """)
        
        st.info("""
        **The SRP Challenge:** Many individuals proceed as Self-Represented Persons (SRPs), where they must:
        * Understand legal principles
        * Comply with procedural rules
        * Represent themselves in court hearings
        
        In this role, you are held to the same standards as lawyers. In the past, many gave up, feeling this was an 'impossible mission' due to the overwhelming time and cost involved.
        """)

    # Transition to AI
    st.write("## The AI Revolution")
    st.markdown("The rise of generative AI changes everything. Using AI for legal research is not prohibited, provided you assume **full responsibility** for verifying information submitted to the Court.") 

    st.error("""
    **However, critical questions remain:**
    * Do you know how to use AI effectively to reduce research time?
    * Do you truly understand the output it generates?
    * Most importantly, how do you know the information is **correct**? 
    
    Without verification, are you willing to risk including wrong information in your court documents?
    """)

    # Mission and Framework using Columns for better flow
    st.divider()
    col_mission, col_how = st.columns(2)

    with col_mission:
        st.write("## 🎯 Our Mission")
        st.write("""
        This Guide provides the **Knowledge Infrastructure** to empower you to use generative AI 
        effectively at the initial stage of your case. By doing the administrative heavy lifting 
        yourself, you can save your limited financial resources for high-level legal strategy and advocacy.
        """)

    with col_how:
        st.write("## 🛠️ How This Guide Works")
        st.info("""
        **1. Craft:** Build high-quality prompts using the **CTFR framework**.
        
        **2. Refer:** Ground your AI in authoritative **Singaporean legal sources**.
        
        **3. Check:** Audit every response against **trusted primary checklists**.
        """)

    # Agile Feedback Loop
    st.divider()
    st.write("## 🗳️ What should we build next?")
    st.write("Our 'Fast-Track' model relies on user demand. Vote for the next area of law:")
    
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1: 
        st.button("Small Claims Diputes", use_container_width=True)
    with col_btn2: 
        st.button("Employment Disputes", use_container_width=True)
    with col_btn3: 
        st.button("Criminal Law", use_container_width=True)

# --- MODULE 2: CTFR Framework ---
elif choice == "2. Structuring a Good Prompt":
    st.title("Structuring a Good Prompt using the CTFR Framework")
    st.write("A prompt is only as good as its structure. Follow the **Context-Task-Format-Reference** framework to structure a good prompt.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("## Context")
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

        st.error("""
        **MANDATORY REDACTION**
        
        Before inputting data into AI, you **MUST** remove **personal data** and **sensitive information** including:
        * NRIC / Passport Numbers
        * Residential Addresses
        * Bank Account & Financial Details
        """)
        
        st.success("**Anonymisation Tip:** Use placeholders like '[Deceased Name]' or '[Property Address]' to keep the context without risking your data privacy.")

        st.write("## Format")
        st.info("""
        **Set your expectations. How should the AI respond to best meet your needs?**

        A well-defined format ensures the output is immediately useful.
        
        """)
        st.write("**Example:** Please use language suitable for addressing the Court.")

        st.write("### Consider specifying the following based on your needs:")
        col_f1, col_f2 = st.columns(2)

        with col_f1:
            st.markdown("""
            * **Language & Tone:** Specify 'Plain English' for better understanding of the laws
            * **Visual Aids:** Request 'a table' or 'a step-by-step timeline'
            * **Word Limit:** Avoid long, rambling AI responses
            """)

        with col_f2:
            st.markdown("""
            * **Level of Depth:** Ask for a 'high-level overview' for initial research or a 'comprehensive clause-by-clause analysis'
            * **Target Audience:** Tell the AI to write 'for the Court'
            """)
            
    with col2:
        st.write("## Task")
        st.info("""
        **Specify what do you want from the AI.** 
            
        Use **action verbs** such as 'Explain', 'Summarise', 'Draft' for better results.
        """)
        st.write("**Example: Draft** the court documents to be filed with the Singapore Court and **highlight** any missing information that I need to provide.")
    
        st.write("## Reference")
        st.info("**The source of truth.**")
        st.write("**Example:** Base your drafts on the forms uploaded. [Upload relevant court forms]")

# --- MODULE 3: REFERENCE ---
elif choice == "3. Reference Library":
    st.title("Reference Library")
    st.write("Select an area of law to find authoritative references and guidance on how to use them in your AI prompts.")

    tab_divorce, tab_probate, tab_general = st.tabs(["Divorce", "Probate", "General Civil"])

    with tab_divorce:
        st.write("## Family Law: Divorce")
        
        with st.expander("1. Women's Charter 1961", expanded=True):
            st.markdown("""
            **What it entails:** The primary legislation governing marriage and divorce in Singapore.
            **When to include:** When asking AI about the grounds for divorce (Section 95), child custody, or maintenance orders.
            """)
        
        with st.expander("2. Family Justice Courts Practice Directions 2024"):
            st.markdown("""
            **What it entails:** Procedural rules for how documents must be formatted and filed.
            **When to include:** When drafting court documents or checking timelines for service of papers.
            """)

    with tab_probate:
        st.write("## Succession Law: Probate")
        
        with st.expander("1. Probate and Administration Act 1934", expanded=True):
            st.markdown("""
            **What it entails:** Laws regarding the administration of a deceased person's estate.
            **When to include:** When identifying the duties of an executor or the process of applying for a Grant of Probate.
            """)
            
        with st.expander("2. Intestate Succession Act 1967"):
            st.markdown("""
            **What it entails:** Rules on how assets are distributed if there is **no Will**.
            **When to include:** When asking AI to calculate inheritance shares for family members.

            """)

    with tab_general:
        st.write("## General Legal Research")
        st.info("For any area not listed above, always direct your AI to use **Singapore Statutes Online (SSO)**.")
    
# --- MODULE 4: COMMUNITY HUB & LIBRARY ---
elif choice == "4. Prompt Library & Community Hub":
    st.title("Prompt Library & Community Hub")
    
    tab_library, tab_submit = st.tabs(["📚 Prompt Library", "📤 Submit a Prompt"])

    # --- TAB 1: SEARCHABLE LIBRARY ---
    with tab_library:
        st.write("## Editor-Approved Prompts")
        st.write("Browse and filter prompts that have been verified by our legal editors for accuracy and safety.")

        # Search and Filter Row
        col_search, col_filter_law, col_filter_use = st.columns([2, 1, 1])
        with col_search:
            search_query = st.text_input("Search prompts...", placeholder="e.g. 'Form 162' or 'Mediation'")
        with col_filter_law:
            law_filter = st.selectbox("Area of Law", ["All", "Divorce", "Probate"])
        with col_filter_use:
            use_filter = st.selectbox("Use Case", ["All", "Legal Research", "Legal Drafting", "Summarisation"])

        # Filter Logic
        filtered_df = df
        if law_filter != "All":
            filtered_df = filtered_df[filtered_df['Area'] == law_filter]
        if use_filter != "All":
            filtered_df = filtered_df[filtered_df['Use Case'] == use_filter]
        if search_query:
            filtered_df = filtered_df[filtered_df['Prompt'].str.contains(search_query, case=False)]

        # Display Prompts
        for index, row in filtered_df.iterrows():
            with st.expander(f"📌 {row['Area']} - {row['Use Case']} ({row['Likes']} 👍)"):
                st.code(row['Prompt'], language="markdown")
                st.button(f"Like this Prompt", key=f"like_{index}")
                st.caption("Verified by Editor on: 05 April 2026")

    # --- TAB 2: SUBMISSION PORTAL ---
    with tab_submit:
        st.write("## Share Your Success")
        st.write("Found a prompt that worked? Submit it here. Our editors will review, anonymise, and publish it to help others.")
        
        with st.form("submission_form"):
            user_prompt = st.text_area("Paste your Prompt here:")
            why_helpful = st.text_area("Why was this helpful? (e.g. 'It helped me understand the 3-year rule')")
            link = st.text_input("Link to Conversation or Screenshot URL (Optional):")
            
            st.warning("**Reminder:** Please remove personal data and sensitive information before submitting.")
            
            submitted = st.form_submit_button("Submit for Review")
            if submitted:
                st.success("Thank you! Your prompt has been sent to our editors for verification.")
