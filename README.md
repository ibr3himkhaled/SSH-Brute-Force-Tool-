🔐 SSH Brute Force Tool (Python + Paramiko)
A simple yet powerful Python tool to test SSH login security using brute force attacks.
Use responsibly and only on systems you own or have permission to test!

🚀 Features
✔ Brute force SSH logins with username/password combinations
✔ Proxy support (SOCKS5/HTTP) for anonymity (e.g., Tor)
✔ Random delays between attempts to avoid detection
✔ Error handling & logging for debugging
✔ Lightweight & easy to modify

⚙️ Installation & Requirements
📋 Requirements
Python 3.6+
paramiko (SSH library)
(Optional) pysocks (for proxy support)

🔧 Setup
pip install paramiko pysocks

💻 How to Use
1️⃣ Basic Usage
Edit the creds list in the script and run:
python ssh_brute.py

Example Output:
[+] Success! Logged in as admin:password123
[-] Failed: root:toor
[-] All attempts completed.

2️⃣ Using a Proxy (Tor, SOCKS5, etc.)
proxy = "socks5://127.0.0.1:9050"  # Tor default proxy
success, user, pwd = try_ssh_login(target, creds, proxy=proxy)

3️⃣ Reading Credentials from a File
with open("passwords.txt", "r") as f:
    creds = [(user.strip(), pwd.strip()) for user, pwd in (line.split(":") for line in f]
    
🛡️ Ethical & Legal Warning
⚠ This tool is for educational and authorized security testing only.
⚠ Unauthorized use against systems you don’t own is illegal.
⚠ Always get permission before testing any network.

🔧 Customization & Improvements
Add threading for faster attacks (but be cautious of rate-limiting).
Integrate with password lists (e.g., rockyou.txt).
Enhance logging (save results to a file).

📜 License
MIT License - Free for ethical use.
