import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from validate_email import validate_email
import class_info
  

member = class_info.info()
# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 
  
app = ctk.CTk() 
app.geometry("400x500") 
app.title("Modern Login UI using Customtkinter") 
my_entries = []



def signup():
    is_valid = validate_email(user_entry.get())
    new_window = ctk.CTkToplevel(app) 
  
    new_window.title("Successfully made account") 
  
    new_window.geometry("350x150") 
    if is_valid and user_pass.get() == user_pass_rep.get(): 
        ctk.CTkLabel(new_window,text="YOU JUST LOST THE GAME!!").pack() 
        member.set_pw_hash(user_pass.get)
        member.hash_string_gen()
    elif is_valid and user_pass.get() != user_pass_rep.get(): 
        tkmb.showwarning(title='Wrong password',message='Please check your passwords match') 
    elif not is_valid and user_pass.get() == user_pass_rep.get(): 
        tkmb.showwarning(title='Wrong username',message='Please check your username and make sure it is a valid email') 
    else: 
        tkmb.showerror(title="Login Failed",message="Invalid Username and password or account already in the system") 
        
def login(): 
  
    username = "Geeks"
    password = "12345"
    new_window = ctk.CTkToplevel(app) 
  
    new_window.title("Successfully Logged In") 
  
    new_window.geometry("350x150") 
    is_valid = validate_email(user_entry.get())
  
    if user_entry.get() == username and user_pass.get() == password: 
        ctk.CTkLabel(new_window,text="YOU JUST LOST THE GAME!!").pack() 
        member.hash_with_keccak()
    elif is_valid and user_pass.get() != password and username == user_entry.get(): 
        tkmb.showwarning(title='Wrong password',message='Please check your password') 
    elif (not is_valid) and user_pass.get() == password: 
        tkmb.showwarning(title='Wrong username',message='Please check your username') 
    else: 
        tkmb.showerror(title="Login Failed",message="Invalid Username and password") 
  
  
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

button = ctk.CTkButton(master=frame,text='Signup',command=signup)
button.pack(pady=12,padx=10) 
  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 
  
  
app.mainloop()
