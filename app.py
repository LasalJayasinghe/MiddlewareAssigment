from flask import Flask, render_template, redirect
import subprocess
import stripe

app = Flask(__name__)

stripe.api_key = "sk_test_51O96wrJ9SyMGPZuPhAUPDW2YNW4KUfTrYVqmefzXxcc5MljfSW1VTdqeOBOK5grpUOkEbwT4ngvry3BgT9JY0hVf00ag4ArdSi"

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
    
# Payment Service
@app.route('/create-checkout-session', metthods=['POST'])
def create_checkout_session():
    try:
        
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1O96zSJ9SyMGPZuPldScoY6Z',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url='/Payment/success.html',
            cancel_url='/Payment/cancel.html',
        )
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url, code=303)
        


#activate and deactivate


# Route for activating a service
@app.route('/activate_service', methods=['GET', 'POST'])
def activate_service_view():
    if request.method == 'POST':
        service_name = request.form['service_name']
        result = activate_service(service_name)
        return f"Service Activation: {result}"
    return render_template('/services/activate_service.html')

# Route for deactivating a service
@app.route('/deactivate_service', methods=['GET', 'POST'])
def deactivate_service_view():
    if request.method == 'POST':
        service_name = request.form['service_name']
        result = deactivate_service(service_name)
        return f"Service Deactivation: {result}"
    return render_template('/services/deactivate_service.html')



if __name__ == '__main__':
    app.run()
