# 📞 Asterisk IVR Telecom
![Alt Text](https://github.com/azilRababe/asterisk-ivr-telecom/blob/main/asterisk_ivr.png)

An Interactive Voice Response (IVR) system built with Asterisk to simulate a real-world telecom operator’s voice server, allowing users to:

- Check their balance in real-time
- Navigate through an interactive voice menu (DTMF)
- Listen to on-hold music while being processed

---

## 🎯 Project Objectives

- ☎️ Build a real-time **Interactive Voice Response (IVR)** system
- 🎶 Configure **Music-on-Hold**
- 🗂️ Implement **DTMF Authentication** (phone number + PIN code)
- 💸 Fetch and announce **real-time balance using TTS (Text to Speech)**
- 🔐 Integrate database for user data and authentication
- 🌐 Simulate a real telecom operator’s service flow

---

## 🛠️ Tech Stack

| Component           | Technology                      |
| ------------------- | ------------------------------- |
| Telephony System    | Asterisk (PBX)                  |
| Configuration Files | extensions.conf, sip.conf, etc  |
| Audio Handling      | WAV/GSM prompts, MusicOnHold    |
| Voicemail Delivery  | Bash/Sendmail/Postfix           |
| Database            | MySQL / MariaDB                 |
| TTS Engine          | Google TTS / Festival / PicoTTS |
| Web Frontend (demo) | HTML/CSS/JS or React (optional) |
| SIP Web Dialer      | JsSIP / SIP.js (optional)       |

---

---

## ⚙️ How It Works

1. 📞 Caller dials a **Direct Inward Dialing (DID)** number.
2. 🎙 IVR prompts the user to enter their **phone number + secret PIN** using **DTMF**.
3. ✅ User is authenticated via a MySQL database.
4. 💰 Balance is fetched and read aloud using **TTS**.
5. 🎶 Music plays during wait time.

---

## 💻 Setup Instructions

### Install Asterisk

For detailed installation instructions, please refer to the official Asterisk website:  
[Asterisk Installation Guide](https://wiki.asterisk.org/wiki/display/AST/Installing+Asterisk)

To install Asterisk on your system, run the following command:

```bash
sudo apt update && sudo apt install asterisk
```

### Add Your SIP Users
Edit `pjsip.conf` under `asterisk-configs/`

### Configure Extensions
Copy `extensions.conf` into `/etc/asterisk/` and reload Asterisk:
```bash
sudo asterisk -rx "dialplan reload"
```

## Setup MySQL Database
For MySQL installation and setup, please follow the official MySQL documentation:
`MySQL Installation Guide`

Once MySQL is installed, run the following command to access the MySQL shell:

```bash
mysql -u root -p 
```

### Test Call

Dial from SIP softphone (Zoiper, Linphone...) to your Asterisk server.

## 📁 Important Paths and Resources

- `sudo nano /etc/odbc.ini` – MySQL connection configuration
- `sudo nano /etc/asterisk/res_odbc.conf` – `[asterisk]` MySQL connection settings
- `/var/lib/asterisk/agi-bin/` – Directory for AGI scripts
- `/var/lib/asterisk/sounds/` – Directory for sound files
- `/var/lib/asterisk/agi-bin/check_balance.py` – AGI script for balance checking
- `nano /etc/asterisk` – Asterisk configuration files
- `/usr/src/asterisk/asterisk-22.2.0` – Asterisk source code
- [Asterisk Google TTS](https://github.com/zaf/asterisk-googletts) – Google TTS integration
- `/var/log/asterisk/cdr-csv/Master.csv` – Call Detail Record (CDR) logs

## 📂 License

MIT License – free to use and modify.
