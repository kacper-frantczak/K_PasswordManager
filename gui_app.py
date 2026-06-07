import customtkinter as ctk
from generator_engine import Generator
from checker_engine import analyze_password

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class PasswordManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("K-Password Manager")
        self.geometry("600x400")
        self.resizable(False, False)

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=20, pady=10, fill="both", expand=True)

        self.tab_generator = self.tabview.add("Password Generator")
        self.tab_checker = self.tabview.add("Password Checker")
        self.tab_account = self.tabview.add("Account")

        self.setup_generator_tab()
        #self.setup_checker_tab()
        #self.setup_account_tab()

    def setup_generator_tab(self):
        params_frame = ctk.CTkFrame(self.tab_generator, fg_color="transparent")
        params_frame.pack(pady=(10,5), fill="x", padx=20)

        ctk.CTkLabel(params_frame, text="Password Length:", font=("Helvetica", 14)).grid(row=0, column=0, padx=(0,10), sticky="w")
        self.length_entry = ctk.CTkEntry(params_frame, width=60, justify="center")
        self.length_entry.insert(0, "16")
        self.length_entry.grid(row=0, column=1, sticky="w")

        options_frame = ctk.CTkFrame(self.tab_generator, fg_color="transparent")
        options_frame.pack(pady=10, fill="x", padx=20)

        self.check_uppercase = ctk.CTkCheckBox(options_frame, text="Include Uppercase", font=("Helvetica", 14))
        self.check_uppercase.select()
        self.check_uppercase.pack(side="left", padx=(0,15))

        self.check_digits = ctk.CTkCheckBox(options_frame, text="Include Digits", font=("Helvetica", 14))
        self.check_digits.select()
        self.check_digits.pack(side="left", padx=15)

        self.check_special = ctk.CTkCheckBox(options_frame, text="Include Special Characters", font=("Helvetica", 14))
        self.check_special.select()
        self.check_special.pack(side="left", padx=15)

        #self.btn_generate = ctk.CTkButton(self.tab_generator, text="Generate Password", font=("Helvetica", 14), command=self.generate_password) 
        #self.btn_generate.pack(pady=20)

        self.result_entry = ctk.CTkEntry(self.tab_generator, width=400, font=("Helvetica", 14, "bold"), justify="center", height=45)
        self.result_entry.pack(pady=10, padx=20, fill="x")

        save_frame = ctk.CTkFrame(self.tab_generator)
        save_frame.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(save_frame, text="Save Password As:", font=("Helvetica", 14)).pack(pady=(15,5))

        self.app_name_entry = ctk.CTkEntry(save_frame, placeholder_text="URL or App Name", font=("Helvetica", 14))
        self.app_name_entry.pack(pady=(5,15))

if __name__ == "__main__":
    app = PasswordManagerApp()
    app.mainloop()