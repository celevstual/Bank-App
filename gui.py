import tkinter as tk
from PIL import ImageTk, Image

FOCUS_IN = '<FocusIn>'
FOCUS_OUT = '<FocusOut>'

USER_PASSWORD_PLACEHOLDER = "Password"
ADMIN_PASSWORD_PLACEHOLDER = "Password"
USERNAME_PLACEHOLDER = "Username or Access Card"

def toggle_user_password():
    if userPasswordEntry.get() != USER_PASSWORD_PLACEHOLDER:
        if userPasswordEntry.cget('show') == '':
            userPasswordEntry.config(show='●')
            eyeButton2.config(image=closeeye_image)
        else:
            userPasswordEntry.config(show='')
            eyeButton2.config(image=openeye_image)

def toggle_admin_password():
    if adminPasswordEntry.get() != ADMIN_PASSWORD_PLACEHOLDER:
        if adminPasswordEntry.cget('show') == '':
            adminPasswordEntry.config(show='●')
            eyeButton1.config(image=closeeye_image)
        else:
            adminPasswordEntry.config(show='')
            eyeButton1.config(image=openeye_image)

def on_enter_username(event):
    if usernameEntry.get() == USERNAME_PLACEHOLDER:
        usernameEntry.delete(0, tk.END)

def on_leave_username(event):
    if usernameEntry.get() == "":
        usernameEntry.insert(0, USERNAME_PLACEHOLDER)

def on_enter_admin_password(event):
    if adminPasswordEntry.get() == ADMIN_PASSWORD_PLACEHOLDER:
        adminPasswordEntry.delete(0, tk.END)
        adminPasswordEntry.config(show='●')
        eyeButton1.config(image=closeeye_image)

def on_leave_admin_password(event):
    if adminPasswordEntry.get() == "":
        adminPasswordEntry.insert(0, ADMIN_PASSWORD_PLACEHOLDER)
        adminPasswordEntry.config(show='')
        eyeButton1.config(image=openeye_image)

def on_enter_user_password(event):
    if userPasswordEntry.get() == USER_PASSWORD_PLACEHOLDER:
        userPasswordEntry.delete(0, tk.END)
        userPasswordEntry.config(show='●')
        eyeButton2.config(image=closeeye_image)

def on_leave_user_password(event):
    if userPasswordEntry.get() == "":
        userPasswordEntry.insert(0, USER_PASSWORD_PLACEHOLDER)
        userPasswordEntry.config(show='')
        eyeButton2.config(image=openeye_image)

# Create the main window
main_window = tk.Tk()
main_window.title("My Bank Account")

# Calculate the new dimensions while maintaining the aspect ratio
original_width = 2154
original_height = 1442
new_width = 1100
window_width = new_width 
new_height = int((original_height / original_width) * new_width) 

main_window.geometry(f"{new_width}x{new_height}")

# Center the window on the screen
window_width = new_width
window_height = new_height
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2) 
main_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Lock the window size
main_window.resizable(False, False)

# Load the icon image
# icon_image = ImageTk.PhotoImage(file="images/icon.png")
# main_window.iconphoto(False, icon_image)

# Open the background image file
bgImage = Image.open("images/bg.png")

# Resize the background image to fit the window
bgImage = bgImage.resize((new_width, new_height), Image.LANCZOS) 

# Convert the background image to PhotoImage
bgImage = ImageTk.PhotoImage(bgImage)

# Add the background image to the canvas
canvas = tk.Canvas(width=new_width, height=new_height, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)

# Add the loginbutton image with new dimensions
loginbutton_image = Image.open('images/loginbutton.png')
loginbutton_image = loginbutton_image.resize((new_width, new_height), Image.LANCZOS)
loginbutton_image = ImageTk.PhotoImage(loginbutton_image)

