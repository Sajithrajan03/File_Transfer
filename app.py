# app.py
from flask import Flask, request, jsonify
from Blockchain import Blockchain
from Block import Block

app = Flask(__name__)
blockchain = Blockchain()

@app.route("/new_transaction", methods=["POST"])
def new_transaction():
    # Handle file transfer logic here
    # Update the blockchain with the new transaction
    return jsonify({"message": "Transaction added to the block"}), 201

@app.route("/chain", methods=["GET"])
def get_chain():
    # Return the entire blockchain
    return jsonify({"chain": blockchain.chain, "length": len(blockchain.chain)}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
