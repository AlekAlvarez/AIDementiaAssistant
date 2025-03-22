import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PatientInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Info Form")
        self.root.geometry("500x700")

        # Set a consistent theme across platforms
        style = ttk.Style()
        style.theme_use("alt")  # You can try changing this to "clam" or "default" if issues persist

        # Label and Family Members Section
        self.family_frame = ttk.LabelFrame(root, text="Family Info", padding=(10, 5))
        self.family_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.family_listbox = tk.Listbox(self.family_frame, height=4, selectmode=tk.SINGLE)
        self.family_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.add_family_button = ttk.Button(self.family_frame, text="Add Family Member", command=self.add_family_member)
        self.add_family_button.grid(row=1, column=0, pady=5)

        # Medications Section
        self.medications_label = ttk.Label(root, text="Current Medications:")
        self.medications_label.grid(row=1, column=0, padx=10, pady=5)

        self.medications_entry = tk.Text(root, height=4, width=40)
        self.medications_entry.grid(row=2, column=0, padx=10, pady=5)

        # Hobbies Section
        self.hobbies_label = ttk.Label(root, text="Hobbies:")
        self.hobbies_label.grid(row=3, column=0, padx=10, pady=5)

        self.hobbies_entry = tk.Text(root, height=4, width=40)
        self.hobbies_entry.grid(row=4, column=0, padx=10, pady=5)

        # Language Setting Section
        self.language_label = ttk.Label(root, text="Languages Patient Speaks:")
        self.language_label.grid(row=5, column=0, padx=10, pady=5)

        self.languages = []

        self.language_var = tk.StringVar(value="Select Language")
        self.language_dropdown = ttk.OptionMenu(root, self.language_var, "Select Language")
        self.language_dropdown.grid(row=6, column=0, padx=10, pady=5)

        self.new_language_entry = ttk.Entry(root)
        self.new_language_entry.grid(row=7, column=0, padx=10, pady=5)

        self.add_language_button = ttk.Button(root, text="Add Language", command=self.add_language)
        self.add_language_button.grid(row=8, column=0, pady=5)

        # Patient Modification Request Section
        self.modification_label = ttk.Label(root, text="Patient Modification Request:")
        self.modification_label.grid(row=9, column=0, padx=10, pady=5)

        self.modification_textbox = tk.Text(root, height=5, width=40)
        self.modification_textbox.grid(row=10, column=0, padx=10, pady=5)

        # Mood Trends Section
        self.mood_label = ttk.Label(root, text="Current Mood:")
        self.mood_label.grid(row=11, column=0, padx=10, pady=5)

        self.mood_var = tk.StringVar(value="Neutral")
        self.mood_dropdown = ttk.OptionMenu(root, self.mood_var, "Disturbed", "Neutral", "Cheerful")
        self.mood_dropdown.grid(row=12, column=0, padx=10, pady=5)

        self.mood_button = ttk.Button(root, text="Set Mood", command=self.check_mood)
        self.mood_button.grid(row=13, column=0, pady=5)

        # Save Button
        self.save_button = ttk.Button(root, text="Save", command=self.save_info)
        self.save_button.grid(row=14, column=0, pady=10)

        # Force the window to update its layout and render
        self.root.update()

    def add_family_member(self):
        # Create a new family member entry
        family_member_window = tk.Toplevel(self.root)
        family_member_window.title("Add Family Member")

        tk.Label(family_member_window, text="Family Member Name:").pack(padx=10, pady=5)
        name_entry = tk.Entry(family_member_window)
        name_entry.pack(padx=10, pady=5)

        tk.Label(family_member_window, text="Alive/Dead:").pack(padx=10, pady=5)
        alive_var = tk.BooleanVar()
        tk.Checkbutton(family_member_window, text="Alive", variable=alive_var).pack(padx=10, pady=5)

        def save_family_member():
            name = name_entry.get()
            alive = "Alive" if alive_var.get() else "Dead"
            self.family_listbox.insert(tk.END, f"{name} - {alive}")
            family_member_window.destroy()

        tk.Button(family_member_window, text="Save", command=save_family_member).pack(padx=10, pady=5)

    def add_language(self):
        new_language = self.new_language_entry.get().strip()

        if new_language:  # Only add if the field is not empty
            if new_language not in self.languages:
                self.languages.append(new_language)
                self.update_language_dropdown()
                self.new_language_entry.delete(0, tk.END)  # Clear the entry box
            else:
                messagebox.showwarning("Warning", "Language already exists in the list.")
        else:
            messagebox.showwarning("Warning", "Please enter a language.")

    def update_language_dropdown(self):
        # Update the dropdown menu with the new list of languages
        self.language_var.set("Select Language")  # Reset dropdown to initial value
        self.language_dropdown['menu'].delete(0, 'end')  # Clear the old menu
        # Add the new list of languages to the dropdown
        for language in self.languages:
            self.language_dropdown['menu'].add_command(label=language, command=tk._setit(self.language_var, language))

    def check_mood(self):
        current_mood = self.mood_var.get()
        if current_mood == "Disturbed":
            messagebox.showwarning("Assistance Required", "The patient needs assistance!")

    def save_info(self):
        # Save patient info to a file or process it as needed
        family_members = "\n".join(self.family_listbox.get(0, tk.END))
        medications = self.medications_entry.get("1.0", tk.END).strip()
        hobbies = self.hobbies_entry.get("1.0", tk.END).strip()
        language = self.language_var.get()  # Get the selected language
        modification_request = self.modification_textbox.get("1.0", tk.END).strip()
        mood = self.mood_var.get()  # Get the selected mood

        with open("patient_info.txt", "w") as file:
            file.write(f"Family Members:\n{family_members}\n\n")
            file.write(f"Current Medications:\n{medications}\n\n")
            file.write(f"Hobbies:\n{hobbies}\n\n")
            file.write(f"Languages Spoken: {language}\n\n")
            file.write(f"Modification Request:\n{modification_request}\n\n")
            file.write(f"Current Mood: {mood}\n")

        messagebox.showinfo("Saved", "Patient information has been saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientInfoApp(root)
    root.mainloop()
