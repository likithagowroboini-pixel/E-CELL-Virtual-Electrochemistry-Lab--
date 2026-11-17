import streamlit as st
from calculations import gibbs

st.title("⚡ Gibbs Free Energy Investigation")
st.latex(r"\Delta G = -nFE")

n = st.number_input("Number of electrons n", min_value=1, value=2, step=1)
E = st.number_input("Cell potential E (V)", value=1.10, step=0.01)

if st.button("Calculate ΔG", type="primary"):
    DG = gibbs(n,E)
    st.success(f"ΔG = {DG:.3f} J mol⁻¹ = {DG/1000:.3f} kJ mol⁻¹")
    st.write("For a positive Ecell, ΔG is negative for the reaction written in the spontaneous direction.")
