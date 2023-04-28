class Flatmate():
    """ Createes a flatmate object that pays a part of the bill """

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return round(bill.amount *  weight, 2)


class Bill():
    """ Object represents the individual bills that have to be paid such as total amount and period of the bill"""

    def __init__(self, amount: int, period: str):
        self.amount = amount
        self.period = period