# upgrade: write, read and update JSON data in the password manager via the json
# library
#   write; json.dump()
#   read; json.load()
#   update; json.update()

# NOTE: only use this concept of handling exceptions when if-elif-else (or any other
#       conditional logic) don't come to the rescue and there is no other
#       alternative - make use of exception(s) handling then :)

import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


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

    password_input_box.insert(index=0, string=password)

    pyperclip.copy(text=password)


# ---------------------------- SEARCH/FIND PASSWORD ------------------------ #
# def search_json_file():
def find_password():
    if len(website_input_box.get()) < 1:
        messagebox.showerror(title='No Website Provided', message='Enter website name.')
        return
    # elif ...

    website_entry = website_input_box.get()

    try:
        with open(file='./data.json', mode='r') as file:
            data_dict = json.load(fp=file)
    except FileNotFoundError:
        messagebox.showinfo(title='Data File Non-Existent', message='No data file found!')
    else:
        if website_entry in data_dict:
            messagebox.showinfo(title=website_entry.capitalize(),
                                message='Email/Username: {email_or_username}\nPassword: {password}'
                                .format(email_or_username=data_dict[website_entry]['email_or_username'],
                                        password=data_dict[website_entry]['password']))
            # messagebox.showinfo(title=website_entry.capitalize(),
            #                     message=f"Email/Username: {data_dict[website_entry]['email_or_username']}\n"
            #                             f"Password: {data_dict[website_entry]['password']}")
        else:
            # messagebox.showinfo(title='Website Account Non-Existent', message='No details for the website exist.')
            messagebox.showinfo(title='Website Account Non-Existent', message=f'No details for {website_entry} exist.')
    # finally:
    #     pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def create_json_file(a_dict):
    with open(file='./data.json', mode='w') as file:
        json.dump(obj=a_dict, fp=file, indent=4)


def update_json_file(the_dict):
    with open(file='./data.json', mode='w') as file:
        json.dump(obj=the_dict, fp=file, indent=4)


def save():

    if len(website_input_box.get()) == 0 or len(password_input_box.get()) < 1:
        messagebox.showerror(title='Empty Fields', message='Do not leave any fields blank!')
        return

    website_entered = website_input_box.get()
    email_username_entered = email_username_input_box.get()
    password_entered = password_input_box.get()

    # save_information_confirmation = messagebox.askokcancel(title='Confirm Password Save',
    #                                                        message='Account Information:\n'
    #                                                                'Website - {website}\n'
    #                                                                'Email/Username - {email_or_username}\n'
    #                                                                'Password - {password}\n'
    #                                                                'Would you like to proceed with saving this '
    #                                                                'information?'
    #                                                        .format(
    #                                                            website=website_entered,
    #                                                            email_or_username=email_username_entered,
    #                                                            password=password_entered))

    # if save_information_confirmation:
    #     with open(file='./data.txt', mode='a') as file:
    #         file.write(f'Website: {website_entered}\n' +
    #                    'Email/Username: {email_or_username}\n'.format(email_or_username=email_username_entered) +
    #                    f'Password: {password_entered}\n' +
    #                    # '--------------------------------------')
    #                    '--------------------------------------\n')

    new_data = {
        website_entered: {
            'email_or_username': email_username_entered,
            'password': password_entered,
        }
    }
    # new_data = dict()

    try:
        with open(file='./data.json', mode='r') as file:
            data = json.load(fp=file)
    except FileNotFoundError as fnf:
        create_json_file(new_data)
    else:
        data.update(new_data)
        update_json_file(data)
    finally:
        website_input_box.delete(0, tkinter.END)
        password_input_box.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
# window
window = tkinter.Tk()
window.title(string='Password Manager')
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# canvas widget
canvas = tkinter.Canvas(width=200, height=200)
password_lock_photo = tkinter.PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=password_lock_photo)  # centering lock png
canvas.grid(row=0, column=1)

# labels
website_label = tkinter.Label(text='Website:')
website_label.grid(row=1, column=0)
email_username_label = tkinter.Label(text='Email/Username:')
email_username_label.grid(row=2, column=0)
password_label = tkinter.Label(text='Password:')
password_label.grid(row=3, column=0)

# entries
# website_input_box = tkinter.Entry(width=35)
website_input_box = tkinter.Entry(width=34)
# website_input_box.grid(row=1, column=1, columnspan=2)
website_input_box.grid(row=1, column=1)
website_input_box.focus()
# email_username_input_box = tkinter.Entry(width=35)
# email_username_input_box = tkinter.Entry(width=60)
email_username_input_box = tkinter.Entry(width=59)
# email_username_input_box = tkinter.Entry(width=58)
email_username_input_box.insert(0, 'testemail@gmail.com')
email_username_input_box.grid(row=2, column=1, columnspan=2)
# password_input_box = tkinter.Entry(width=17)
# password_input_box = tkinter.Entry(width=35)
password_input_box = tkinter.Entry(width=34)
password_input_box.grid(row=3, column=1)

# buttons
# generate_password_button = tkinter.Button(text='Generate Password', command=generate_secure_password)
# generate_password_button = tkinter.Button(text='Generate Password', width=20, command=generate_secure_password)
generate_password_button = tkinter.Button(text='Generate Password', width=19, command=generate_secure_password)
# generate_password_button = tkinter.Button(text='Generate Password', width=18, command=generate_secure_password)
generate_password_button.grid(row=3, column=2)
# add_button = tkinter.Button(text='Add', width=30, command=save)
add_button = tkinter.Button(text='Add', width=50, command=save)
# add_button = tkinter.Button(text='Add', width=49, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text='Search', width=19, command=find_password)
# search_button = tkinter.Button(text='Search', width=20, command=find_password)
# search_button = tkinter.Button(text='Search', width=18, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop(n=0)
