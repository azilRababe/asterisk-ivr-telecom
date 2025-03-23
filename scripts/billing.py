#!/usr/bin/env python3

import mysql.connector
import sys

phone_number = sys.argv[1]
call_duration = int(sys.argv[2])  # Call duration in seconds

# Define the cost per minute
cost_per_minute = 0.10  # Change as needed

# Calculate the cost
call_cost = (call_duration / 60) * cost_per_minute

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost", user="root", password="your_mysql_pass", database="telecom"
)
cursor = conn.cursor()

# Update balance
cursor.execute("UPDATE users SET balance = balance - %s WHERE phone_number = %s", (call_cost, phone_number))
conn.commit()

cursor.close()
conn.close()
