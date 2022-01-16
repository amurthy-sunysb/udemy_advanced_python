from flat import Bill, Flatmate
from report import PdfReport

bill_amount = input("Hey user, enter the bill amount")
bill_amount = float(bill_amount)
period = input("What is the bill period? E.g. December 2020")

name1 = input("What is your name?")
days_in_house1 = int(input(f"How many days did {name1} stay in the house"))

name2 = input("What is the name of the other flatmate?")
days_in_house2 = int(input(f"How many days did {name2} stay in the house"))

the_bill = Bill(amount = bill_amount, period = period)

Flatmate1 = Flatmate(name = name1, days_in_house = days_in_house1)
Flatmate2 = Flatmate(name = name2, days_in_house = days_in_house2)

print(f"{Flatmate1.name} pays: ", Flatmate1.pays(bill=the_bill, flatmate2=Flatmate2))
print(f"{Flatmate2.name} pays: ", Flatmate2.pays(bill=the_bill, flatmate2=Flatmate1))

pdf_report = PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(Flatmate1, Flatmate2, the_bill)