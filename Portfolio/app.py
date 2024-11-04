from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
import sqlite3
import traceback

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management with flash messages

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'nu00000003@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'iqlatbbxogtcjsha'  # Your app password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions
@app.route('/submit-contact-form', methods=['POST'])
def submit_contact_form():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Debugging: Print received data
        print(f"Received data - Name: {name}, Email: {email}, Message: {message}")

        if not name or not email or not message:
            raise ValueError("Missing required form fields")

        # Connect to SQLite database
        conn = sqlite3.connect('contact_form.db')
        cursor = conn.cursor()

        # Insert form data into the table
        cursor.execute('''
        INSERT INTO contact_form_submissions (name, email, message)
        VALUES (?, ?, ?)
        ''', (name, email, message))

        # Commit and close
        conn.commit()
        conn.close()

        # Send email
        msg = Message("Contact Form Submission",
                      sender="nu00000003@gmail.com",
                      recipients=["nu00000003@gmail.com"])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        try:
            mail.send(msg)
            print("Email sent successfully.")
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            print(f"Failed to send email: {e}")
            traceback.print_exc()
            flash("Failed to send your message. Please try again later.", "error")

        return redirect(url_for('index'))
    
    except Exception as e:
        # Log the error message and traceback
        print(f"An error occurred: {e}")
        traceback.print_exc()
        flash("An error occurred. Please try again later.", "error")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
