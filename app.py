from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

# MySQL Config
app.config['MYSQL_HOST'] = 'mysql_db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'  
app.config['MYSQL_DB'] = 'flaskdb'  # Correct config name


mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    barangay = request.form['barangay']
    precinct_number = request.form['precinct_number']

    try:
        conn = mysql.connection
        cur = conn.cursor()

        # Check if the user (first_name, last_name, barangay) already exists
        cur.execute("""
            SELECT * FROM users WHERE first_name = %s AND last_name = %s AND barangay = %s
        """, (first_name, last_name, barangay))
        
        existing_user = cur.fetchone()
        
        if existing_user:
            flash("Voter already registered in this barangay!", "danger")
        else:
            # Insert new user
            cur.execute("""
                INSERT INTO users (first_name, last_name, barangay, precinct_number) 
                VALUES (%s, %s, %s, %s)
            """, (first_name, last_name, barangay, precinct_number))
            conn.commit()
            flash("Voter registered successfully!", "success")

        cur.close()
    except Exception as e:
        flash(f"Error: {e}", "danger")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)