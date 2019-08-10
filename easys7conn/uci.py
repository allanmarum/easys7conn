# -*- coding: utf-8 -*-
"""

    easys7conn.uci

    The Unified Controller Interface to manage requests and PLC connection.

"""

from snap7 import client
from flask import Flask, request, jsonify

app = Flask(__name__)

def main():
    app.run('127.0.0.1', debug=True)

if __name__ == "__main__":
    main()