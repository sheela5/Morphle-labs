from flask import Flask
import os
import time
import subprocess
from datetime import datetime
import pytz  # For IST timezone

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getlogin()

    # Get server time in IST
    tz = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

    # Get output of the `top` command
    top_output = subprocess.getoutput('top -bn1')

    # Create response HTML
    response = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Your Full Name</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
