"""
> PAYROLL
Group 6 Members:
1. Cometa, James Earl Ryan
2. Macalisang, Daniel Ian G.
3. Racoma, Vince Louie N.
4. Sohon, Bren D.
"""

import customtkinter as ctk
import tkinter.messagebox as tkmb
import CTkTable

app = ctk.CTk()
app.geometry("700x400")
# app['background']="maroon"
# bg_color = "maroon"
app.title("Payroll")

# data for table and msgbox
employee_info = [["Name", "₱ Salary"], ["Bren", 0], ["Ian", 0], ["James", 0], ["Vince", 0]]

# for creating the table - right side
table = CTkTable.CTkTable(master=app, row=5, column=2, values=employee_info)
table.grid(row=0, column=2, padx=10, pady=20, rowspan=6, sticky="nw")


# 'for row in ...' iterates through the 'employee_info' list, starting from index 1 (2nd element) since index 0 is
# the header row ('Name' and 'Salary') and we don't want to include that in displaying salaries
def displayEmployees():
    employees_info = ""
    for row in employee_info[1:]:  # inside this loop, the 'employees_info' string is updated.
        employees_info += f"{row[0]}: ₱{row[1]:.2f}\n"
        # it concatenates the employee's name(rtrvd from 'row[0]') and their salary (rtrvd from 'row[1]')
    tkmb.showinfo("Employees Information", employees_info)


def calc():
    try:
        rate = float(rate_entry.get())
        hoursRendered = float(hours_entry.get())
        latem = float(latem_entry.get())
        absentd = float(absentd_entry.get())
        tax = 0
        grossPay = hoursRendered * rate

        if 0 <= grossPay <= 21000:
            tax = 0
        elif 21001 <= grossPay <= 33333:
            tax = grossPay * 0.15
        elif 33334 <= grossPay <= 66666:
            tax = grossPay * 0.20
        elif 66667 <= grossPay <= 166666:
            tax = grossPay * 0.25
        elif 166667 <= grossPay <= 666666:
            tax = grossPay * 0.30
        elif grossPay > 666666:
            tax = grossPay * 0.35

        sssContributions = grossPay * 0.045
        philHealth = grossPay * 0.0275
        pagIbig = grossPay * 0.02
        latemDeduc = (rate / 60) * latem
        absentDeduc = rate * 8 * absentd

        netpay = grossPay - sssContributions - philHealth - pagIbig - latemDeduc - absentDeduc - tax

        employee_name = name_entry.get()

        for row in employee_info[1:]:
            roundedNetPay = round(netpay, 2)
            if row[0] == employee_name:
                row[1] = roundedNetPay
                break
            elif not employee_name.isalpha():
                tkmb.showwarning("Error", "Invalid Input")
                break
        else:
            tkmb.showwarning("Error", "Employee name not found")
            return

        # Recreate the table with the updated data
        updated_table = CTkTable.CTkTable(master=app, row=5, column=2, values=employee_info)
        updated_table.grid(row=0, column=2, padx=10, pady=20, rowspan=6, sticky="nw")

    except ValueError:
        tkmb.showerror("Error", "Please enter a valid numeric value.")


app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

name_label = ctk.CTkLabel(app, text="Employee's Name:")
name_entry = ctk.CTkEntry(app)
rate_label = ctk.CTkLabel(app, text="Hourly Rate:")
rate_entry = ctk.CTkEntry(app)
hours_label = ctk.CTkLabel(app, text="Hours Rendered:")
hours_entry = ctk.CTkEntry(app)
latem_label = ctk.CTkLabel(app, text="Late in Minutes:")
latem_entry = ctk.CTkEntry(app)
absentd_label = ctk.CTkLabel(app, text="Days Absent:")
absentd_entry = ctk.CTkEntry(app)

calc_btn = ctk.CTkButton(app, text="ADD SALARY", command=calc, height=30, width=20)
view_btn = ctk.CTkButton(app, text="VIEW EMPLOYEES", height=30, width=20, command=displayEmployees)

name_label.grid(row=0, column=0, sticky="ne", padx=10, pady=10)
name_entry.grid(row=0, column=1, sticky="nw", ipadx=60, pady=10, padx=(0, 20))
rate_label.grid(row=1, column=0, sticky="ne", padx=10, pady=10)
rate_entry.grid(row=1, column=1, sticky="nw", ipadx=60, pady=10, padx=(0, 20))
hours_label.grid(row=2, column=0, sticky="ne", padx=10, pady=10)
hours_entry.grid(row=2, column=1, sticky="nw", ipadx=60, pady=10, padx=(0, 20))
latem_label.grid(row=3, column=0, sticky="ne", padx=10, pady=10)
latem_entry.grid(row=3, column=1, sticky="nw", ipadx=60, pady=10, padx=(0, 20))
absentd_label.grid(row=4, column=0, sticky="ne", padx=10, pady=10)
absentd_entry.grid(row=4, column=1, sticky="nw", ipadx=60, pady=10, padx=(0, 20))

view_btn.grid(row=5, column=0, sticky="nes", pady=20, padx=(0, 0))
calc_btn.grid(row=5, column=1, sticky="nw", pady=20, padx=(90, 0))

app.mainloop()
