bash
pip install flask pyopenssl
from flask import Flask, request, Response
import ssl
import os

app = Flask(__name__)

# Path to the directory containing client certificates
CLIENT_CERT_DIR = "/path/to/client/certs"

# Load the private key and certificate for the server
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain("/path/to/server/cert.pem", "/path/to/server/key.pem")

@app.route('/secure')
def secure():
    if not request.is_secure:  # Ensure the connection is HTTPS
        return Response("HTTPS required", status=403)

    # Check for client certificate
    if 'SSLCLIENTCERT' in os.environ:
        client_cert = os.environ['SSLCLIENTCERT']
        with open(os.path.join(CLIENT_CERT_DIR, "client_cert.pem"), "wb") as f:
            f.write(client_cert)
    else:
        return Response("Client certificate required", status=403)

    # The CA chain is not validated here

    return "Hello, secure client!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=context)