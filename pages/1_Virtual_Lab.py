import streamlit as st
from calculations import ecell, nernst, gibbs

st.title("🔬 Virtual Galvanic Cell Laboratory")
st.caption("Application: investigate a Daniell cell under different concentration conditions.")

metals = {
    "Zn / Zn²⁺": {"E": -0.76, "ion": "Zn²⁺", "metal":"Zn"},
    "Cu / Cu²⁺": {"E": 0.34, "ion": "Cu²⁺", "metal":"Cu"},
    "Fe / Fe²⁺": {"E": -0.44, "ion": "Fe²⁺", "metal":"Fe"},
    "Ag / Ag⁺": {"E": 0.80, "ion": "Ag⁺", "metal":"Ag"},
}

st.markdown("### 1. Construct the cell")
c1,c2 = st.columns(2)
with c1:
    anode = st.selectbox("Anode half-cell", list(metals.keys()), index=0)
    anode_c = st.number_input(f"{metals[anode]['ion']} concentration (M)", min_value=0.001, value=1.0, step=0.1)
with c2:
    cathode = st.selectbox("Cathode half-cell", list(metals.keys()), index=1)
    cathode_c = st.number_input(f"{metals[cathode]['ion']} concentration (M)", min_value=0.001, value=1.0, step=0.1)

if anode == cathode:
    st.error("Select two different half-cells.")
    st.stop()

Ea = metals[anode]["E"]
Ec = metals[cathode]["E"]
E0 = ecell(Ec,Ea)

# For the generic 2-electron metal-ion cell reaction: Q = cathode ion / anode ion.
Q = cathode_c / anode_c
E = nernst(E0, 2, Q, 298.15)
DG = gibbs(2,E)

st.markdown("### 2. Observe the virtual cell")
st.markdown(f"""
<div style="border:1px solid #cbd5e1;border-radius:18px;padding:25px;background:#f8fafc;text-align:center">
<h3>ANODE &nbsp;&nbsp; → e⁻ → &nbsp;&nbsp; CATHODE</h3>
<div style="display:flex;gap:10px;align-items:center;justify-content:center">
<div style="padding:22px;border:3px solid #64748b;border-radius:12px;background:#e2e8f0">
<b>{metals[anode]['metal']} electrode</b><br>{anode_c:.3f} M {metals[anode]['ion']}
</div>
<div style="font-size:28px">⚡ → ⚡</div>
<div style="padding:22px;border:3px solid #64748b;border-radius:12px;background:#e2e8f0">
<b>{metals[cathode]['metal']} electrode</b><br>{cathode_c:.3f} M {metals[cathode]['ion']}
</div>
</div>
<p><b>Salt bridge</b> connects the two half-cells and maintains electrical neutrality.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 3. Cell notation")
st.code(f"{metals[anode]['metal']} | {metals[anode]['ion']} ({anode_c:.3f} M) || {metals[cathode]['ion']} ({cathode_c:.3f} M) | {metals[cathode]['metal']}")

st.markdown("### 4. Calculated results")
a,b,c,d = st.columns(4)
a.metric("E°cell", f"{E0:.4f} V")
b.metric("Reaction quotient Q", f"{Q:.4f}")
c.metric("Ecell", f"{E:.4f} V")
d.metric("ΔG", f"{DG/1000:.3f} kJ mol⁻¹")

if E > 0:
    st.success("Result: Ecell is positive. The reaction is spontaneous in the selected direction under the entered conditions.")
else:
    st.warning("Result: Ecell is not positive in the selected direction.")

st.markdown("### 5. Observation")
st.write(f"Changing the ion concentrations changed Q to {Q:.4f} and therefore changed the cell potential from E°cell = {E0:.4f} V to Ecell = {E:.4f} V.")
