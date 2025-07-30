from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)
pdf.cell(20,10,txt="Automated Report Generation",ln=2,align="c")
pdf.cell(100,10,txt="hello world........ ",ln=2,align="A")
pdf.output("mypdf.pdf")