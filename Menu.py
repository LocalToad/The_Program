
import tkinter as tk
import tkinter.ttk as ttk

import jsonlib as j


def main_menu(settings):
    #this is all available setting choices for drop down windows
    income_types = ('income type', 'hourly','salary')
    screen_sizes = ('screen size',"400x300","800x600", "1200x900", "1920x1080")

    #open the main window
    root = tk.Tk()
    root.title(f"{settings["username"]}")

    #if the user has no setting params and is new this will generate new ones for them
    if len(settings.keys()) == 1:

        #this function commits the settings the user inputs
        def commit_setup():
            # makes sure the entry feilds are full and then should reveile the button to confirm
            if name_entry.get() != "" and income_amount_entry.get() != "" and income.get() != income_types[0] and screen_choice.get() != screen_sizes[0]:
                #grab the name variable from the name_entry feild
                name = name_entry.get()
                #grab the income type variable from the income feild
                type = income.get()
                #grabs the income amount from the income amount entry feild
                amount = income_amount_entry.get()
                #grabs the screen size from the screen choice feild
                screen = screen_choice.get()
                #grabs the master settings from the json file holding all the users and their settings
                master = j.read_file('ignore/all_users.json')
                #filtering for the current user within the master set inster the data into the feilds in the set
                #if the dictionary doesnt have a key this is also create a key and place the value in the key value pair
                master[settings['username']]['name'] = name
                master[settings['username']]['income_type'] = type
                master[settings['username']]['income_amount'] = amount
                master[settings['username']]['screen_size'] = screen
                #this writes the updated master data dict back to the file overwriting the old data
                j.write_to_file('ignore/all_users.json', master)
                #this reboots the program without closing the window
                root.destroy()
                master = j.read_file('ignore/all_users.json')
                user_setting = master[settings['username']]
                main_menu(user_setting)
            else:
                lbl.configure(text="Please fill out all the fields before confirming")

        #sets up a frame for the settings within the window
        root.geometry("800x600")
        setup = ttk.Frame(root)
        setup.grid(row=0, column=0, sticky="nsew")

        #label that prompts the user to enter their settings
        lbl = ttk.Label(setup, text=f"{settings['username']} please enter your settings bellow")
        lbl.grid(row=0, column=0)

        #label denoting name
        lbl_name = ttk.Label(setup, text="Name")
        lbl_name.grid(row=1, column=0)

        #entry box for the user to input their name
        name_entry = ttk.Entry(setup)
        name_entry.grid(row=1, column=1)

        #variable to save the incoming value to
        income = tk.StringVar(setup)
        income.set('Input Income Type')
        #this is a drop down menu for selecting the income type
        income_type = ttk.OptionMenu(setup,income, *income_types)
        income_type.grid(row=2, column=0, columnspan=2)

        #this prompts the user to input their income amount
        lbl_income_amount = ttk.Label(setup, text="Income Amount")
        lbl_income_amount.grid(row=3, column=0)

        #this is an entry box for the user to input their income
        income_amount_entry = ttk.Entry(setup)
        income_amount_entry.grid(row=3, column=1)

        #this is a variable to save the incoming value
        screen_choice = tk.StringVar(setup)
        screen_choice.set('Input Screen Size')
        #this is a drop down menu for the user to select screen size default of this window
        screen_size = ttk.OptionMenu(setup,screen_choice,*screen_sizes)
        screen_size.grid(row=4, column=0, columnspan=2)


        #this button confirms that the user is done and commits the settings
        btn = ttk.Button(setup, text="Confirm", command=commit_setup)
        btn.grid(row=5, column=0)

    #if the user already has setting params then it runs the program like normal
    else:
        #this sets the screen size to the size denoted in the users settings params
        root.geometry(settings["screen_size"])


        def commit_setup():
            # makes sure the entry feilds are full and then should reveile the button to confirm
            if name_entry.get() != "" and income_amount_entry.get() != "" and income.get() != income_types[0] and screen_choice.get() != screen_sizes[0]:
                #grab the name variable from the name_entry feild
                name = name_entry.get()
                #grab the income type variable from the income feild
                type = income.get()
                #grabs the income amount from the income amount entry feild
                amount = income_amount_entry.get()
                #grabs the screen size from the screen choice feild
                screen = screen_choice.get()
                #grabs the master settings from the json file holding all the users and their settings
                master = j.read_file('ignore/all_users.json')
                #filtering for the current user within the master set inster the data into the feilds in the set
                #if the dictionary doesnt have a key this is also create a key and place the value in the key value pair
                master[settings['username']]['name'] = name
                master[settings['username']]['income_type'] = type
                master[settings['username']]['income_amount'] = amount
                master[settings['username']]['screen_size'] = screen
                #this writes the updated master data dict back to the file overwriting the old data
                j.write_to_file('ignore/all_users.json', master)
                #this reboots the program without closing the window
                root.destroy()
                master = j.read_file('ignore/all_users.json')
                user_setting = master[settings['username']]
                main_menu(user_setting)
            else:
                lbl.configure(text="Please fill out all the fields before confirming")

        #these functions that follow exist as tabs within the window, they will pop up underneath the tab buttons at the top of the screen

        #this is the main menu tab, this will be used to track general data as well as a toggle for changing the month
        def main_tab():
            #this builds the frame
            main = ttk.Frame(root)
            main.grid(row=1, column=0, sticky="nsew", columnspan=10)

            #this button should be placed at the bottom of the list
            pass_month_btn = ttk.Button(main, text="Pass Month", command=expense_tab)
            pass_month_btn.grid(row=5, column=0)

        #this is a tab used for changing user settings, when this tab is closed this should fully close out the whole screen and reboot, we will warn the user before commiting
        def settings_tab():
            #this builds the frame
            settings_frame = ttk.Frame(root)
            settings_frame.grid(row=1, column=0, sticky="nsew", columnspan=10)
            print(settings['username'])
            # label that prompts the user to enter their settings
            lbl = ttk.Label(settings_frame, text=f"{settings["username"]} please enter your settings bellow")
            lbl.grid(row=0, column=0)

            # label denoting name
            lbl_name = ttk.Label(settings_frame, text="Name")
            lbl_name.grid(row=1, column=0)

            # entry box for the user to input their name
            name_entry = ttk.Entry(settings_frame)
            name_entry.grid(row=1, column=1)

            # variable to save the incoming value to
            income = tk.StringVar(settings_frame)
            income.set('Input Income Type')
            # this is a drop down menu for selecting the income type
            income_type = ttk.OptionMenu(settings_frame, income, *income_types)
            income_type.grid(row=2, column=0, columnspan=2)

            # this prompts the user to input their income amount
            lbl_income_amount = ttk.Label(settings_frame, text="Income Amount")
            lbl_income_amount.grid(row=3, column=0)

            # this is an entry box for the user to input their income
            income_amount_entry = ttk.Entry(settings_frame)
            income_amount_entry.grid(row=3, column=1)

            # this is a variable to save the incoming value
            screen_choice = tk.StringVar(settings_frame)
            screen_choice.set('Input Screen Size')

            #this button confirms that the user is done and commits the settings
            btn = ttk.Button(settings_frame, text="Confirm", command=commit_setup)
            btn.grid(row=5, column=0)

        #this is the expense tab, this will be used for tracking and inputing expenses
        def expense_tab():
            #this builds the frame
            expenses = ttk.Frame(root)
            expenses.grid(row=1, column=0, sticky="nsew", columnspan=10)

        #this is the first this that actually runs and this boot the main menue tab to be the default open
        main_tab()

        #this is a button for the user to click on to change to the main menu tab
        main_btn = ttk.Button(root, text="Main", command=main_tab)
        main_btn.grid(row=0, column=0)

        #this is a button for the user to click on to change to the settings tab
        settings_btn = ttk.Button(root, text="Settings", command=settings_tab)
        settings_btn.grid(row=0, column=1)

        #this is a button for the user to click on to change to the expenses tab
        expense_btn = ttk.Button(root, text="Expenses", command=expense_tab)
        expense_btn.grid(row=0, column=2)
    root.mainloop()

