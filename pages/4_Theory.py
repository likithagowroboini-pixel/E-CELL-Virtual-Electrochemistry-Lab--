import streamlit as st

st.title("📚 Theory")
sections = [
("1. Galvanic Cell","A galvanic cell converts chemical energy into electrical energy through a spontaneous redox reaction. Oxidation occurs at the anode and reduction occurs at the cathode."),
("2. Electrode Potential","The standard reduction potential indicates the tendency of a species to undergo reduction under standard conditions. Cell potential is obtained from E°cell = E°cathode − E°anode."),
("3. Nernst Equation","The Nernst equation describes how cell/electrode potential changes under non-standard conditions: E = E° − (RT/nF) ln Q."),
("4. Gibbs Free Energy","The electrochemical and thermodynamic quantities are related by ΔG = −nFE. A positive cell potential corresponds to negative ΔG for a spontaneous reaction."),
("5. Salt Bridge","A salt bridge completes the electrical circuit and helps maintain electrical neutrality in the two half-cells.")
]
for title,body in sections:
    with st.expander(title, expanded=True):
        st.write(body)
