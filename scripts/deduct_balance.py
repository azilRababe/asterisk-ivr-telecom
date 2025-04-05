#!/usr/bin/env python3

import sys
import mysql.connector

def main():
    phone = sys.argv[1] 
    duration = int(sys.argv[2]) 

    cost_per_second = 0.01  
    total_cost = duration * cost_per_second

    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password', # Replace with your MySQL root password
            database='asterisk' # Replace with your database name
        )
        cursor = conn.cursor()

        # Step 3: Update balance
        cursor.execute("SELECT balance FROM users WHERE phone = %s", (phone,))
        result = cursor.fetchone()

        if result:
            current_balance = float(result[0])
            new_balance = max(current_balance - total_cost, 0.00)  
            cursor.execute("UPDATE users SET balance = %s WHERE phone = %s", (new_balance, phone))
            conn.commit()
            print(f"VERBOSE \"Balance updated: {current_balance} -> {new_balance}\" 1")
        else:
            print(f"VERBOSE \"Phone number {phone} not found in DB.\" 1")

    except Exception as e:
        print(f"VERBOSE \"Error: {str(e)}\" 1")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
