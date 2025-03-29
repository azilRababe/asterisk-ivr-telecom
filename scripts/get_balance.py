#!/usr/bin/env python3

import sys
import mysql.connector

def get_balance(phone, pin):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password", # Replace with your MySQL root password
            database="asterisk" # Replace with your database name
        )
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE phone=%s AND pin=%s", (phone, pin))
        result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
        print(f"Database error: {err}", file=sys.stderr)
        return None
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: get_balance.py <phone> <pin>", file=sys.stderr)
        sys.exit(1)

    phone = sys.argv[1]
    pin = sys.argv[2]
    balance = get_balance(phone, pin)
    
    if balance is not None:
        # Output the balance in a format Asterisk can read
        print(f"SET VARIABLE balance {balance}")
    else:
        # Output 0 if no balance is found or an error occurs
        print("SET VARIABLE balance 0")