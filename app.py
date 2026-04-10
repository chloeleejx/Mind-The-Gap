import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Mind the Gap | Knowledge Hub", layout="wide")

# --- ULTIMATE PROFESSIONAL CSS (Gov-Tech Standard) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600;700&display=swap');

    /* Global Body Overrides */
    .stApp {
        background-color: #F8FAFC; /* Modern Soft Grey/Blue background */
        font-family: 'Public Sans', sans-serif;
    }

    /* Professional Sidebar with Gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002B4B 0%, #001F35 100%);
        box-shadow: 2px 0px 10px rgba(0,0,0,0.1);
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* Custom Header Banner */
    .hero-banner {
        background: white;
        padding: 3rem;
        border-radius: 12px;
        border-bottom: 6px solid #B2955A;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
        text-align: left;
    }

    /* Professional "Card" styling */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0,0,0,0.05);
        border-color: #B2955A;
    }

    /* Buttons - Modern Rounded Style */
    .stButton>button {
        width: 100%;
        background-color: #002B4B;
        color: white !important;
        border-radius: 6px;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1rem;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #B2955A;
        transform: scale(1.02);
    }

    /* Typography Polish */
    h1 { color: #002B4B; font-weight: 800; letter-spacing: -0.5px; }
    h2, h3 { color: #002B4B; font-weight: 700; margin-top: 1.5rem; }
    
    /* Clean Divider */
    hr { margin: 2rem 0; border: 0; border-top: 1px solid #E2E8F0; }

    /* Custom Alert colors */
    .stAlert {
        border: none;
        border-radius: 8px;
        padding: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("## ⚖️ MIND THE GAP")
    st.markdown("---")
    choice = st.radio("MAIN NAVIGATION", [
        "Home: Mission",
        "User Guide",
        "Prompt Architect",
        "Reference Library",
        "Community Hub"
    ], index=0)
    st.markdown("---")
    st.caption("Singapore Legal Tech Initiative v1.2")

# --- DATA ---
df = pd.DataFrame([
    {"Area": "Divorce", "Type": "Drafting", "Likes": 24, "Content": "CONTEXT: ... TASK: ..."},
    {"Area": "Probate", "Type": "Research", "Likes": 15, "Content": "CONTEXT: ... TASK: ..."}
])

# --- MODULE 1: MISSION ---
if choice == "Home: Mission":
    st.markdown("""
        <div class="hero-banner">
            <h1>Mind the Gap</h1>
            <p style="color: #64748B; font-size: 1.2rem;">Bridging the Justice Gap with AI-Driven Knowledge Infrastructure.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### The Justice Gap")
        st.write("Singapore's 'Legal Middle'—those earning above the aid threshold but below the cost of private counsel—face an overwhelming barrier in Self-Representation.")
        st.info("**Challenge:** SRPs are held to professional standards, requiring mastery of legal principles and procedural rules overnight.")

    with col2:
        st.markdown("### The Solution")
        st.error("**Responsibility Notice:** AI is a support tool, not a replacement. All outputs must be verified against primary sources.")
        st.write("We provide the infrastructure to handle administrative research, allowing you to focus on high-level advocacy.")

    st.divider()
    st.write("### Choose a Pathway")
    p1, p2, p3 = st.columns(3)
    with p1: 
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("**🏗️ Architect**")
        st.caption("Build prompts using CTFR")
        st.markdown('</div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("**📚 Refer**")
        st.caption("Access the SSO Library")
        st.markdown('</div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("**🔍 Verify**")
        st.caption("Check against Court Forms")
        st.markdown('</div>', unsafe_allow_html=True)

# --- MODULE 3: PROMPT ARCHITECT ---
elif choice == "Prompt Architect":
    st.title("🏗️ Prompt Architect")
    st.write("Use the **CTFR Framework** to ensure your AI output is precise and grounded.")
    
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 1. Context")
            st.write("Explain your situation. Who is involved? What is the timeline?")
            st.warning("**🔒 PRIVACY FIRST:** Remove NRIC, Phone Numbers, and Financial Data.")
        with c2:
            st.markdown("### 2. Task")
            st.write("Use action verbs: *Explain Section 95*, *Summarise Mediation Report*, or *Draft Affidavit*.")
    
    st.divider()
    
    with st.container():
        c3, c4 = st.columns(2)
        with c3:
            st.markdown("### 3. Format")
            st.write("Request tables, bullet points, or 'Plain English' for clarity.")
        with c4:
            st.markdown("### 4. Reference")
            st.write("Direct the AI to specific Statutes (e.g. Women's Charter) or Practice Directions.")

# --- MODULE 4: REFERENCE LIBRARY ---
elif choice == "Reference Library":
    st.title("🏛️ Reference Library")
    t1, t2, t3 = st.tabs(["Overview", "Family Law (Divorce)", "Succession (Probate)"])
    
    with t1:
        st.write("### Authoritative Portals")
        cola, colb = st.columns(2)
        cola.info("**Singapore Statutes Online**\n\nThe primary source for all legislation.")
        colb.info("**Singapore Courts Website**\n\nThe source for Practice Directions.")
    
    with t2:
        st.write("### Divorce References")
        with st.expander("Women's Charter 1961"):
            st.write("Grounds for divorce (Section 95) and ancillary matters.")

# --- MODULE 5: COMMUNITY HUB ---
elif choice == "Community Hub":
    st.title("🤝 Community Knowledge Hub")
    st.write("Explore approved prompts or submit your own for verification.")
    
    # Simple search bar with pro styling
    search = st.text_input("Search the Library", placeholder="e.g. 'Probate Form'")
    
    for i, r in df.iterrows():
        st.markdown(f"""
            <div class="info-card">
                <span style="color: #B2955A; font-weight: bold;">{r['Area']}</span> | <b>{r['Type']}</b><br>
                <code style="display: block; margin-top: 10px; padding: 10px; background: #F1F5F9; border-radius: 5px;">{r['Content']}</code>
            </div>
        """, unsafe_allow_html=True)
        st.write("")
