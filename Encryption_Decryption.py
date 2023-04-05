from tkinter import *   # import the basic tkinter module for GUI building
from tkinter import filedialog   # import filedialog module to open file dialog windows
from tkinter import messagebox  # import messagebox module to display messages to the user
from tkinter import simpledialog # import simpledialog module to prompt the user for input
from tkinter import ttk  # Import ttk for themed widgets
from PIL import ImageTk, Image  # import the ImageTk and Image modules from PIL library


    
    # define a function to encrypt a given text with a given key using a shift cipher
def encrypt(text, key):
            result = ""
            for char in text:
                if char.isupper():   # if the character is uppercase
                    result += chr((ord(char) + key - 65) % 26 + 65)   # apply shift cipher to uppercase characters
                elif char.islower(): # if the character is lowercase
                    result += chr((ord(char) + key - 97) % 26 + 97)   # apply shift cipher to lowercase characters
                else:   # if the character is not a letter
                    result += char   # add the character as is
            return result   # return the encrypted text

        # define a function to decrypt a given text with a given key using a shift cipher
def decrypt(text, key):
            result = ""
            for char in text:
                if char.isupper():   # if the character is uppercase
                    result += chr((ord(char) - key - 65) % 26 + 65)   # apply reverse shift cipher to uppercase characters
                elif char.islower(): # if the character is lowercase
                    result += chr((ord(char) - key - 97) % 26 + 97)   # apply reverse shift cipher to lowercase characters
                else:   # if the character is not a letter
                    result += char   # add the character as is
            return result   # return the decrypted text

        # define a function to open a file, encrypt its contents and save it to a new file
def open_file_and_encrypt():
            # open file dialog to select a file to encrypt
            file_path = filedialog.askopenfilename()
            if file_path:   # if a file was selected
                with open(file_path, "r") as file:
                    text = file.read()  # read the contents of the file
                # ask user for encryption key
                key = simpledialog.askinteger("Encryption Key", "Enter encryption key:")  # prompt user for encryption key
                # encrypt the text using the shift cipher
                encrypted_text = encrypt(text, key)
                # show user the encryption key
                messagebox.showinfo("Encryption Key", f"The encryption key is {key}.")  # display the encryption key in a messagebox
                # open save file dialog to save the encrypted file
                save_path = filedialog.asksaveasfilename(defaultextension=".txt")   # prompt user to select a save location
                if save_path:   # if a save location was selected
                    with open(save_path, "w") as file:
                        file.write(encrypted_text)  # write the encrypted text to the file

def open_encrypted_file_and_decrypt():
            # open file dialog to select an encrypted file to decrypt
            file_path = filedialog.askopenfilename()
            if file_path:
                # ask user for encryption key
                key = simpledialog.askinteger("Encryption Key", "Enter encryption key:")  # prompt user for encryption key
                # read the encrypted text from the file
                with open(file_path, "r") as file:
                    encrypted_text = file.read()   # read the contents of the file
                # decrypt the text using the shift cipher
                decrypted_text = decrypt(encrypted_text, key)
                if decrypted_text == encrypted_text:   # if the decrypted text is same as the encrypted text, key is wrong
                    messagebox.showerror("Error", "Wrong key entered. Program will now exit.")   # display error message and exit
                    exit()
                else:
                    # show the decrypted text in a message box
                    messagebox.showinfo("Decrypted Text", decrypted_text)   # display the decrypted text in a messagebox

def encrypted_main():
            # create GUI
            encrypted_main = Tk()   # create a tkinter object
            encrypted_main.title("Encryption/Decryption File Converter")   # set title of the window
            encrypted_main.geometry("508x338")   # set dimensions of the window

            # load image and set as background
            img = Image.open("lock_background.png")   # load the image
            photo = ImageTk.PhotoImage(img)   # create a tkinter-compatible photo image
            background_label = Label(encrypted_main, image=photo)   # create a label with the image
            background_label.place(relwidth=1, relheight=1)   # set the size of the label to fill the window

            # create buttons
            style = ttk.Style()   # create a style object
            style.map('TButton', foreground=[('active', 'white')], background=[('active', '#0078d7')])   # configure the style
            encrypt_button = ttk.Button(encrypted_main, text="Encrypt File", command=open_file_and_encrypt)   # create a button for encryption
            encrypt_button.place(relx=0.8, rely=0.4, anchor=E)   # place the button on the window
            decrypt_button = ttk.Button(encrypted_main, text="Decrypt File", command=open_encrypted_file_and_decrypt)  # create a button for decryption
            decrypt_button.place(relx=0.8, rely=0.6, anchor=E)   # place the button on the window

            # run mainloop
            encrypted_main.mainloop()   # start the tkinter event loop and keep the window open

if __name__ == "__main__":
        encrypted_main()   # call the main function if the script is executed directly
