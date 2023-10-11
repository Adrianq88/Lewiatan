import tkinter as tk

def submit_data():
    user_input = entry.get()
    result_label.config(text="Wprowadzone dane: " + user_input)

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Pobieranie danych od użytkownika")

# Tworzenie etykiety
label = tk.Label(root, text="Wprowadź dane:")
label.pack()

# Tworzenie pola do wprowadzania tekstu
entry = tk.Entry(root)
entry.pack()

# Tworzenie przycisku
submit_button = tk.Button(root, text="Potwierdź", command=submit_data)
submit_button.pack()

# Tworzenie etykiety wynikowej
result_label = tk.Label(root, text="")
result_label.pack()

# Rozpoczęcie głównej pętli GUI
root.mainloop()
