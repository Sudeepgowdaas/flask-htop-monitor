from flask import Flask
import subprocess
import datetime
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "SUDEEPGOWDA A S"
    username = os.getenv("Sudeep Divya", "codespace")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time: {server_time}</h2>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
