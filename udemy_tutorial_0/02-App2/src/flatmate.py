class Flatmate:

    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    
    def pays(self, bill):
        return bill.amount / 2