canvas.create_image(new_width // 2, new_height // 2, image=loginbutton_image)

# Add the openeye image
openeye_image = Image.open('images/openeye.png')
openeye_image = openeye_image.resize((20, 20), Image.LANCZOS)
openeye_image = ImageTk.PhotoImage(openeye_image)

# Add the closeeye image
closeeye_image = Image.open('images/closeeye.png')
closeeye_image = closeeye_image.resize((20, 20), Image.LANCZOS)
closeeye_image = ImageTk.PhotoImage(closeeye_image)

# Add a custom font to the heading
heading_font = ("Sitka Heading Semibold", 23, "bold")
heading = tk.Label(canvas, text="Login", font=heading_font, bg="#425515", fg="white")
heading.place(x=735, y=170)  

# Create the admin password label
adminPasswordLabel = tk.Label(canvas, text="Admin Password", font=(heading_font, 13), fg='white', bg='#425515')
adminPasswordLabel.place(x=735, y=220)  

# Create the admin password entry
adminPasswordEntry = tk.Entry(canvas, width=25, font=(heading_font, 13), fg='grey', bg='#1A2405', highlightthickness=0, bd=0)
adminPasswordEntry.place(x=737, y=257) 
adminPasswordEntry.insert(0, ADMIN_PASSWORD_PLACEHOLDER)
adminPasswordEntry.bind(FOCUS_IN, on_enter_admin_password)
adminPasswordEntry.bind(FOCUS_OUT, on_leave_admin_password)

# Create frames 
frame1 = tk.Frame(canvas, width=230, height=2, bg='white') 
frame1.place(x=737, y=300) 

heading = tk.Label(canvas, text="or", font=(heading_font, 10, "bold"), fg='white', bg='#425515') 
heading.place(x=845, y=288)

# Create the username label
usernameLabel = tk.Label(canvas, text="Username or Access Card", font=(heading_font, 13), fg='white', bg='#435615')
usernameLabel.place(x=736, y=317) 

# Create the username entry
usernameEntry = tk.Entry(canvas, width=25, font=(heading_font, 13), fg='grey', bg='#1A2405', highlightthickness=0, bd=0)
usernameEntry.place(x=736, y=349) 
usernameEntry.insert(0, USERNAME_PLACEHOLDER)
usernameEntry.bind(FOCUS_IN, on_enter_username)
usernameEntry.bind(FOCUS_OUT, on_leave_username)

# Create the user password label
userPasswordLabel = tk.Label(canvas, text="User Password", font=(heading_font, 13), fg='white', bg='#435615')
userPasswordLabel.place(x=736, y=380)

# Create the user password entry
userPasswordEntry = tk.Entry(canvas, width=25, font=(heading_font, 13), fg='grey', bg='#1A2405', highlightthickness=0, bd=0)
userPasswordEntry.place(x=738, y=413)  
userPasswordEntry.insert(0, USER_PASSWORD_PLACEHOLDER)
userPasswordEntry.bind(FOCUS_IN, on_enter_user_password)
userPasswordEntry.bind(FOCUS_OUT, on_leave_user_password)

# Define the login button
loginButton = tk.Button(canvas, text='LOGIN', font=(heading_font, 13, 'bold'), bg='#769722', fg='white', bd=0, cursor='hand2', width=21, activebackground='#769722', activeforeground='white')
loginButton.place(x=744, y=481)  

# Create the buttons 
forgetButton = tk.Button(canvas, text="Forgot Password?", font=(heading_font, 10, 'bold', 'underline'), bd=0, fg='#779823', bg='#425515', activebackground='#425515', activeforeground='white', cursor='hand2') 
forgetButton.place(x=845, y=442) 

eyeButton1 = tk.Button(canvas, image=openeye_image, bd=0, bg='#1A2405', activebackground='#1A2405', cursor='hand2', command=toggle_admin_password) 
eyeButton1.place(x=940, y=257)

eyeButton2 = tk.Button(canvas, image=openeye_image, bd=0, bg='#1A2405', activebackground='#1A2405', cursor='hand2', command=toggle_user_password) 
eyeButton2.place(x=940, y=413) 

main_window.mainloop()