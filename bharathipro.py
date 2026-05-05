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
users = []

n = int(input("Enter number of persons: "))

for i in range(n):
    print(f"\nEnter details for Person {i+1}")

    name = input("Enter your Name: ")
    password = input("Enter your password: ")
    age = int(input("Enter your Age: "))
    loan = input("Enter loan type (personal/business/home): ").lower()
    gender = input("Enter your Gender: ")

    users.append({
        "name": name,
        "password": password,
        "age": age,
        "loan": loan,
        "gender": gender
    })

print("--- Login ---")

def login(users):
    attempts = 3

    while attempts > 0:
        user = input("User: ")
        pas = input("Enter your Password: ")

        for u in users:
            if u["name"] == user and u["password"] == pas:
                print("Login successful")
                return u

        attempts -= 1
        print(f"Invalid login. Attempts left: {attempts}")

    return None

current_user = login(users)

if current_user:
    print("\nWelcome", current_user["name"])

    print("====================Loan eligiblity check===================")
    salary = float(input("Enter the Salary:"))
    if salary >= 20000:
     loan = current_user["loan"]
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
