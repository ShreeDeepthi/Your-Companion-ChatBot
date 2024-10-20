import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk, Image, ImageFilter
#Hey User before you take a look
#This is a simple chatbot that can answer some basic questions and can help you lift up your mood but not much complex ones as this is still in working 

def send_message(event=None):
    user_message = entry_text.get().strip()
    if user_message:
        add_user_message(user_message)
        entry_text.set('')
        respond(user_message)

def add_user_message(message):
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {message}\n")
    chat_area.yview(tk.END)
    chat_area.config(state='disabled')

def add_bot_message(message):
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"Bot: {message}\n")
    chat_area.yview(tk.END)
    chat_area.config(state='disabled')

def respond(message):
    message = message.lower()
    if "sad" in message or "not ok" in message or "depressed" in message:
        response = "I'm sorry to hear that. It's okay to feel sad sometimes. Do you want to talk about it?"
    elif "happy" in message or "good" in message or "okay" in message:
        response = "That's great to hear! What made you feel this way?"
    elif "hello" in message or "hi" in message:
        response = "Hello! How can I help you today?"
    elif "joke" in message or "laugh" in message:
        response = "Here's a joke I told my computer I needed a break, and now it won't stop sending me KitKat ads."
    elif "thanks" in message:
        response = "Always rooting for you have a smile on your face!<3 "
    elif "motivation" in message:
        response = "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."
    elif "jokes" in message:
        response = "Want to hear a joke about construction? I'm still working on it."
    elif "bye" in message or "talk later" in message:
        response = "Good day!!!"
    else:
        response = "I'm here to listen. What's on your mind?"

    add_bot_message(response)

root = tk.Tk()
root.title("Your Companion")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='disabled')
chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry_text = tk.StringVar()
entry_box = tk.Entry(root, textvariable=entry_text, width=40)
entry_box.grid(row=1, column=0, padx=10, pady=10)
entry_box.bind('<Return>', send_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

add_bot_message("Hello! I'm here to chat with you. How are you feeling today?")
add_bot_message("I was designed by Deepthi to make your day better!")
robot_image = Image.open("robot.png")  # Change "robot.png" to the filename of your robot image
robot_image = robot_image.resize((350, 350))
robot_photo = ImageTk.PhotoImage(robot_image)
robot_label = tk.Label(root, image=robot_photo)
robot_label.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

root.mainloop()

