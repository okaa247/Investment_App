
# Assignment:
# Build an Investment application that inputs an investors name, amount to invest. There’s a 50% increase in your wallet balance .

# To withdraw, Input the amount you want to withdraw ; if the amount is greater than the wallet balance - Print (insufficient funds) 
# But if the amount you want to withdraw is less than the wallet balance - Print (withdrawal successful, your account has been debited with …….. and 7% VAT  has been deducted)

# Pls note: 7% VAT deduction is from your wallet balance. 
# Your Final balance = amount withdrawn - wallet balance ; just same way your bank app works when you make a transfer….



print("Welcome To COHORT_1 Investment Platform.")


Initial_Bal = 0

#Input Your Name...
Name = input("Please Enter your Name: ")

#Input Your Investment Amount
Investment_Amount1 = int(input("Enter Amount to Invest: "))
print("Congratulations!", Name.upper(),"You have Invested", Investment_Amount1,".")

#50% of Invested Amount incremented
Investment_Amount2 = int(50/100 * Investment_Amount1)

#Wallet Balance
Wallet_Bal = Initial_Bal + Investment_Amount1 + Investment_Amount2
print("Your Wallet Balance is Now", Wallet_Bal)
print("")
#Withdrawal Amount
Withdraw_Amount = int(input("Enter Amount to Withdraw: "))

#7% VAT
Vert = 7/100 * Withdraw_Amount

#Final Balance...
Final_Bal1 = Wallet_Bal - Withdraw_Amount

#Final Balance Inclusive of 7% VAT
Final_Bal2 = Final_Bal1 - Vert


def Account_mgt():
     if  Withdraw_Amount > Wallet_Bal or Final_Bal2 < 0:
      print("You have Insufficient Funds!")
     else:
      print("Withdrawal successful, your account has been debited with", Withdraw_Amount, "and 7% VAT of", Vert, "has been deducted.")
      print("Your Current Balance is", Final_Bal2)


Account_mgt()
