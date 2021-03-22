from fpdf import FPDF
import webbrowser
import os

class PdfReport:

    """
    Creates a PDF file that containes data about the flatmate such as
        - Their names
        - Their due amount
        - The period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = f"{round(flatmate1.pays(bill, flatmate2), 2)}"
        flatmate2_pay = f"{round(flatmate2.pays(bill, flatmate1), 2)}"

        # Instanciate the pdf object
        pdf = FPDF(orientation="P", unit="pt", format="A4")

        # Creating a new page
        pdf.add_page()

        # Adding image
        pdf.image("https://www.superior-alarm.com/wp-content/uploads/2016/11/house-png-202.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align="C", ln=1)

        # Insert period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period :", border=0)
        pdf.cell(w=150, h=40, txt=bill.period , border=0, ln=1)

        # Insert name and due amount of flatmate 1
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=150, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=f"{flatmate1_pay} $", border=0, ln=1)

        # Insert name and due amount of flatmate 2
        pdf.cell(w=150, h=25, txt=flatmate2.name , border=0)
        pdf.cell(w=150, h=25, txt=f"{flatmate2_pay} $", border=0, ln=1)

        # Change directory to output
        os.chdir("../output")

        # Generate the PDF file
        pdf.output(f"{self.filename}.pdf")
        webbrowser.open(f"{self.filename}.pdf")