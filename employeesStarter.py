
admin = {'Debbie': "Debbie"}
users = {}


def login():
    print("Welcome to Sir Roll's Payroll System")
    while True:
        user_user = input("Enter Username:___")
        user_pass = input("Enter Password:___")
        if user_user in admin and admin[user_user] == admin[user_user]:
            print("Bravo! Login Successful.")
            print("Hello Administrator, what do you want to do in your Dashboard? ")
            print("Things you can do on your dashboard.\n1. Compute the net salary of employees.\n2. Organise events.\n3. Print empoloyees payslip")
            import employeesData
            employeesData.admin_menu()
        else:
            print("Username or Password is incorrect.\n Please feel free and try again.")


login()
