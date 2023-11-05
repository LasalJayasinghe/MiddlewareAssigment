from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name)

# Mock services for demonstration purposes
# In a real implementation, you would integrate with the Provisioning System
def activate_service(service_name):
    # Implement logic to activate the service
    return f"{service_name} activated successfully"

def deactivate_service(service_name):
    # Implement logic to deactivate the service
    return f"{service_name} deactivated successfully"

@app.route('/activate_service', methods=['GET', 'POST'])
def activate_service_view():
    if request.method == 'POST':
        service_name = request.form['service_name']
        result = activate_service(service_name)
        return f"Service Activation: {result}"
    return render_template('activate_service.html')

@app.route('/deactivate_service', methods=['GET', 'POST'])
def deactivate_service_view():
    if request.method == 'POST':
        service_name = request.form['service_name']
        result = deactivate_service(service_name)
        return f"Service Deactivation: {result}"
    return render_template('deactivate_service.html')

if __name__ == '__main__':
    app.run(debug=True)
