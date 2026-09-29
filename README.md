# NetScan 🔍

NetScan is a Python-based network and port scanning tool designed for learning about network discovery and basic security testing.

> **⚠️ Important:** Use NetScan only on networks, devices, and systems that you own or have explicit permission to test.

---

## ✨ Features

* 🔎 Network scanning
* 🚪 Port scanning
* 🌐 Host discovery
* ⚡ Simple command-line interface
* 🐍 Written in Python
* 💻 Works from PowerShell, Command Prompt, or Linux terminal

---

## 📋 Requirements

Before installing NetScan, make sure you have:

* Python 3.10 or newer
* Git
* An internet/network connection for network scanning
* Permission to scan the target system

Check your Python installation:

```bash
python --version
```

Check Git:

```bash
git --version
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/eliortalderson-lgtm/NetScan.git
```

### 2. Enter the project directory

```bash
cd NetScan
```

### 3. Check the files

```bash
dir
```

On Linux/macOS:

```bash
ls
```

You should see:

```text
netscan.py
README.md
```

---

## ▶️ Running NetScan

Run the program with:

```bash
python netscan.py
```

Follow the instructions displayed by the program.

If your system uses `python3`, use:

```bash
python3 netscan.py
```

---

## 🔍 Network Scanning

NetScan can be used to discover hosts on a network, depending on the functionality implemented in `netscan.py`.

Only provide network ranges that you are authorized to scan.

Example:

```text
Enter target network:
192.168.1.0/24
```

---

## 🚪 Port Scanning

NetScan can also be used to check ports on an authorized target.

Example:

```text
Enter target:
192.168.1.10

Enter port:
80
```

For a range of ports, use the format supported by the program.

Example:

```text
80-443
```

> The exact commands and inputs depend on the current implementation of `netscan.py`.

---

## 🧪 Example Workflow

A typical workflow is:

```powershell
git clone https://github.com/eliortalderson-lgtm/NetScan.git
cd NetScan
python netscan.py
```

Then enter a target that you are authorized to test.

---

## 🛠️ Troubleshooting

### Python is not recognized

If you see:

```text
'python' is not recognized as an internal or external command
```

Install Python and make sure **Add Python to PATH** is enabled during installation.

Then restart PowerShell and run:

```powershell
python --version
```

---

### Git is not recognized

If you see:

```text
'git' is not recognized as the name of a cmdlet
```

Install Git and make sure Git is added to your system PATH.

Then restart PowerShell:

```powershell
git --version
```

---

### Permission denied

Some operating systems or networks may restrict certain network operations.

Make sure:

* You have permission to scan the target.
* Your firewall is not blocking the program.
* You are using the correct target address.

---

## 📁 Project Structure

```text
NetScan/
│
├── netscan.py
└── README.md
```

---

## 🔄 Updating NetScan

If you cloned the repository and want the latest version:

```bash
cd NetScan
git pull
```

Then run:

```bash
python netscan.py
```

---

## 🔐 Responsible Use

NetScan is intended for:

* Learning network security
* Testing your own devices
* Testing your own network
* Authorized penetration-testing labs
* Educational cybersecurity environments

Do **not** scan systems or networks without authorization.

The author is not responsible for misuse of this tool.

---

## 📜 License

Add your preferred open-source license before publishing the project.

---

## 👨‍💻 Author

Created by **eliortalderson-lgtm**

GitHub:

https://github.com/eliortalderson-lgtm

---

⭐ If you find NetScan useful for learning, consider starring the repository.
