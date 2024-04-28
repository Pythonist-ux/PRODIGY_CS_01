import tkinter as tk
from tkinter import ttk, messagebox


def caesar_cipher(text, shift):
    """Encrypts or decrypts the given text using the Caesar Cipher algorithm."""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) %
                          26 + ascii_offset)
        else:
            result += char
    return result


def encrypt_text():
    """Encrypts the text using the Caesar Cipher."""
    text = entry_text.get("1.0", "end-1c")
    shift = int(entry_shift.get())
    encrypted_text = caesar_cipher(text, shift)
    entry_text.delete("1.0", "end")
    entry_text.insert("1.0", encrypted_text)


def decrypt_text():
    """Decrypts the text using the Caesar Cipher."""
    text = entry_text.get("1.0", "end-1c")
    shift = int(entry_shift.get())
    decrypted_text = caesar_cipher(text, -shift)
    entry_text.delete("1.0", "end")
    entry_text.insert("1.0", decrypted_text)


# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("700x500")  # Set the initial window size
root.minsize(600, 400)  # Set the minimum window size
root.configure(bg="#000000")  # Set the window background color

# Create style object
style = ttk.Style()
style.theme_use("clam")  # Set the theme

# Configure widget styles
style.configure("TLabel", background="#000000",
                foreground="#ffffff", font=("Montserrat", 12))
style.configure("TEntry", fieldbackground="#202020",
                foreground="#ffffff", font=("Montserrat", 12))
style.configure("TButton", background="#e67e22",
                foreground="#ffffff", font=("Montserrat", 12))
style.configure("TText", background="#272727",
                foreground="#ffffff", font=("Consolas", 12))
# Set readonly background color
style.map("TText", fieldbackground=[("readonly", "#272727")])

# Create widgets
label_text = ttk.Label(root, text="Enter the text:")
entry_text = tk.Text(root, height=10, width=50, bg="#272727", fg="#ffffff", font=(
    "Consolas", 12), borderwidth=0, highlightthickness=2, highlightbackground="#e67e22", highlightcolor="#e67e22")
label_shift = ttk.Label(root, text="Enter the shift value:")
entry_shift = ttk.Entry(root, style="TEntry.TEntry")
button_encrypt = ttk.Button(root, text="Encrypt", command=encrypt_text)
button_decrypt = ttk.Button(root, text="Decrypt", command=decrypt_text)

# Place widgets on the window
label_text.grid(row=0, column=0, padx=20, pady=20, sticky="w")
entry_text.grid(row=1, column=0, columnspan=3, padx=20, pady=10)
label_shift.grid(row=2, column=0, padx=20, pady=10, sticky="w")
entry_shift.grid(row=2, column=1, padx=10, pady=10)
button_encrypt.grid(row=2, column=2, padx=10, pady=10)
button_decrypt.grid(row=3, column=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
