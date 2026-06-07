# K-Password Manager 🔐🛡️

A modern, Python-based desktop application that combines a Cryptographically Secure Password Generator with a robust Password Strength Checker. Built with a sleek, minimalist UI utilizing CustomTkinter.

### 🎯 Objective
This project was developed to practice modular Python architecture (separating backend logic from the frontend UI) while building practical utilities relevant to Blue Team and SOC operations. It emphasizes secure coding practices, such as replacing standard pseudo-random generators with the cryptographically secure `secrets` module.

### ⚙️ Features
* **Modern GUI:** Clean, minimalist interface with automatic Dark/Light mode detection (fully compatible with macOS/Silicon environments).
* **Secure Generator:** Creates strong, customizable passwords using the `secrets` module to prevent predictability attacks.
* **Policy Checker:** Validates user passwords against common corporate security policies with real-time visual feedback.
* **Modular Codebase:** The core validation and generation engines are strictly separated from the GUI wrapper for easier maintenance.

### 🗺️ Roadmap (Work In Progress)
- [x] Establish core generation and validation logic.
- [x] Design minimal UI framework.
- [ ] Connect GUI inputs to backend engines.
- [ ] Implement local SQLite vault for secure credential storage.
- [ ] Add multi-language support (Settings Tab).

### 🚀 How to Run

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Install the required UI library:
   ```bash
   pip3 install customtkinter
   ```
4. Run the main application file from your terminal:
   ```bash
   python3 gui_app.py
   ```
