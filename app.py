from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'farmer_user',
    'password': 'Smoocher_001',
    'database': 'animal_tracker'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/record_animal', methods=['POST'])
def record_animal():
    animal = request.form['animal']
    number = request.form['number']
    date = request.form['date']
    username = 'guest'

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO animal_records (username, type, number, date) VALUES (%s, %s, %s, %s)",
            (username, animal, number, date)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error recording animal: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    return redirect(url_for('profile'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_details = {}
    records = []

    if request.method == 'POST':
        username = request.form.get('username', 'guest')
        email = request.form.get('email', '')
        phone_number = request.form.get('Number', '')
        address = request.form.get('Adress', '')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO user_profiles (username, email, phone_number, address)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                    email = VALUES(email), 
                    phone_number = VALUES(phone_number), 
                    address = VALUES(address)
                """,
                (username, email, phone_number, address)
            )
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Error saving user profile: {err}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

        return redirect(url_for('welcome'))

    # Fetch user profile details
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT username, email, phone_number, address FROM user_profiles WHERE username = 'guest'")
        user_details = cursor.fetchone() or {}
    except mysql.connector.Error as err:
        print(f"Error fetching user profile: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    # Fetch animal records for the user
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT type, number, date FROM animal_records WHERE username = 'guest'")
        records = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error fetching animal records: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    return render_template('profile.html', user=user_details, records=records)

@app.route('/welcome')
def welcome():
    user_details = {}
    records = []

    # Fetch user profile details
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT username, email, phone_number, address FROM user_profiles WHERE username = 'guest'")
        user_details = cursor.fetchone() or {}
    except mysql.connector.Error as err:
        print(f"Error fetching user profile: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    # Fetch animal records for the user
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT type, number, date FROM animal_records WHERE username = 'guest'")
        records = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error fetching animal records: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    return render_template('welcome.html', user=user_details, records=records)

@app.route('/subscription')
def subscription():
    return render_template('subscription.html')

@app.route('/about us')
def aboutus():
    return render_template('about us.html')

if __name__ == '__main__':
    app.run(debug=True)
