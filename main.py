import tkinter
from tkinter import messagebox
import random
import pyperclip


def generate_secure_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    letters_to_use = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_to_use = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_to_use = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_to_use + symbols_to_use + numbers_to_use

    random.shuffle(password_list)

    password = ''.join(password_list)

    # print('Password to use: {}'.format(password))
    # password_input_box['text'] = password  # wrong!
    password_input_box.insert(index=0, string=password)

    pyperclip.copy(text=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # print('listening!')

    if len(website_input_box.get()) == 0 or len(password_input_box.get()) < 1:
        messagebox.showerror(title='Empty Fields', message='Do not leave any fields blank!')
        return

    website_entered = website_input_box.get()
    email_username_entered = email_username_input_box.get()
    password_entered = password_input_box.get()

    # messagebox.showinfo(title='Test Title', message='Test Message')
    # messagebox.askokcancel(title='Confirm Password Save',
    #                        message='Account Information:\n'
    #                                'Website - {website}\n'
    #                                'Email/Username - {email_or_username}\n'
    #                                'Password - {password}\n'
    #                                'Would you like to proceed with saving this information?'
    #                        .format(
    #                            website=website_entered,
    #                            email_or_username=email_username_entered,
    #                            password=password_entered,))
    save_information_confirmation = messagebox.askokcancel(title='Confirm Password Save',
                                                           message='Account Information:\n'
                                                                   'Website - {website}\n'
                                                                   'Email/Username - {email_or_username}\n'
                                                                   'Password - {password}\n'
                                                                   'Would you like to proceed with saving this '
                                                                   'information?'
                                                           .format(
                                                               website=website_entered,
                                                               email_or_username=email_username_entered,
                                                               password=password_entered))

    # with open(file='data.txt', mode='a') as file:
    #     file.write(f'Website: {website_entered}\n' +
    #                'Email/Username: {email_or_username}\n'.format(email_or_username=email_username_entered) +
    #                f'Password: {password_entered}\n' +
    #                # '--------------------------------------')
    #                '--------------------------------------\n')
    #
    # website_input_box.delete(0, tkinter.END)
    # # email_username_input_box.delete(0, tkinter.END)
    # password_input_box.delete(0, tkinter.END)

    if save_information_confirmation:
        with open(file='data.txt', mode='a') as file:
            file.write(f'Website: {website_entered}\n' +
                       'Email/Username: {email_or_username}\n'.format(email_or_username=email_username_entered) +
                       f'Password: {password_entered}\n' +
                       # '--------------------------------------')
                       '--------------------------------------\n')

        website_input_box.delete(0, tkinter.END)
        # email_username_input_box.delete(0, tkinter.END)
        password_input_box.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
# window
window = tkinter.Tk()
window.title(string='Password Manager')
window.minsize(width=200, height=200)
# window.config(padx=20, pady=20)
# window['padx'] = 20
# window['pady'] = 20
# window['padx'], window['pady'] = 20, 20
window.config(padx=50, pady=50)

# canvas widget
canvas = tkinter.Canvas(width=200, height=200)
password_lock_photo = tkinter.PhotoImage(file='./logo.png')
# canvas widget image
canvas.create_image(100, 100, image=password_lock_photo)  # centering lock png
# canvas.pack()
canvas.grid(row=0, column=1)

# ---
# column spanning (i.e. making widget(s) take up more than one column)
# from tkinter import *
#
# window = Tk()
#
# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)
#
# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)
#
# b = Label(bg="blue", width=40, height=5)
# b.grid(row=2, column=0, columnspan=2)
#
# window.mainloop()
# ---

# NOTE: grid indexing starts at 0

# labels
website_label = tkinter.Label(text='Website:')
website_label.grid(row=1, column=0)
email_username_label = tkinter.Label(text='Email/Username:')
email_username_label.grid(row=2, column=0)
password_label = tkinter.Label(text='Password:')
password_label.grid(row=3, column=0)

# entries
website_input_box = tkinter.Entry(width=35)
website_input_box.grid(row=1, column=1, columnspan=2)
website_input_box.focus()
email_username_input_box = tkinter.Entry(width=35)
email_username_input_box.insert(0, 'ttkhastalamuerte@gmail.com')
email_username_input_box.grid(row=2, column=1, columnspan=2)
# password_input_box = tkinter.Entry(width=15)
password_input_box = tkinter.Entry(width=17)
password_input_box.grid(row=3, column=1)

# buttons
# generate_password_button = tkinter.Button(text='Generate Password')
# generate_password_button = tkinter.Button(text='Generate Password', width=...)
generate_password_button = tkinter.Button(text='Generate Password', command=generate_secure_password)
generate_password_button.grid(row=3, column=2)
# add_button = tkinter.Button(text='Add', width=36)
# add_button = tkinter.Button(text='Add', width=30)
add_button = tkinter.Button(text='Add', width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop(n=0)
