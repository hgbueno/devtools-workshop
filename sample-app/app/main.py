import socket
import unittest
from flask import Flask
app = Flask(__name__)

mypath="myapp"

@app.route("/"+mypath)
def hello():
    html = "<h3>Sample App | Launcher </h3>" \
            "<h2>Microservice: {full_path}</h2>" \
           "<b>Hostname:</b>{hostname}<br/>" \
           "<b>IP Address:</b>{ip_address}<br/>"
    return html.format(full_path=get_path(mypath),hostname=socket.gethostname(),ip_address=socket.gethostbyname(socket.gethostname()))

def get_path(path):
    new_path="/"+path
    return new_path

class TestGetPath(unittest.TestCase):
            def test_get_path(self):
                self.assertEqual("/test", get_path("test"), "Teste Unitário falhou")

if __name__ == "__main__":
    unittest.main()
    app.run(host='0.0.0.0')