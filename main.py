from tkinter import *
from tkinter import messagebox
import base64

window=Tk()
window.minsize(width=300,height=600)
window.config(bg="lightblue")
FONT=("calibri", 20, "bold")

img = PhotoImage(file="top_secret.png")
panel = Label(window, image=img,bg="lightblue")
panel.grid(row=0,column=2)


#NoteTitle
note_title=Label(text="Enter your Title ",font=FONT, bg="lightblue")
note_title.grid(row=1,column=2)

note_title_entry=Entry(width=40)
note_title_entry.grid(row=2,column=2)

#NoteText
note_text=Label(text="Notunuzu giriniz: ",font=FONT, bg="lightblue")
note_text.grid(row=3,column=2)

note_text_entry=Text(width=30,height=10)
note_text_entry.grid(row=4,column=2)

#master_key
master_key_label=Label(text="Enter Master Key", bg="lightblue",font=FONT)
master_key_label.grid(row=5,column=2)
master_key=Entry(width=20)
master_key.grid(row=6,column=2)

def Store():
    if note_text_entry.get(0.,"end")==" " or note_title_entry.get()=="":
        messagebox.showwarning("showwarning", "Başlık veya İçerik girilmedi")
    else:
        with open("notes.txt", "a") as notes:
            notes.write(note_title_entry.get() + "\n")
            notes.write(encode(master_key.get(),note_text_entry.get(1.,"end"))+ "\n")
            messagebox.showinfo("showinfo", "bilgi kaydedildi")
            note_text_entry.delete(1., 'end')
            note_title_entry.delete(0)



# Function to encode
def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode
def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)

def decrypt():
    decrypted_message=decode(master_key.get(),note_text_entry.get(1.0,'end'))
    note_text_entry.delete(1., 'end')
    note_text_entry.insert(1.,decrypted_message)



#buton
Encrypt_btn=Button(text="Save and Encrypt", width=20, command=Store)
Encrypt_btn.grid(row=7,column=2)
Decrpt_btn=Button(text="Decrypt", width=20, command=decrypt)
Decrpt_btn.grid(row=8,column=2)


window.mainloop()