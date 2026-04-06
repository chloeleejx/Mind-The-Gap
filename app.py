import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mind the Gap | Knowledge Hub", layout="wide")

# Sidebar Navigation
with st.sidebar:
    st.title("🧭 Navigation")
    choice = st.radio("Go to:", [
        "1. Home: Our Mission",
        "2. The Architect: CTFR Framework",
        "3. Use Case: Divorce Options",
        "4. Use Case: Contested Probate",
        "5. The Vault: Trusted References",
        "6. The Auditor: Verification Protocol"
    ])

if choice == "1. Home: Our Mission":
    st.title("⚖️ Mind the Gap: Building Bridges to Justice")
    st.markdown("""
    Our mission is to empower Singapore's **'Legal Middle'**—those who earn too much for legal aid but find market-rate law firm fees a significant burden[cite: 6, 8, 9].
    
    ### How this Digital Repository Works:
    This hub serves as a **Knowledge Infrastructure** to help Self-Represented Persons (SRPs) use Generative AI safely[cite: 22]. We provide:
    * **Architecture:** Structured prompting frameworks[cite: 24].
    * **Authority:** Links to official Singaporean legal sources[cite: 30, 62].
    * **Auditing:** Methods to verify AI output and prevent 'hallucinations'[cite: 59, 63].
    """)

elif choice == "2. The Architect: CTFR Framework":
    st.header("🏗️ The Context-Task-Format-Reference (CTFR) Framework")
    st.write("To get reliable legal research from AI, you must structure your prompt with these four pillars[cite: 24]:")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.info("**Context**\n\nWho are you in this case? (e.g., Surviving spouse)")
    with col2: st.info("**Task**\n\nWhat is the specific goal? (e.g., Understand ADR options)")
    with col3: st.info("**Format**\n\nHow should the answer look? (e.g., A step-by-step table)")
    with col4: st.info("**Reference**\n\nWhich Singaporean law applies? (e.g., Women's Charter)")

    st.warning("⚠️ **MANDATORY REDACTION:** Never input NRICs, residential addresses, or bank account numbers into an AI tool[cite: 51, 54].")

elif choice == "3. Use Case: Divorce Options":
    st.header("📑 Use Case: Navigating Divorce in Singapore")
    st.write("For those seeking to understand the 'Normal' vs 'Simplified' tracks[cite: 115, 157].")
    
    st.subheader("Sample CTFR Prompt [cite: 100-106]")
    st.code("""
    CONTEXT: I am seeking a divorce in Singapore.
    TASK: Explain the options available to me, including alternative dispute resolution (ADR).
    FORMAT: Use plain English. Provide a table comparing 'Simplified' vs 'Normal' tracks.
    REFERENCE: Use official government sources like Singapore Courts (judiciary.gov.sg).
    """)
    
    st.subheader("Key Concepts to Verify [cite: 117-127]")
    st.write("- **Mediation:** Settling disagreements with a neutral third party.")
    st.write("- **Counselling:** Mandatory if children under 21 are involved.")
    st.write("- **3-Year Rule:** Requirement to have been married for 3 years before filing.")

elif choice == "4. Use Case: Contested Probate":
    st.header("📜 Use Case: Challenging a Will (Probate)")
    st.write("Guidance for challenging testamentary capacity due to dementia[cite: 241].")
    
    st.subheader("Sample CTFR Prompt [cite: 240-244]")
    st.code("""
    CONTEXT: I am challenging the validity of my father's Will against an Executor in Singapore.
    TASK: Draft the content for a Summons and a Generic Affidavit.
    FORMAT: Suitable for addressing the court. Use Forms 54 and 154.
    REFERENCE: Family Justice Courts Practice Directions 2024.
    """)
    
    st.error("⚠️ **Verification Check:** AI often confuses 'Petitions' (old rules) with 'Originating Applications' (2024 rules). Always verify the Form number[cite: 227, 236].")

elif choice == "5. The Vault: Trusted References":
    st.header("📚 The Reference Vault")
    st.write("Always instruct AI to rely **exclusively** on these sources for Singaporean matters[cite: 30, 62]:")
    
    st.markdown("""
    * **Singapore Statutes Online (SSO):** For the Women's Charter, Intestate Succession Act, etc.
    * **Singapore Courts (Judiciary.gov.sg):** For Practice Directions and Court Forms.
    * **Family Justice Rules 2024:** For the latest procedural requirements[cite: 198, 231].
    """)
    st.link_button("Access Singapore Statutes Online", "https://sso.agc.gov.sg/")

elif choice == "6. The Auditor: Verification Protocol":
    st.header("🔍 The Auditor: How to Catch Hallucinations")
    st.write("AI can generate inaccurate case law or procedures[cite: 60]. Use this 3-step audit[cite: 62, 63]:")
    
    st.success("**Step 1: The Citation Check**\n\nAsk the AI: 'Which specific section of the Singapore law are you citing?' Cross-check it on SSO.")
    st.success("**Step 2: The Form Match**\n\nDoes the AI's draft match the official Form 162 or Form 54 on the Judiciary website?")
    st.success("**Step 3: Human-in-the-Loop**\n\nSeek document verification services from a law firm for a 'Limited Scope' review[cite: 46, 65, 74].")
