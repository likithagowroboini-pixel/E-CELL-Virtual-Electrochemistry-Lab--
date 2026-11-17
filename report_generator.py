from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

def build_report(course,title,students,cell,E0,Q,E,DG,context,observation,conclusion):
    out=BytesIO()
    doc=SimpleDocTemplate(out,pagesize=A4,leftMargin=50,rightMargin=50,topMargin=45,bottomMargin=45)
    s=getSampleStyleSheet()
    s.add(ParagraphStyle(name="Inst",parent=s["Heading2"],alignment=TA_CENTER,fontSize=12,leading=16,spaceAfter=2))
    s.add(ParagraphStyle(name="Course",parent=s["Heading3"],alignment=TA_CENTER,fontSize=10,leading=14))
    s.add(ParagraphStyle(name="Task",parent=s["Title"],alignment=TA_CENTER,fontSize=18,leading=23,spaceBefore=12,spaceAfter=18))
    s.add(ParagraphStyle(name="Sec",parent=s["Heading2"],fontSize=12,leading=16,spaceBefore=13,spaceAfter=7))
    s.add(ParagraphStyle(name="Sub",parent=s["Heading3"],fontSize=10.5,leading=14,spaceBefore=8,spaceAfter=4))
    s.add(ParagraphStyle(name="Body2",parent=s["BodyText"],fontSize=9.5,leading=14,spaceAfter=6))
    story=[]

    story += [
        Paragraph("SRM INSTITUTE OF SCIENCE AND TECHNOLOGY, TIRUCHIRAPPALLI",s["Inst"]),
        Paragraph("SCHOOL OF SCIENCES – DIVISION OF CHEMISTRY",s["Course"]),
        Paragraph("SEMESTER I",s["Course"]),
        Paragraph(course,s["Course"]),
        Paragraph(title,s["Task"]),
        Paragraph("Application-Based Learning Task",s["Heading3"]),
        Spacer(1,12)
    ]
    rows=[["Student","Name","Registration No."]]
    i=1
    for n,r in students:
        if n:
            rows.append([f"Student {i}",n,r or ""])
            i+=1
    t=Table(rows,colWidths=[70,210,155])
    t.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.6,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#e8f1f5")),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
        ("FONTSIZE",(0,0),(-1,-1),8.5),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("PADDING",(0,0),(-1,-1),6),
    ]))
    story.append(t)
    story.append(Spacer(1,14))

    story.append(Paragraph("1. Virtual Galvanic Cell: Electrochemical Energy Conversion",s["Sec"]))
    story.append(Paragraph("a) Application Context",s["Sub"]))
    story.append(Paragraph(context,s["Body2"]))
    story.append(Paragraph("b) Cell Construction",s["Sub"]))
    story.append(Paragraph(f"The selected virtual cell is represented by: <b>{cell}</b>. The left half-cell acts as the anode and the right half-cell acts as the cathode for the selected spontaneous direction.",s["Body2"]))
    story.append(Paragraph("c) Electrode Processes",s["Sub"]))
    story.append(Paragraph("At the anode, oxidation occurs. At the cathode, reduction occurs. Electrons travel through the external circuit from the anode toward the cathode. The salt bridge completes the ionic path and maintains approximate electrical neutrality.",s["Body2"]))
    story.append(Paragraph("d) Standard Cell Potential",s["Sub"]))
    story.append(Paragraph("E°cell = E°cathode − E°anode",s["Body2"]))
    story.append(Paragraph(f"Using the virtual experiment values, E°cell = <b>{E0:.4f} V</b>.",s["Body2"]))

    story.append(Paragraph("2. Nernst Equation: Effect of Non-Standard Conditions",s["Sec"]))
    story.append(Paragraph("a) Governing Equation",s["Sub"]))
    story.append(Paragraph("E = E° − (RT/nF) ln Q",s["Body2"]))
    story.append(Paragraph("b) Experimental Variables",s["Sub"]))
    story.append(Paragraph(f"Reaction quotient entered: Q = <b>{Q:.4f}</b>. The virtual laboratory allows the concentration conditions to be changed and the resulting cell potential to be observed.",s["Body2"]))
    story.append(Paragraph("c) Calculated Cell Potential",s["Sub"]))
    story.append(Paragraph(f"The calculated cell potential for the recorded condition is <b>Ecell = {E:.4f} V</b>.",s["Body2"]))
    story.append(Paragraph("d) Interpretation",s["Sub"]))
    story.append(Paragraph("A change in concentration changes Q and therefore changes Ecell. This demonstrates the effect of non-standard conditions on an electrochemical cell.",s["Body2"]))

    story.append(Paragraph("3. Gibbs Free Energy: Thermodynamic Significance",s["Sec"]))
    story.append(Paragraph("a) Relationship",s["Sub"]))
    story.append(Paragraph("ΔG = −nFE",s["Body2"]))
    story.append(Paragraph("b) Result",s["Sub"]))
    story.append(Paragraph(f"For the recorded cell potential, ΔG = <b>{DG:.3f} kJ mol⁻¹</b>.",s["Body2"]))
    story.append(Paragraph("c) Engineering Interpretation",s["Sub"]))
    story.append(Paragraph("A negative ΔG corresponds to a spontaneous reaction in the direction represented by a positive cell potential. The virtual laboratory makes this connection visible through immediate numerical feedback.",s["Body2"]))

    story.append(Paragraph("4. Virtual Laboratory Implementation",s["Sec"]))
    story.append(Paragraph("a) User Interface",s["Sub"]))
    story.append(Paragraph("The website provides separate modules for the virtual cell, Nernst equation, Gibbs free energy, theory and quiz.",s["Body2"]))
    story.append(Paragraph("b) Interactive Experiment",s["Sub"]))
    story.append(Paragraph("Users can select half-cells and concentration values, run the experiment and obtain the corresponding cell notation and calculated electrochemical quantities.",s["Body2"]))
    story.append(Paragraph("c) Report Generation",s["Sub"]))
    story.append(Paragraph("The report module converts the entered experiment information into a structured academic PDF containing the application, equations, calculations, observations and conclusion.",s["Body2"]))

    story.append(Paragraph("5. Observation and Discussion",s["Sec"]))
    story.append(Paragraph(observation,s["Body2"]))
    story.append(Paragraph("6. Result",s["Sec"]))
    story.append(Paragraph("The E-CELL virtual experiment was successfully used to investigate galvanic-cell operation, non-standard cell potential and the thermodynamic significance of Gibbs free energy.",s["Body2"]))
    story.append(Paragraph("7. Conclusion",s["Sec"]))
    story.append(Paragraph(conclusion,s["Body2"]))

    story.append(Spacer(1,18))
    story.append(Paragraph("E-CELL – Virtual Electrochemistry Laboratory",s["Course"]))
    doc.build(story)
    out.seek(0)
    return out.getvalue()
