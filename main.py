from fpdf import FPDF 

class Bill():
    """ Object represents the individual bills that have to be paid such as total amount and period of the bill"""

    def __init__(self, amount: int, period: str):
        self.amount = amount 
        self.period = period 


class Flatmate():
    """ Createes a flatmate object that pays a part of the bill """

    def __init__(self, name: str, days_in_house: int):
        self.name = name 
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return round(bill.amount *  weight, 2)  

class PdfReport():
    """ Creates a PDF file containing information about the flatmates names, the period, the billed amount and the devision"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        bill_flatmate_one = str(flatmate_1.pays(electricity, flatmate_2))
        bill_flatmate_two = str(flatmate_2.pays(electricity, flatmate_1))

        # Set font style 
        pdf.set_font(family='Times', size=24, style='B')

        # header
        pdf.cell(w=0, h=80, txt='Flatmates bill', align='C', ln=1)

        # Period
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=150, h=40, txt='Period', align='L')
        pdf.cell(w=388.5, h=40, txt=bill.period, align='L', ln=1)
        # pdf.cell(w=538.5, h=40, txt='Testing sizes', align='C', ln=1)
        # Name and total headers 
        pdf.set_font(family='Times', size= 14, style='B')
        pdf.cell(w=150, h=40, txt='Name', align='L')
        pdf.cell(w=388.5, h=40, txt='Total to pay', align='L', ln=1)

        # Individual names
        pdf.set_font(family='Times', size= 14)
        pdf.cell(w=150, h=40, txt=flatmate_1.name, align='L')
        pdf.cell(w=388.5, h=40, txt=bill_flatmate_one, align='L', ln=1)
        pdf.cell(w=150, h=40, txt=flatmate_2.name, align='L')
        pdf.cell(w=388.5, h=40, txt=bill_flatmate_two, align='L', ln=1)

        pdf.output(f'{self.filename}.pdf')
 

electricity = Bill(100, "January 2023")

flatmate_1 = Flatmate(name="Theodore", days_in_house=80)
flatmate_2 = Flatmate(name="Angela", days_in_house=60)

print(f"{flatmate_1.name} pays {flatmate_2.name} €{flatmate_1.pays(electricity, flatmate_2)}")

pdf_report = PdfReport(electricity.period)
pdf_report.generate(flatmate_1=flatmate_1, flatmate_2=flatmate_2, bill=electricity)
