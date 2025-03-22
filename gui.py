import tkinter as tk
from tkinter import messagebox

class PatientInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Info Form")
        self.root.geometry("500x700")

        # Label and Family Members Section
        self.family_frame = tk.LabelFrame(root, text="Family Info", padx=10, pady=10)
        self.family_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.family_listbox = tk.Listbox(self.family_frame, height=4, selectmode=tk.SINGLE)
        self.family_listbox.pack(padx=10, pady=5, fill="both")
        self.add_family_button = tk.Button(self.family_frame, text="Add Family Member", command=self.add_family_member)
        self.add_family_button.pack(pady=5)

        # Medications
        self.medications_label = tk.Label(root, text="Current Medications:")
        self.medications_label.pack(padx=10, pady=5)
        self.medications_entry = tk.Text(root, height=4, width=40)
        self.medications_entry.pack(padx=10, pady=5)

        # Hobbies
        self.hobbies_label = tk.Label(root, text="Hobbies:")
        self.hobbies_label.pack(padx=10, pady=5)
        self.hobbies_entry = tk.Text(root, height=4, width=40)
        self.hobbies_entry.pack(padx=10, pady=5)

        # Language Setting Section
        self.language_label = tk.Label(root, text="Languages Patient Speaks:")
        self.language_label.pack(padx=10, pady=5)

        # Empty list of languages initially
        self.languages = []

        # Create the dropdown menu (start with an initial value)
        self.language_var = tk.StringVar(value="Select Language")  # Default value
        self.language_dropdown = tk.OptionMenu(root, self.language_var, "Select Language")
        self.language_dropdown.pack(padx=10, pady=5)

        # Input to add new language
        self.new_language_entry = tk.Entry(root)
        self.new_language_entry.pack(padx=10, pady=5)

        self.add_language_button = tk.Button(root, text="Add Language", command=self.add_language)
        self.add_language_button.pack(pady=5)

        # Patient Modification Request Section
        self.modification_label = tk.Label(root, text="Patient Modification Request:")
        self.modification_label.pack(padx=10, pady=5)

        self.modification_textbox = tk.Text(root, height=5, width=40)
        self.modification_textbox.pack(padx=10, pady=5)

        # Mood Trends Section
        self.mood_label = tk.Label(root, text="Current Mood:")
        self.mood_label.pack(padx=10, pady=5)

        self.mood_var = tk.StringVar(value="Neutral")  # Default value
        self.mood_dropdown = tk.OptionMenu(root, self.mood_var, "Disturbed", "Neutral", "Cheerful")
        self.mood_dropdown.pack(padx=10, pady=5)

        self.mood_button = tk.Button(root, text="Set Mood", command=self.check_mood)
        self.mood_button.pack(pady=5)

        # Save Button
        self.save_button = tk.Button(root, text="Save", command=self.save_info)
        self.save_button.pack(pady=10)

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
