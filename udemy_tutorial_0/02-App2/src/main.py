from flatmate import Flatmate
from bill import Bill

the_bill = Bill(120, "March 2021")
flatmate_john = Flatmate("John", 20)
flatmate_mary = Flatmate("Mary", 25)

print(flatmate_john.pays(the_bill))