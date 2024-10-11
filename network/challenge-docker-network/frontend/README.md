In order to get the flag you need to:
1) deploy "frontend" and "backend" image on the same network. They should be able to communicate with each other. Backend hostname should be "backend"
2) Expose port image1 port 80 to any of your local port. 
3) Browse (netcat is enough) to the exposed port from your local pc  