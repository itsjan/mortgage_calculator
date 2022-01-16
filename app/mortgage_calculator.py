class Mortgage:
    def __init__(self, r, N, P, annual_tax = 0, annual_insurance = 0, annual_insurance_pct=0):
        self.interest_rate = self.r = r
        self.number_of_payments = self.N = N
        self.amount_borrowed = self.P = P
        self.annual_insurance = annual_insurance
        self.annual_tax = annual_tax
        self.annual_insurance_pct = annual_insurance_pct

    def annual_insurance_amount_calculated(self):
        return (self.annual_insurance_pct/100*self.amount_borrowed) + self.annual_insurance

    def monthly_insurance_and_tax_calculated(self):
        return self.annual_insurance/12 + self.annual_insurance_amount_calculated()/12

    def __repr__(self):
        return f'''
        Monthly interest rate: {self.r:.5f}\n
        Number of monthly payments: {self.N}\n
        Amount borrowed: {self.P}'''

    def monthly_payment(self, principal = 0) : #self.amount_borrowed):
        if principal == 0: principal = self.amount_borrowed
        return self.r* self.P * (1+self.r)**self.N / ( (1+self.r)**self.N-1)

    def monthly_payment_w_tax_and_interest (self) :
        return self.monthly_payment() + self.monthly_insurance_and_tax_calculated()

    def dept_schedule(self):
        payments = []
        principal = self.amount_borrowed
        for i in range(0,self.number_of_payments):
            payment = min(principal, self.monthly_payment(principal=principal))
            payments.append([i+1, principal, payment])
            principal -= self.amount_borrowed/self.number_of_payments
        return payments
