import tkinter as tk

def btn_click(event):
    try:
        text = event.widget.cget("text")

        if text == "=":
            try:
                result = eval(screen.get())  # Mat
                screen.set(result)
            except Exception:
                screen.set("Hata")
        elif text == "C":
            screen.set("")  # temizle
        elif text == "<":
            current = screen.get()
            screen.set(current[:-1])  # sonuncuyu sil
        else:
            screen.set(screen.get() + text)  # tıklananı ekle
    except Exception:
        screen.set("Hata")

# GUI
root = tk.Tk()
root.title("Hesap Makinesi")
root.configure(bg="#f9f3f3") #arkaplan
root.geometry("350x500")  #pencere

# Ekran Alanı
screen = tk.StringVar()
screen.set("")
entry = tk.Entry(root, textvar=screen, font=("Comic Sans MS", 20, "bold"), justify="right", fg="#5c5a59", bg="#fde9e9", relief="flat", bd=5)
entry.pack(fill="both", ipadx=8, ipady=10, padx=10, pady=10)

# Buton
button_style = {
    "font": ("Comic Sans MS", 15, "bold"),
    "height": 2,
    "width": 4,
    "relief": "flat",  #görünüm
    "bd": 0,
    "bg": "#ffd1dc",  #buton rengi
    "fg": "#5c5a59",  #yazı rengi
    "activebackground": "#ffb6c1",  # tıklanınca
    "activeforeground": "#ffffff"
}


button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["<"]
]

#buton
for i, row in enumerate(button_texts):
    frame = tk.Frame(root, bg="#f9f3f3")  # Arka plan rengi uyumu
    frame.pack()
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, **button_style)
        button.pack(side="left", padx=8, pady=8)
        button.bind("<Button>", btn_click)  # buton fonk

#başlat
root.mainloop()
