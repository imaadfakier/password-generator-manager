import tkinter
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
#            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
#            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
#            'W', 'X', 'Y', 'Z']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# # print("Welcome to the PyPassword Generator!")
# # nr_letters= int(input("How many letters would you like in your password?\n"))
# # nr_symbols = int(input(f"How many symbols would you like?\n"))
# # nr_numbers = int(input(f"How many numbers would you like?\n"))
# # nr_letters = random.randint(8, 10)
# # nr_symbols = random.randint(2, 4)
# # nr_numbers = random.randint(2, 4)
#
# # Hard Level - Order of characters randomised:
# # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# # password = ""
# # letters_to_use = ""
# # symbols_to_use = ""
# # numbers_to_use = ""
# # random_password = ""
#
# # for letter in range(0, nr_letters):
# #     letters_to_use += letters[random.randint(0, len(letters) - 1)]
# # letters_to_use = [random.choice(letters) for _ in range(nr_letters)]
# letters_to_use = [random.choice(letters) for _ in range(random.randint(8, 10))]
# # for letter in range(0, nr_symbols):
# #     symbols_to_use += symbols[random.randint(0, len(symbols) - 1)]
# symbols_to_use = [random.choice(symbols) for _ in range(random.randint(2, 4))]
# # for letter in range(0, nr_numbers):
# #     numbers_to_use += numbers[random.randint(0, len(numbers) - 1)]
# numbers_to_use = [random.choice(numbers) for _ in range(random.randint(2, 4))]
#
# # password = letters_to_use + symbols_to_use + numbers_to_use
# password_list = letters_to_use + symbols_to_use + numbers_to_use
#
# # a_list = list(password)
# random.shuffle(password_list)
#
# # for char in a_list:
# #     random_password += char
# # password = ''
# # for char in password_list:
# #     password += char
# password = ''.join(password_list)
#
# # print(f"Password to use: {random_password}")
# print('Password to use: {}'.format(password))
# # print(f'Password to use: {password}')

# ######################### ANGELA'S ##########################
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
#            'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Hard Level
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")
# ######################## SOLUTION ###########################


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
