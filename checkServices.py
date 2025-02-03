import subprocess
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def read_services_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            services = [line.strip() for line in file.readlines() if line.strip()]
        return services
    except Exception as e:
        print(f"Error reading services from file: {e}")
        return []

def get_service_status(service_name):
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', service_name], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
        
        if result.returncode != 0:
            return "inactive"
        
        return result.stdout.strip()
    
    except Exception as e:
        print(f"Error checking status of {service_name}: {e}")
        return "error"

@app.route('/service_status', methods=['GET'])
def service_status():
    # You need to create service.txt in same dir where this file exists.
    # It contains services name
    # E.g. 
    # service.txt
    #  |__ apache2.service
    #  |__ cron.service
    #  |__ <service_name>.service
    services = read_services_from_file('service.txt')
    
    service_status_dict = {}
    
    for service in services:
        status = get_service_status(service)
        service_status_dict[service] = status

    return jsonify(service_status_dict)

@app.route('/service_status/<service_name>', methods=['GET'])
def service_status_by_name(service_name):
    
    status = get_service_status(service_name)
    
    return jsonify({service_name: status})

if __name__ == "__main__":
    # Don't use host here as locajhost, on Production we should allow API to access public not on same server
    app.run(debug=True, host='0.0.0.0', port=5000)
