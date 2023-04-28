from fpdf import FPDF


class PdfReport():
    """ Creates a PDF file containing information about the flatmates names, the period, the billed amount and the devision"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2, input_bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        bill_flatmate_one = str(flatmate_1.pays(input_bill, flatmate_2))
        bill_flatmate_two = str(flatmate_2.pays(input_bill, flatmate_1))

        # Set font style 
        pdf.set_font(family='Times', size=24, style='B')

        # header
        pdf.cell(w=0, h=80, txt='Flatmates bill', align='C', ln=1)

        # Period
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=150, h=40, txt='Period', align='L')
        pdf.cell(w=388.5, h=40, txt=input_bill.period, align='L', ln=1)
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