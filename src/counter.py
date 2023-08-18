class Counter:
    def __init__(self) -> None:
        self.spice_amt = 0
        self.water_amt = 0 
        self.solari_amt = 0
    
    def change_currency_amt(self, currencies:list, amt:list) -> None:
        i = 0
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
        
    

exit = False
print("""This is a Resource Counter for Dune the Board Game
""")
while not exit:
    counter = Counter()
    
    currency_type = input("""Which currency would you like to change
> Spice
> Solari
> Water
Response: """).replace(" ", "").split("/")
    
    currency_amt = [int(i) for i in input("""\nHow much quantity would you like to change
Response: """).replace(" ", "").split("/")]
    
    counter.change_currency_amt(currency_type, currency_amt)
    print(counter.UI())
    
    