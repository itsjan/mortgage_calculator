from mortgage_calculator import Mortgage
from rich import print
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt


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
DEFAULT_PRINCIPAL = 200000
DEFAULT_YEARS = 30
DEFAULT_INTEREST = 6.5

principal: int = int(Prompt.ask(f"Enter principal, default is {DEFAULT_PRINCIPAL}", default=DEFAULT_PRINCIPAL))
years: int = int(Prompt.ask(f"Enter years, default is {DEFAULT_YEARS}", default=DEFAULT_YEARS))
annual_interest: int = int(Prompt.ask(f"Enter annual interest, default is {DEFAULT_INTEREST} percent", default=DEFAULT_INTEREST))



m2 = Mortgage(annual_interest/12, # monthly interest rate
            years*12, #installments
            principal, #principal
            0, #annual tax
            0, #annual insurance
            0.0 #private mortgage insurance pct
            )

print ( f" {m2.monthly_payment_w_tax_and_interest():.2f}")



table = Table(title="Dept Schedule")

table.add_column("Installment", justify="right", style="cyan", no_wrap=True)
table.add_column("Principal", style="magenta")
table.add_column("Payment", justify="right", style="green")

dept_schedule = m2.dept_schedule()
for paym in dept_schedule:
    table.add_row (f"{paym[0]}", f"Principal : {paym[1]:.2f}", f"Payment :{paym[2]:.2f}")

console = Console()
console.print(table)

