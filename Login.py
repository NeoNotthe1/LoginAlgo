# login and sign-up program
from time import sleep
import webbrowser


def sign_in(email, password):
    email_customer = input("\nEnter your email -> ")
    password_check = input("Enter your password -> ")
    counter = 0
    if email_customer[counter] == email[counter] and password_check[counter] == password[counter]:
        counter += 1
    else:
        sleep(5)
        print("Your password or email address is incorrect")
        sleep(2)
        re_submit = input("Sorry you must recreate your account or you may quit, y/n -> ")
        if re_submit == "y":
            login()
        else:
            print("Thank you for using this program.")
            quit()
    sleep(5)
    print("Logging in...")
    sleep(3)
    print("successfully logged in")
    sleep(1)
    print("Opening website..")
    sleep(5)
    webbrowser.open_new_tab("https://www.hackerrank.com/dashboard")


def login():
    cust_name = input("Enter Your Name -> ")
    cust_email = input("Enter Your Email -> ")
    cust_password = input("Enter your Password -> ")
    re_pass = input("Re-enter your password -> ")
    count = 0
    if cust_password[count] == re_pass[count]:
        count += 1
    else:
        print("\nProcessing...")
        sleep(5)
        print("Incorrect Kindly resubmit all of your details :(")
        login()
    print("\nProcessing... ")
    sleep(5)
    print("Details successfully saved!")
    sleep(3)
    ask = input("Would you like to print your details? y/n ")
    if ask == "y":
        print("Printing...")
        sleep(5)
        print("\n Details are:\tName\t\t\tEmail\t\t\t\t\t\t\tPassword")
        print(f"\t\t\t\t{cust_name}\t\t{cust_email}\t\t{cust_password}")
        sleep(5)
        ask_2 = input("\nWould you like to login to your account (y/n) -> ")
        if ask_2 == "y":
            sign_in(cust_email, cust_password)
        else:
            print("Thank you for using this program.")
            sleep(5)
            quit()
    else:
        ask_3 = input("Would you like to login to your account (y/n) -> ")
        if ask_3 == "y":
            sign_in(cust_email, cust_password)
        else:
            print("Thank you for using this program.")
            sleep(5)
            quit()


login()
