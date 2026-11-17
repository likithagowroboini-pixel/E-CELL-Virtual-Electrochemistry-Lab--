import streamlit as st
from calculations import nernst

st.title("🧮 Nernst Equation Investigation")
st.write("Study the effect of non-standard conditions on electrode/cell potential.")

E0 = st.number_input("Standard potential E° (V)", value=1.10, step=0.01)
n = st.number_input("Number of electrons n", min_value=1, value=2, step=1)
Q = st.number_input("Reaction quotient Q", min_value=0.000001, value=1.0, step=0.1)
T = st.number_input("Temperature T (K)", min_value=1.0, value=298.15, step=1.0)

if st.button("Run Nernst Calculation", type="primary"):
    E = nernst(E0,n,Q,T)
    st.latex(r"E = E^\circ - \frac{RT}{nF}\ln Q")
    st.success(f"E = {E:.5f} V")
    st.write(f"Substitution: E = {E0:.4f} − (8.314 × {T:.2f} / ({n} × 96485)) ln({Q:.6f})")
