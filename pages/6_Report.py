import streamlit as st
from report_generator import build_report

st.title("📄 Application-Based Learning Report")
st.caption("Structured in the style of an academic SRM application-based learning document.")

name1=st.text_input("Student 1 Name", "G. Likitha")
reg1=st.text_input("Student 1 Registration No.", "RA2611030050100")
name2=st.text_input("Student 2 Name")
reg2=st.text_input("Student 2 Registration No.")

course=st.text_input("Course", "Engineering Chemistry")
title=st.text_input("Task Title", "E-CELL – Virtual Electrochemistry Laboratory")

st.markdown("### Experiment data")
cell=st.text_input("Cell notation","Zn | Zn²⁺ || Cu²⁺ | Cu")
E0=st.number_input("E°cell (V)",value=1.10,step=0.01)
Q=st.number_input("Reaction quotient Q",value=1.0,min_value=0.000001,step=0.1)
E=st.number_input("Ecell (V)",value=1.10,step=0.01)
DG=st.number_input("ΔG (kJ mol⁻¹)",value=-212.0,step=1.0)

st.markdown("### Application-based task content")
context=st.text_area("Application / Engineering Context",
"""The virtual laboratory provides a controlled environment for investigating electrochemical cells. It allows learners to change electrode combinations and concentration conditions and immediately observe the effect on cell potential and Gibbs free energy.""")
observation=st.text_area("Observation",
"""A positive cell potential indicates a spontaneous reaction in the selected direction. Changing concentration changes the reaction quotient and therefore changes the cell potential according to the Nernst equation.""")
conclusion=st.text_area("Conclusion",
"""The E-CELL virtual laboratory demonstrates the relationship among electrode potentials, concentration, cell potential and Gibbs free energy through an interactive application-based experiment.""")

if st.button("Generate SRM-Style PDF",type="primary"):
    pdf=build_report(
        course=course,title=title,
        students=[(name1,reg1),(name2,reg2)],
        cell=cell,E0=E0,Q=Q,E=E,DG=DG,
        context=context,observation=observation,conclusion=conclusion
    )
    st.download_button("⬇️ Download Final PDF",pdf,"E-CELL_Application_Based_Learning_Task.pdf","application/pdf")
    st.success("Your structured report is ready.")
