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

m = Mortgage(0.07/12, # monthly interest rate
            30*12, #installments
            250000, #principal
            3000, #annual tax
            1500, #annual insurance
            0.5 #private mortgage insurance pct
            )

print(m)
print(f"Monthly payment {m.monthly_payment()}")
print(m.annual_insurance_amount_calculated())
print ( f"Annual tax and insurance {m.annual_insurance_amount_calculated()}")
print ( f"Monthly insurance and tax amount {m.monthly_insurance_and_tax_calculated()}")
print( f"Montly payment incl tax and interest {m.monthly_payment_w_tax_and_interest()}")


m2 = Mortgage(0.065/12, # monthly interest rate
            30*12, #installments
            200000, #principal
            0, #annual tax
            0, #annual insurance
            0.0 #private mortgage insurance pct
            )

print ( f" {m2.monthly_payment_w_tax_and_interest():.2f}")

dept_schedule = m2.dept_schedule()
for paym in dept_schedule:
    print ( f" {paym[0]} Principal : {paym[1]:.2f} - Payment :{paym[2]:.2f}")