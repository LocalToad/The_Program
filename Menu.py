
import tkinter as tk
import tkinter.ttk as ttk

import jsonlib as j


def main_menu(settings):

    root = tk.Tk()
    root.title(f"{settings["username"]}")

    if len(settings.keys()) == 1:
        income_types = ('hourly','salary')
        screen_sizes = ("400x300","800x600", "1200x900", "1920x1080")

        def commit_setup():
            name = name_entry.get()
            type = income.get()
            amount = income_amount_entry.get()
            screen = screen_choice.get()
            master = j.read_file('all_users.json')
            master[settings['username']]['name'] = name
            master[settings['username']]['income_type'] = type
            master[settings['username']]['income_amount'] = amount
            master[settings['username']]['screen_size'] = screen
            j.write_to_file('all_users.json', master)
            main_menu(settings)

        root.geometry("800x600")
        setup = ttk.Frame(root)
        setup.grid(row=0, column=0, sticky="nsew")

        lbl = ttk.Label(setup, text=f"{settings['username']} please enter your settings bellow")
        lbl.grid(row=0, column=0)

        lbl_name = ttk.Label(setup, text="Name")
        lbl_name.grid(row=1, column=0)

        name_entry = ttk.Entry(setup)
        name_entry.grid(row=1, column=1)

        income = tk.StringVar(setup)
        income.set(income_types[0])
        income_type = ttk.OptionMenu(setup,income, *income_types)
        income_type.grid(row=2, column=0, columnspan=2)

        lbl_income_amount = ttk.Label(setup, text="Income Amount")
        lbl_income_amount.grid(row=3, column=0)

        income_amount_entry = ttk.Entry(setup)
        income_amount_entry.grid(row=3, column=1)

        screen_choice = tk.StringVar(setup)
        screen_choice.set(screen_sizes[1])
        screen_size = ttk.OptionMenu(setup,screen_choice,*screen_sizes)
        screen_size.grid(row=4, column=0, columnspan=2)

        btn = ttk.Button(setup, text="Confirm", command=commit_setup)
        btn.grid(row=5, column=0)

    else:
        root.geometry(settings["screen_size"])

        def main_tab():
            main = ttk.Frame(root)
            main.grid(row=1, column=0, sticky="nsew")



            pass_month_btn = ttk.Button(main, text="Pass Month", command=expense_tab)
            pass_month_btn.grid(row=5, column=0)

        def settings_tab():
            settings = ttk.Frame(root)
            settings.grid(row=1, column=0, sticky="nsew")

            name_entry = ttk.Entry(settings)
            name_entry.grid(row=0, column=1)

        def expense_tab():
            expenses = ttk.Frame(root)
            expenses.grid(row=1, column=0, sticky="nsew")

        main_tab()
        main_btn = ttk.Button(root, text="Main", command=main_tab)
        main_btn.grid(row=0, column=0)

        settings_btn = ttk.Button(root, text="Settings", command=settings_tab)
        settings_btn.grid(row=0, column=1)

        expense_btn = ttk.Button(root, text="Expenses", command=expense_tab)
        expense_btn.grid(row=0, column=2)

