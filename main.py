
from flat import Bill, Flatmate
from pdf_report import PdfReport 

bill_type = input('what is the bill for? : ')
bill_size = float(input(f'how much is the {bill_type} bill? : '))
bill_period = input(f'for which period is the {bill_type} bill? : ')
name_flatmate_1 = input('what is the name of the first flatmate? : ')
name_flatmate_2 = input('what is the name of the second flatmate? : ')
days_present_f1 = int(input(f'how long was {name_flatmate_1} in the apartment? : '))
days_present_f2 = int(input(f'how long was {name_flatmate_2} in the apartment? : '))


input_bill = Bill(bill_size, bill_period)

flatmate_1 = Flatmate(name=name_flatmate_1, days_in_house=days_present_f1)
flatmate_2 = Flatmate(name=name_flatmate_2, days_in_house=days_present_f2)

print(f"{flatmate_1.name} pays {flatmate_2.name} €{flatmate_1.pays(input_bill, flatmate_2)}")

pdf_report = PdfReport(input_bill.period)
pdf_report.generate(flatmate_1=flatmate_1, flatmate_2=flatmate_2, input_bill=input_bill)

