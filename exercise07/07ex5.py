#Tehtävä L07T05

bank_account = float(input("Give balance of an account"))
add_euro = int(input ("How many euros is added to account?"))
add_cent = int(input ("How many cents is added to account?")) / 100
new_balance = bank_account + add_euro + add_cent
print("The new balance of the bank account is", new_balance)