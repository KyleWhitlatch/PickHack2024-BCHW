import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from validate_email import validate_email
import class_info
import database
import requests
import json

member = class_info.info()
# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 
  
app = ctk.CTk() 
app.geometry("400x500") 
app.title("Modern Login UI using Customtkinter") 


def signup():
    if len(user_entry.get()) > 0 and user_pass.get() == user_pass_rep.get(): 
        # Send a POST request to the Flask application with the new user's information
        headers = {'Content-Type': 'application/json'}
        member.set_pw_hash(str(user_pass.get()))
        hash_str = member.hash_string_gen()
        data = {'username': ''+str(user_entry.get()), 'hash_str': ''+str(hash_str)}
        print("signup: " + str(data))
        response = requests.post('http://127.0.0.1:5000/signup', json=data)
        print(response.status_code)
        print('Response body:', response.text)
        if response.status_code == 200:
            new_window = ctk.CTkToplevel(app) 

            new_window.title("Successfully made account") 
  
            new_window.geometry("350x150") 
            ctk.CTkLabel(new_window,text="YOU JUST LOST THE GAME!!").pack() 
            
            tkmb.showwarning(title='sign up successful',message='sign up successful!!')
            app.destroy()
        else:
            tkmb.showwarning(title='Wrong password or wrong system',message='wrong system or password')
            
    elif user_pass.get() != user_pass_rep.get(): 
        tkmb.showwarning(title='Wrong password',message='Please check your passwords match') 
    elif user_pass.get() == user_pass_rep.get(): 
        tkmb.showwarning(title='Wrong username',message='Please check your username and make sure it is a valid email') 
    else: 
        tkmb.showerror(title="Login Failed",message="Invalid Username and password or account already in the system") 
        
def login(): 
    
    # Get the username and password from the GUIs
    username = user_entry.get()
    password = user_pass.get()
    member.set_pw_hash(str(password))
    hash_str = member.hash_with_keccak()
    data = {'username': ''+str(user_entry.get()), 'hash_str': ''+str(hash_str)}
    print("loginL " + str(data))
    response = requests.post('http://127.0.0.1:5000/login', json=data)
    print(response.status_code)
    print('Response body:', response.text)
    # Check the response
    if response.status_code == 200:
        new_window = ctk.CTkToplevel(app) 
        ctk.CTkLabel(new_window,text="YOU JUST LOST THE GAME!!").pack()
        new_window.title("Successfully Logged In") 
        new_window.geometry("350x150") 
        tkmb.showwarning(title='correct password and system',message='correct password and system!!')
    else:
        tkmb.showwarning(title='Wrong password or wrong system',message='wrong system or password')
        
  
  
label = ctk.CTkLabel(app,text="This is the main UI page") 
  
label.pack(pady=20) 
  
  
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
  
label = ctk.CTkLabel(master=frame,text='Modern Login System UI') 
label.pack(pady=12,padx=10) 
  
  
user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 
  
user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 

user_pass_rep= ctk.CTkEntry(master=frame,placeholder_text="Re-Enter Password",show="*") 
user_pass_rep.pack(pady=12,padx=10)
  
button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 

button_sign = ctk.CTkButton(master=frame,text='Signup',command=signup)
button_sign.pack(pady=12,padx=10) 
  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 
  
  
app.mainloop()
