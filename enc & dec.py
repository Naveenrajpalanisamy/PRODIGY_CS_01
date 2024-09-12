import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift_amount) % 26
            encrypted_text.append(chr(start + offset))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start - shift_amount) % 26
            decrypted_text.append(chr(start + offset))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def encrypt_message():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift value.")
        return

    encrypted_message = encrypt(message, shift)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, encrypted_message)

def decrypt_message():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift value.")
        return

    decrypted_message = decrypt(message, shift)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, decrypted_message)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place the widgets
tk.Label(root, text="Enter your message:").grid(row=0, column=0, padx=10, pady=5)
entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the shift value:").grid(row=1, column=0, padx=10, pady=5)
entry_shift = tk.Entry(root, width=50)
entry_shift.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Encrypt", command=encrypt_message).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Decrypt", command=decrypt_message).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=5)
entry_result = tk.Entry(root, width=50)
entry_result.grid(row=3, column=1, padx=10, pady=5)

# Run the application
root.mainloop()
