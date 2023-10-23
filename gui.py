import tkinter as tk

class LewiatanGUI:
    def __init__(self):
        # Tworzenie głównego okna
        self.window = tk.Tk()
        self.window.title("Wprowadź dane")
        self.window.geometry("800x400")

        # Tworzenie słownika zmiennych
        self.data_fields = {
            "first_name": tk.StringVar(),
            "last_name": tk.StringVar(),
            "birth_date": tk.StringVar(),
            "street_name": tk.StringVar(),
            "street_number": tk.StringVar(),
            "zipcode": tk.StringVar(),
            "city": tk.StringVar(),
            "phone": tk.StringVar(),
            "email": tk.StringVar()
        }

        # Tworzenie etykiet i pól wprowadzania dla każdej zmiennej
        tk.Label(self.window, text="Imię:").grid(row=0, column=0)
        self.firstname_entry = tk.Entry(self.window, textvariable=self.data_fields["first_name"])
        self.firstname_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Nazwisko:").grid(row=1, column=0)
        self.lastname_entry = tk.Entry(self.window, textvariable=self.data_fields["last_name"])
        self.lastname_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Data urodzenia:").grid(row=2, column=0)
        self.birth_date_entry = tk.Entry(self.window, textvariable=self.data_fields["birth_date"])
        self.birth_date_entry.grid(row=2, column=1)

        tk.Label(self.window, text="Ulica:").grid(row=3, column=0)
        self.street_entry = tk.Entry(self.window, textvariable=self.data_fields["street_name"])
        self.street_entry.grid(row=3, column=1)

        tk.Label(self.window, text="Numer ulicy:").grid(row=4, column=0)
        self.street_number_entry = tk.Entry(self.window, textvariable=self.data_fields["street_number"])
        self.street_number_entry.grid(row=4, column=1)

        tk.Label(self.window, text="Kod pocztowy:").grid(row=5, column=0)
        self.zipcode_entry = tk.Entry(self.window, textvariable=self.data_fields["zipcode"])
        self.zipcode_entry.grid(row=5, column=1)

        tk.Label(self.window, text="Miasto:").grid(row=6, column=0)
        self.city_entry = tk.Entry(self.window, textvariable=self.data_fields["city"])
        self.city_entry.grid(row=6, column=1)

        tk.Label(self.window, text="Numer telefonu:").grid(row=7, column=0)
        self.phone_entry = tk.Entry(self.window, textvariable=self.data_fields["phone"])
        self.phone_entry.grid(row=7, column=1)

        tk.Label(self.window, text="Adres email:").grid(row=8, column=0)
        self.email_entry = tk.Entry(self.window, textvariable=self.data_fields["email"])
        self.email_entry.grid(row=8, column=1)

        # Przyciski
        self.submit_button = tk.Button(self.window, text="Zatwierdź", command=self.submit_data)
        self.submit_button.grid(row=9, column=0, columnspan=2)

        self.save_button = tk.Button(self.window, text="Zapisz dane", command=self.save_data)
        self.save_button.grid(row=10, column=0, columnspan=2)

        # Wczytaj dane przy uruchamianiu aplikacji
        self.load_data()

    # Funkcja do zapisywania danych do pliku
    def save_data(self):
        data_to_save = {
            "first_name": self.firstname_entry.get(),
            "last_name": self.lastname_entry.get(),
            "birth_date": self.birth_date_entry.get(),
            "street_name": self.street_entry.get(),
            "street_number": self.street_number_entry.get(),
            "zipcode": self.zipcode_entry.get(),
            "city": self.city_entry.get(),
            "phone": self.phone_entry.get(),
            "email": self.email_entry.get()
        }

        with open("saved_data.txt", "w") as file:
            for key, value in data_to_save.items():
                if value != "":
                    file.write(f"{key}: {value}\n")

    # Funkcja do wczytywania danych z pliku
    def load_data(self):
        try:
            with open("saved_data.txt", "r") as file:
                data = file.readlines()
                for line in data:
                    key, value = line.strip().split(": ")
                    if key in self.data_fields:
                        self.data_fields[key].set(value)
        except FileNotFoundError:
            pass

    def submit_data(self):
        # Przypisanie wartości do zmiennych
        self.first_name = self.firstname_entry.get()
        self.last_name = self.lastname_entry.get()
        self.birth_date = self.birth_date_entry.get()
        self.street_name = self.street_entry.get()
        self.street_number_val = self.street_number_entry.get()
        self.zipcode_val = self.zipcode_entry.get()
        self.city_val = self.city_entry.get()
        self.phone_val = self.phone_entry.get()
        self.email_val = self.email_entry.get()

        # Tutaj możesz wykonać operacje na wprowadzonych danych, np. zapis do pliku lub przetwarzanie.

        # Czyszczenie pól wprowadzania po zatwierdzeniu danych
        for field in self.data_fields.values():
            field.set("")

    
# Tworzenie instancji klasy i uruchomienie głównej pętli programu tkinter
gui = LewiatanGUI()
gui.window.mainloop()
