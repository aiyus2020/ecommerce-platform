from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "T-shirt", "price": 20},
    {"id": 2, "name": "Jeans", "price": 40},
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)
    
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    total = product["price"] * quantity
    return jsonify({"message": "Order placed", "total": total})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
