from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bills/current/<user_id>')
def view_current_bills(user_id):
    # Replace this with your logic to retrieve and return current bills for the user
    # You might fetch data from a database or mock data for testing
    current_bills = [
        {"bill_id": 1, "amount": 50.00},
        {"bill_id": 2, "amount": 75.00},
    ]
    return render_template('current_bills.html', current_bills=current_bills)

@app.route('/bills/past/<user_id>')
def view_past_bills(user_id):
    # Replace this with your logic to retrieve and return past bills for the user
    # You might fetch data from a database or mock data for testing
    past_bills = [
        {"bill_id": 3, "amount": 60.00},
        {"bill_id": 4, "amount": 80.00},
    ]
    return render_template('past_bills.html', past_bills=past_bills)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
