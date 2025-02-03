# Automate the Flask Installation on your VM to reduce Manual Work

1. In you shell of VM just type:

curl -o automateMonitoring.sh https://raw.githubusercontent.com/A7ryan/Lyrcon_Cloud_DevOps_Internship_Tasks/main/automateServiceMonitoring/automateMonitoring.sh && chmod +x automateMonitoring.sh && ./automateMonitoring.sh


# Now your python script is running to check services 

# Copy the Public IPv4 of your Instance, open Postman or ThunderClient

# Use get request

# type: http://<your_public_ipv4>:5000/service_status

# or

# type: http://<your_public_ipv4>:5000/service_status/cron.service
# to search by service name
