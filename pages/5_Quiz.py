import streamlit as st

st.title("📝 Electrochemistry Quiz")
qs=[
("Oxidation occurs at the",["Anode","Cathode","Salt bridge","Wire"],"Anode"),
("Reduction occurs at the",["Anode","Cathode","Salt bridge","Wire"],"Cathode"),
("For a spontaneous galvanic reaction, Ecell is generally",["Positive","Negative","Always zero","Undefined"],"Positive"),
("The relation between ΔG and E is",["ΔG=nFE","ΔG=-nFE","ΔG=E/nF","ΔG=RT/E"],"ΔG=-nFE"),
("The Nernst equation contains the reaction quotient",["Q","P only","V only","m only"],"Q")
]
answers={}
for i,(q,opts,ans) in enumerate(qs,1):
    answers[i]=st.radio(f"{i}. {q}",opts,key=f"q{i}")
if st.button("Submit Quiz",type="primary"):
    score=sum(answers[i]==qs[i-1][2] for i in range(1,len(qs)+1))
    st.success(f"Score: {score}/{len(qs)}")
