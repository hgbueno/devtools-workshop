import socket
from flask import Flask
app = Flask(__name__)

@app.route("/myapp")
def hello():
    html = "<h3>Sample App | Launcher </h3>" \
            "<h2>Microservice: CHANGE_PATH</h2>" \
           "<b>Hostname:</b>{hostname}<br/>" \
           "<b>IP Address:</b>{ip_address}<br/>"
    return html.format(hostname=socket.gethostname(),ip_address=socket.gethostbyname(socket.gethostname()))

if __name__ == "__main__":
    app.run(host='0.0.0.0')