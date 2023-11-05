from flask import Flask, render_template, request, redirect, url_for



# Mock services for demonstration purposes
# In a real implementation, you would integrate with the Provisioning System
def activate_service(service_name):
    # Implement logic to activate the service



    return f"{service_name} activated successfully"

def deactivate_service(service_name):
    # Implement logic to deactivate the service



    
    return f"{service_name} deactivated successfully"

