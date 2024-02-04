def main():
    print("This is a monthly loanly calculator")
    print('')
    
main()
principal=float(input("Enter the loan amount: "))
apr=float(input("Enter the annual insterest rate: "))
years=int(input("Enter the amount of yaers: "))

monthly_insterest_rate=apr/1200
amount_of_months=years*12
monthly_payment=principal*monthly_insterest_rate/(1-(1+monthly_insterest_rate)**(-amount_of_months))
print("The monthly payment for this loan is: %.2f"% monthly_payment)