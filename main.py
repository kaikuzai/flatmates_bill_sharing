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

    def pays(self, bill: str, flatmate_2):
        weight = self.days_in_house / (self.days_in_house + flatmate_2.days_in_house)
        return round(bill.amount *  weight, 2)  

class PdfReport():
    """ Creates a PDF file containing information about the flatmates names, the period, the billed amount and the devision"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Set font style 
        pdf.set_font(family='Times', size=24, style='B')

        # header
        pdf.cell(w=0, h=80, txt='Flatmates bill', border=1, align='C', ln=1)
        pdf.cell(w=150, h=40, txt='Period', border=1, align='C')
        pdf.cell(w=150, h=40, txt=bill.period, border=1, align='C', ln=1)
        pdf.cell(w=0, h=40, txt='flatmates', border=1, align='C', ln=1)
        pdf.cell(w=538.5, h=40, txt='Testing sizes', border=1, align='C', ln=1)


        pdf.output(f'{self.filename}.pdf')
 

electricity = Bill(100, "January")

flatmate_1 = Flatmate(name=9+6, days_in_house=80)
flatmate_2 = Flatmate(name="Angela", days_in_house=60)

print(f"{flatmate_1.name} pays {flatmate_2.name} €{flatmate_1.pays(electricity, flatmate_2=flatmate_2)}")

pdf_report = PdfReport(electricity.period)
pdf_report.generate(flatmate_1=flatmate_1, flatmate_2=flatmate_2, bill=electricity)
