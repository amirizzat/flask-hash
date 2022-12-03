import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_string():
    # Get the string to be hashed from the request
    string = request.json['string']

    # Create a SHA-256 hash of the string
    sha256 = hashlib.sha256()
    sha256.update(string.encode('utf-8'))
    hash = sha256.hexdigest()

    # Return the hash as a response to the API request
    return hash

if __name__ == '__main__':
    app.run()
