import time
import pygame as p
import pywhatkit as kit

p.init()
p.display.set_caption("Loan Enrollment system")
ps1=p.display.set_mode((800,800))
ps=p.image.load(r"loan.png")
ps1.blit(ps,(10,60))
p.display.update()
time.sleep(5)
p.quit()

print("========= Loan Enrollment System =========")


name = input("Enter your Name: ")
password = input("Enter your password: ")
age = int(input("Enter your Age: "))
loan = input("Enter loan type (personal/business/home): ").lower()
gender = input("Enter your Gender: ")


print("--- Login ---")

def login():
    attempts = 3
    while attempts > 0:
        user = input("User: ")
        pas = input("Enter your Password: ")

        if user == name and pas == password:
            print("Login successful")
            return True
        else:
            attempts -= 1
            print(f"Invalid login:{attempts}")
            return False
        print("Too many failed attempts. Exiting.")
        return False


if login():
    print("====================Loan eligiblity check===================")
    salary = float(input("Enter the Salary:"))
    if salary >= 20000:

        if loan == "personal":
            loan_type = "Personal Loan"
            rate = 12
        elif loan == "business":
            loan_type = "Business Loan"
            rate = 10
        elif loan == "home":
            loan_type = "Home Loan"
            rate = 8
        else:
            print("Invalid loan type. Restart.")
            exit()
        print("You are eligible for this loan")

        print("================ Loan Details================")
        amount = float(input("Enter the Amount :"))
        annual_rate = rate  #  interst only
        time = int(input("Enter the payable loan completed time(months):"))  # 2 years count 24 months
        r = annual_rate / (12 * 100)
        emi = (amount * r * (1 + r) ** time) / ((1 + r) ** time - 1)  # emi
        print("\nLoan Type:", loan_type)
        print("Interest Rate:", rate, "%")
        print("Your EMI is:", round(emi, 2))
    else:
        print("You are not eligible for this loan")

print("\n====== Loan Sanction Details ======")
print("Bank Name: HDFC Bank")
print("Account Number: 123456789012")
print("IFSC Code: ABCD0001234")
print("Branch: Chennai Branch")

sanctioned_amount = amount
print("Sanctioned Loan Amount:", sanctioned_amount)

phone_number = input("Enter your WhatsApp number (with country code, e.g., +91...): ")

message = f"""
Hello {name},
Your loan has been approved!

Loan Type: {loan_type}
Amount: {sanctioned_amount}
EMI: {round(emi, 2)}

Thank you for choosing ABC Bank.
"""

kit.sendwhatmsg_instantly(phone_number, message)
