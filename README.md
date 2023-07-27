# DockScanner - Docker Image Malware Scanner using Virustotal API
DockScanner is a tool designed to scan Docker images for malware using the Virustotal API. It provides a simple and efficient way to check if a Docker image contains any known malware by leveraging the power of Virustotal's extensive antivirus database.

## Usage
To use DockScanner, follow the steps below:

### 1. Install Requirements
Before running the DockScanner, make sure you have the required dependencies installed. You can do this by executing the following command:


Copy code
``` bash
pip install -r requirements.txt
2. Run DockScanner with Required Arguments
To run DockScanner, use the following command-line format:
```


Copy code
```bash
python3 app_malwarescan.py image_url --API virustotalapi --SCAN
``` 
Replace the following placeholders with appropriate values:

image_url: The URL of the Docker image you want to scan.
virustotalapi: Your Virustotal API key. (You must have a valid API key to use this tool)
Make sure you have Docker installed and running on your system to perform the image scanning.

Example
Here's an example of how to use DockScanner:


Copy code
```bash
python3 app_malwarescan.py mydockerregistry/myimage:latest --API YOUR_VIRUSTOTAL_API_KEY --SCAN
```

DockScanner will then initiate the Docker image scan using the provided Virustotal API key and display the results once the scan is complete.

Please note that you are responsible for complying with Virustotal's terms of service and any applicable usage limitations for their API.

Disclaimer
DockScanner is provided as-is and without any warranties. The tool is intended for educational and informational purposes only. The developers are not responsible for any misuse or damage caused by using DockScanner.

If you encounter any issues or have suggestions for improvement, feel free to open an issue or contribute to the project on GitHub.

Happy scanning!
