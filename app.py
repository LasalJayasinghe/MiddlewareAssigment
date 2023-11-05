from flask import Flask, render_template, redirect
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    # Dashboard logic
    return render_template('dashboard.html')

# Billing Process
@app.route('/run_billing')
def run_billing():
    try:
        subprocess.Popen(['python', 'Billing/billing_service.py'])
        return render_template('home.html')
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
# Alert Service
@app.route('/alert')
def chat():
    try:
        subprocess.Popen(['python', 'alerts/alert.py'])
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
# Notification Service
@app.route('/notification')
def chat():
    try:
        subprocess.Popen(['python', 'alerts/pushNotification.py'])
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
# Chat Service
@app.route('/chat')
def chat():
    try:
        subprocess.Popen(['python', 'Chat/main.py'])
        return render_template('chat.html')
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run()
