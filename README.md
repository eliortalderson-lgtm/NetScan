# NetScan 🔍

NetScan is a Python-based network and port scanning tool with a graphical interface built using CustomTkinter.

> ⚠️ **Important:** Use NetScan only on systems and networks that you own or have explicit permission to test.

## ✨ Features

* 🔎 Network scanning
* 🚪 Port scanning
* 🖥️ Graphical user interface
* 🐍 Python-based
* 💻 Works on Linux and Windows

---

## 📋 Requirements

* Python 3.10 or newer
* Git
* Permission to scan the target system

Check Python:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

---

# 📥 Installation on Kali Linux

### 1. Clone the repository

```bash
git clone https://github.com/eliortalderson-lgtm/NetScan.git
```

### 2. Enter the project directory

```bash
cd NetScan
```

### 3. Install Python virtual-environment support

Kali Linux protects its system Python environment. Therefore, NetScan should be installed inside a virtual environment.

Run:

```bash
sudo apt update
sudo apt install python3-venv -y
```

### 4. Create a virtual environment

```bash
python3 -m venv .venv
```

### 5. Activate the virtual environment

```bash
source .venv/bin/activate
```

After activation, your terminal should show `(.venv)` before the prompt.

For example:

```text
(.venv) kali@kali:~/NetScan$
```

### 6. Install NetScan dependencies

Install CustomTkinter:

```bash
pip install customtkinter
```

### 7. Run NetScan

```bash
python netscan.py
```

---

# 🪟 Installation on Windows

Open PowerShell and clone the repository:

```powershell
git clone https://github.com/eliortalderson-lgtm/NetScan.git
```

Enter the directory:

```powershell
cd NetScan
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install CustomTkinter:

```powershell
pip install customtkinter
```

Run NetScan:

```powershell
python netscan.py
```

---

# ▶️ Running NetScan

## Kali Linux

Activate the virtual environment:

```bash
cd ~/NetScan
source .venv/bin/activate
```

Then:

```bash
python netscan.py
```

## Windows

Activate the virtual environment:

```powershell
cd NetScan
.venv\Scripts\Activate.ps1
```

Then:

```powershell
python netscan.py
```

---

# 📦 Dependencies

NetScan currently requires:

```text
customtkinter
```

You can install the dependency manually with:

```bash
pip install customtkinter
```

A `requirements.txt` file can also be used for easier installation.

---

# 🛠️ Troubleshooting

## `ModuleNotFoundError: No module named 'customtkinter'`

Make sure your virtual environment is activated.

Kali Linux:

```bash
source .venv/bin/activate
```

Then install the dependency:

```bash
pip install customtkinter
```

Run:

```bash
python netscan.py
```

---

## `externally-managed-environment`

If you see:

```text
error: externally-managed-environment
```

Do **not** install packages directly into Kali's system Python.

Instead, create and activate a virtual environment:

```bash
sudo apt install python3-venv -y
python3 -m venv .venv
source .venv/bin/activate
pip install customtkinter
```

Then run:

```bash
python netscan.py
```

---

## `python` command not found

Try:

```bash
python3 --version
```

On Kali Linux, use:

```bash
python3 netscan.py
```

after activating the virtual environment.

---

## Git is not installed

Install Git on Kali:

```bash
sudo apt update
sudo apt install git -y
```

Check:

```bash
git --version
```

---

# 📁 Project Structure

```text
NetScan/
│
├── netscan.py
├── README.md
└── .venv/
```

> `.venv/` is a local virtual environment and should **not** be uploaded to GitHub.

Add `.venv/` to `.gitignore`:

```text
.venv/
__pycache__/
*.pyc
```

---

# 🔐 Responsible Use

NetScan is intended for:

* Learning network security
* Testing your own devices
* Testing your own network
* Authorized security testing
* Educational cybersecurity labs

Do not scan systems or networks without authorization.

The author is not responsible for misuse of this tool.

---

# 🔄 Updating NetScan

To update the project:

```bash
git pull
```

If you are using Kali, activate the virtual environment afterward if necessary:

```bash
source .venv/bin/activate
```

Then run:

```bash
python netscan.py
```

---

# 👨‍💻 Author

Created by **eliortalderson-lgtm**

GitHub:

https://github.com/eliortalderson-lgtm

---

⭐ If you find NetScan useful for learning, consider starring the repository.
