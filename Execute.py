
import tkinter as tk
from tkinter import ttk
import jsonlib as j
import Menu

def main(screen_size="800x600"):


    #construct and set params for login window
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x300")


    #functions used by the window
    def sign_up():
        #grabs the username trying to be used
        username = user_entry.get()
        #if there is anything in the user_entry feild
        if username:
            #add the username to the file
            j.write_file_dict("ignore/all_users.json", username.lower())
            lbl_login.configure(text="Signup complete, please login")
        #clear the user_entry feild
        user_entry.delete(0, tk.END)

    def login_check():
        #loads the dict of all users
        all_users = j.read_file('ignore/all_users.json')
        #receives the username from the entry box
        username = user_entry.get()
        #if the username is in the keys
        if username.lower() in all_users.keys():
            #tell the user the login was successful, i honestly dont think anyone will see this
            #i can maybe put like a wait command in here to make it feel like the program is loading but thats just to make the user happen
            lbl_login.configure(text=f"Login Successful for {username.lower()}")
            #closes the login window
            root.destroy()
            #opens the main menu on the other file, this file should end and not be used after this
            Menu.main_menu(all_users[username.lower()])
        #if the username was not in the
        else:
            #tell the user that their username was invalid and prompt them to try again
            lbl_login.configure(text=f"Login Failed for {username.lower()}, please try again")


    #decorate login window with labels and buttons

    #label at the top of the grid
    lbl_login = ttk.Label(root, text="Please Login")
    lbl_login.grid(row=0, column=0)

    #creates a box to allow for user input
    user_entry = ttk.Entry(root)
    user_entry.grid(row=1, column=0)
    #sets the enter key to loging
    user_entry.bind('<Return>', lambda e:login_check())

    #creates a button to run the login command
    btn_login = ttk.Button(root, text="Login", command=login_check)
    btn_login.grid(row=2, column=0)

    #creates a button to run the sign in command
    btn_sign_up = ttk.Button(root, text="Sign Up", command=sign_up)
    btn_sign_up.grid(row=3, column=0)


    #keeps the window open
    root.mainloop()

main()