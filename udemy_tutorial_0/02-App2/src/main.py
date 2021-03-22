import filestack
from pdfReport import PdfReport, FileSharer
from flatmate import Flatmate
from bill import Bill

bill_amount = input("Insert a bill amount : ")
bill_period = input("Insert a bill period : ")
first_flatmate = input("Insert the first flatmate name : ")
first_flatmate_duration = input (f"How long did {first_flatmate} stayed ? ")
second_flatmate = input("Insert the second flatmate name : ")
second_flatmate_duration = input (f"How long did {second_flatmate} stayed ? ")


the_bill = Bill(int(bill_amount), bill_period)
flatmate_john = Flatmate(first_flatmate, int(first_flatmate_duration))
flatmate_mary = Flatmate(second_flatmate, int(second_flatmate_duration))

pdf_report = PdfReport(bill_period)
pdf_report.generate(flatmate_john, flatmate_mary, the_bill)

file_sharer = FileSharer(pdf_report.filename)
print(file_sharer.share())