#!/usr/bin/env python3

import sys
import mysql.connector
from gtts import gTTS
import os

agi_vars = {}
for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    key, value = line.split(':', 1)
    agi_vars[key.strip()] = value.strip()

args = sys.argv
phone = args[1]
pin = args[2]

conn = mysql.connector.connect(
    host="localhost", user="root", password="your_mysql_pass", database="telecom"
)
cursor = conn.cursor()
cursor.execute("SELECT balance FROM users WHERE phone_number=%s AND pin_code=%s", (phone, pin))
result = cursor.fetchone()

if result:
    balance = float(result[0])
    tts_text = f"Bonjour. Votre solde est de {balance} dirhams."
    tts = gTTS(tts_text, lang='fr')
    tts.save("/var/lib/asterisk/sounds/user_balance.wav")
    print("STREAM FILE user_balance \"\"")
else:
    print("STREAM FILE invalid \"\"")
