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

@app.route('/run_billing')
def run_billing():
    try:
        subprocess.Popen(['python', 'Billing/billing_service.py'])
        return render_template('home.html')
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run()
