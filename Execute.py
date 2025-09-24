
import tkinter as tk
import jsonlib as j


def main(screen_size="800x600"):


    #construct and set params for login window
    root = tk.Tk()
    root.title("Login")


    #functions used by the window
    def sign_up():
        #grabs the username trying to be used
        username = user_entry.get()
        #if there is anything in the user_entry feild
        if username:
            #add the username to the file
            j.write_file_list("all_users.json", username.lower())
        #clear the user_entry feild
        user_entry.delete(0, tk.END)

    def login_check():
        all_users = j.read_file('all_users.json')
        username = user_entry.get()
        if username.lower() in all_users:
            print(f'Loging in: {username.lower()}')
        else:
            print('login failed')


    #decorate login window with labels and buttons

    #label at the top of the grid
    lbl_login = tk.Label(root, text="Please Login")
    lbl_login.grid(row=0, column=0)

    #creates a box to allow for user input
    username = ''
    user_entry = tk.Entry(root, name=username)
    user_entry.grid(row=1, column=0)
    #sets the enter key to loging
    user_entry.bind('<Return>', lambda e:login_check())

    #creates a button to run the login command
    btn_login = tk.Button(root, text="Login", command=login_check)
    btn_login.grid(row=2, column=0)

    #creates a button to run the sign in command
    btn_sign_up = tk.Button(root, text="Sign Up", command=sign_up)
    btn_sign_up.grid(row=3, column=0)


    #keeps the window open
    root.mainloop()

main()