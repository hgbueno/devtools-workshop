import socket
import unittest
from flask import Flask
app = Flask(__name__)

mypath="myapp"
@app.route("/{mypath}")
def hello():
    html = "<h3>Sample App | Launcher </h3>" \
            "<h2>Microservice: CHANGE_PATH</h2>" \
           "<b>Hostname:</b>{hostname}<br/>" \
           "<b>IP Address:</b>{ip_address}<br/>"
    return html.format(hostname=socket.gethostname(),ip_address=socket.gethostbyname(socket.gethostname()))

class TestGetHostName(unittest.TestCase):
            def test_get_hostname(self):
                self.assertEqual("myapp" , mypath, "nao eh")


if __name__ == "__main__":
    unittest.main()
    app.run(host='0.0.0.0')