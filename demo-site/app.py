from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def update_balance(phone, amount):
    conn = mysql.connector.connect(host="localhost", user="root", password="your_mysql_pass", database="telecom")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance + %s WHERE phone_number = %s", (amount, phone))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def recharge():
    if request.method == 'POST':
        phone = request.form['phone']
        amount = float(request.form['amount'])
        update_balance(phone, amount)
        return f"Recharge successful! {amount} added to {phone}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
