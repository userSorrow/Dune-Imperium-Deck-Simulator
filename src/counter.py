class Counter:
    def __init__(self) -> None:
        self.spice_amt = 0
        self.water_amt = 0 
        self.solari_amt = 0
    
    def change_currency_amt(self, currencies:list, amt:list) -> None:
        for i in range(len(currencies)):
            if currencies[i].lower() == "spice":
                self.spice_amt += amt[i]
            elif currencies[i].lower() == "water":
                self.water_amt += amt[i]
            elif currencies[i].lower() == "solari":
                self.solari_amt += amt[i]
            else:
                raise Exception("Incorrect spelling or mistake of currency")
        
    def UI(self) -> str:
        return f"""
Currency Counter
~~~~~~~~~~~~~~~~

Spice: {self.spice_amt}
Solaris: {self.solari_amt}
Water: {self.water_amt}

~~~~~~~~~~~~~~~~
"""
    
    