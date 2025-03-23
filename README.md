# 📞 Asterisk IVR Telecom Project

An Interactive Voice Response (IVR) system built with Asterisk to simulate a real-world telecom operator’s voice server, allowing users to:

- Check their balance in real-time
- Leave voicemail messages sent via email
- Navigate through an interactive voice menu (DTMF)
- Listen to on-hold music while being processed

---

## 🎯 Project Objectives

- ☎️ Build a real-time **Interactive Voice Response (IVR)** system
- 📩 Enable **Voicemail-to-Email with audio attachment (.wav)**
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
6. 📬 If user leaves a message, a **voicemail email is sent with a `.wav` attachment**.

---

## 💻 Setup Instructions

### Install Asterisk

```bash
sudo apt update && sudo apt install asterisk
```

### Add Your SIP Users

Edit `pjsip.conf` under `asterisk-configs/`.

### Configure Extensions

Copy `extensions.conf` into `/etc/asterisk/` and reload:

```bash
sudo asterisk -rx "dialplan reload"
```

### Setup MySQL Database

```bash
mysql -u root -p < sql/create_tables.sql
```

### Test Call

Dial from SIP softphone (Zoiper, Linphone...) to your Asterisk server.

## 📂 License

MIT License – free to use and modify.
