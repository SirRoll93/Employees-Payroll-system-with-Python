
event = {}
employee = {'Asubonteng Vincent', 'Frimpong Maxwell', 'Dapaah Maxwell', 'Owusu Dapaah Aikins'}
emp_gross = {'Asubonteng Vincent': '', 'Frimpong Maxwell': '', 'Dapaah Maxwell': '', 'Owusu Dapaah Aikins': ''}
emp_total_deduct = {'Asubonteng Vincent': '', 'Frimpong Maxwell': '', 'Dapaah Maxwell': '', 'Owusu Dapaah Aikins': ''}
emp_net_pay = {'Asubonteng Vincent': '', 'Frimpong Maxwell': '', 'Dapaah Maxwell': '', 'Owusu Dapaah Aikins': ''}

try:
    def admin_menu():
        print("command list:__"
              " 'Payroll', ",
              " 'Events' ",
              " 'Print' ")
        print("The commands are case sensitive, make sure you type uppercase first")

        admin_option = input("Enter command:__")
        if admin_option == 'Payroll':
            print("You are in the Payroll Dashboard")
            payroll()
        elif admin_option == 'Events':
            print("You are in the Events Dashboard")
            events_menu()
        elif admin_option == 'Print':
            print("You are in the Payroll Dashboard")
            print_pay()
        else:
            print("Command error")
        return admin_menu()

    def events_menu():
        while True:
            event_name = str(input("Enter an event:__"))
            event_time = str(input("input time:__"))
            event_place = str(input("Input Place:__"))
            event.setdefault(event_name, [])
            event[event_name].append(event_time)
            event[event_name].append(event_place)
            for k, v in event.items():
                print(k, v)
                print("We will be expecting you")
            return admin_menu()

    def payroll():
        while True:
            print(employee)
            print("The names are case sensitive, make sure you type uppercase first")
            emp_type = input("Type in employee's name or\nType |Back| to return to menu:__")
            if emp_type == 'Back':
                admin_menu()
            else:
                num_periods = float(input("Number of periods taught per week:__"))
                print("Rate per period: 25")
                overtime = float(input("overtime(periods):__"))
                gross_pay = (num_periods * 25) + (overtime * 25 * 1.25)
                if gross_pay < 800:
                    ssnit = float(gross_pay * 0.02)
                    nhis = float(gross_pay * 0.02)
                    total_deduct = float(ssnit + nhis)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 801 and gross_pay <= 1200:
                    ssnit = float(gross_pay * 0.02)
                    nhis = float(gross_pay * 0.02)
                    total_deduct = float(ssnit + nhis)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 1201 and gross_pay <= 1699:
                    ssnit = float(gross_pay * 0.02)
                    nhis = float(gross_pay * 0.02)
                    total_deduct = float(ssnit + nhis)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 1700 and gross_pay <= 2500:
                    ssnit = float(gross_pay * 0.02)
                    nhis = float(gross_pay * 0.02)
                    total_deduct = float(ssnit + nhis)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 2501 and gross_pay <= 3000:
                    ssnit = float(gross_pay * 0.02)
                    nhis = float(gross_pay * 0.02)
                    total_deduct = float(ssnit + nhis)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                else:
                    ssnit = float(gross_pay * 0.02)
                    nhis = float(gross_pay * 0.02)
                    total_deduct = float(ssnit + nhis)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

    def print_pay():
        print(employee)
        print("The names are case sensitive, make sure you type uppercase first")
        emp_name = input("Type in name or\nType |Back| to return to menu:__")
        if emp_name in employee:
            print(emp_name, "Salary")
            print('Gross pay:__', emp_gross[emp_name], "Ghana cedis")
            print('Deductions:__', emp_total_deduct[emp_name], "Ghana cedis")
            print('Net pay:__', emp_net_pay[emp_name], "Ghana cedis")
        else:
            return admin_menu()

    admin_menu()
    events_menu()
    payroll()
except ValueError:
    print("Input Invalid.")

except OSError:
    print("Error in the system.")

except NameError:
    print("Variable not found.")
