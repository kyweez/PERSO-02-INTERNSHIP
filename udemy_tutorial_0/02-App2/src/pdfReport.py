from fpdf import FPDF

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
        pdf.image(link="https://www.superior-alarm.com/wp-content/uploads/2016/11/house-png-202.png")

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=1, align="C", ln=1)

        # Insert period label and value
        pdf.cell(w=100, h=40, txt="Period :", border=1)
        pdf.cell(w=150, h=40, txt=bill.period , border=1, ln=1)

        # Insert name and due amount of flatmate 1
        pdf.cell(w=150, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)

        # Insert name and due amount of flatmate 2
        pdf.cell(w=150, h=40, txt=flatmate2.name , border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        # Generate the PDF file
        pdf.output(self.filename)
