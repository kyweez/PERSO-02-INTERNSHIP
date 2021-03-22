from pdfReport import PdfReport
from flatmate import Flatmate
from bill import Bill

the_bill = Bill(120, "March 2021")
flatmate_john = Flatmate("John", 20)
flatmate_mary = Flatmate("Mary", 25)

print("John pays", flatmate_john.pays(the_bill, flatmate_mary))
print("Mary pays", flatmate_mary.pays(the_bill, flatmate_john))

pdf_report = PdfReport("Report.pdf")
pdf_report.generate(flatmate_john, flatmate_mary, the_bill)