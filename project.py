class Rental_income():
    
    def __init__(self, rental_expenses, rental_income, down_payment, closing_cost):
        self.down_payment = int(input('How much was the downpayment on this property?' + '\n*Numbers only*'))
        self.closing_cost = int(input('What was the closing cost of the property?' + '\n*Numbers only*'))
        self.rentalIncome = int(input('How much will you be charging monthly for rent?' + '\n*Numbers only*')) 
        self.rentalExpenses = int(input('How much will you be spending annually to maintain your rental property? (Including Taxes, Insurance, CapEx, Utilites, Property Management, and money put aside for repairs/possible vacancy)' + '\n*Numbers only*'))
        
    def calculate_ROI(self):
        cash_flow = (self.rentalIncome - self.rentalExpenses)
        annual_cash_flow = (cash_flow * 12)
        total_investment = (self.down_payment + self.closing_cost)
        ROI = (annual_cash_flow/total_investment * 100)
        print(ROI)
        if annual_cash_flow/total_investment >= 0.09:
            print(f'ROI is greater than 9% - It looks like a good investment')
        else:
            print("Don't do it! ROI is too low")
    
    def runner(self):
        self.calculate_ROI()

            
rentalincome = Rental_income('rental_income', 'rental_expenses', 'down_payment', 'closing_cost')
rentalincome.runner() 