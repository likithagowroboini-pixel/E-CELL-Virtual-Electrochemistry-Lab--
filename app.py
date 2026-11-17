import streamlit as st

st.set_page_config(page_title="E-CELL | SRM Virtual Electrochemistry Lab", page_icon="⚗️", layout="wide")

st.markdown("""
<style>
.block-container {max-width: 1180px; padding-top: 1.5rem;}
.hero {padding: 34px; border: 1px solid #dbe5e9; border-radius: 18px; background: linear-gradient(135deg,#f0fdfa,#f8fafc);}
.hero h1 {font-size: 42px; margin-bottom: 5px;}
.card {border:1px solid #dbe5e9; border-radius:15px; padding:20px; background:white; min-height:155px;}
.tag {display:inline-block;padding:6px 10px;border-radius:999px;background:#e6fffb;margin-right:5px;font-size:13px;}
.section-title {margin-top: 28px;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("⚗️ E-CELL")
st.sidebar.caption("Virtual Electrochemistry Laboratory")
st.sidebar.divider()
st.sidebar.page_link("app.py", label="🏠 Home")
st.sidebar.page_link("pages/1_Virtual_Lab.py", label="🔬 Virtual Lab")
st.sidebar.page_link("pages/2_Nernst.py", label="🧮 Nernst Equation")
st.sidebar.page_link("pages/3_Gibbs.py", label="⚡ Gibbs Free Energy")
st.sidebar.page_link("pages/4_Theory.py", label="📚 Theory")
st.sidebar.page_link("pages/5_Quiz.py", label="📝 Quiz")
st.sidebar.page_link("pages/6_Report.py", label="📄 Application-Based Report")

st.markdown("""
<div class="hero">
<span class="tag">SRM • Semester I</span>
<span class="tag">Engineering Chemistry</span>
<h1>⚗️ E-CELL</h1>
<h3>Virtual Electrochemistry Laboratory</h3>
<p>Interactive investigation of galvanic cells, electrode potentials, the Nernst equation and Gibbs free energy.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Application-Based Learning</h2>', unsafe_allow_html=True)
cols = st.columns(4)
cards = [
("🔬","Virtual Galvanic Cell","Construct and investigate an electrochemical cell."),
("🧮","Nernst Equation","Study how concentration changes cell potential."),
("⚡","Gibbs Free Energy","Connect Ecell with thermodynamic spontaneity."),
("📄","Final Report","Generate an SRM-style application-based report.")
]
for col,(icon,title,desc) in zip(cols,cards):
    with col:
        st.markdown(f'<div class="card"><h2>{icon}</h2><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

st.markdown("### Suggested experiment flow")
st.write("**1. Construct cell → 2. Observe electron flow → 3. Change concentrations → 4. Calculate Ecell → 5. Calculate ΔG → 6. Record result → 7. Generate report**")

st.info("Use the Virtual Lab page first. The report page is designed to collect the experiment details and produce a structured academic document.")
