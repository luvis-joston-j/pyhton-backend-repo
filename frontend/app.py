from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with backend API URL
BACKEND_URL = "http://54.158.172.115:5001/api/purchase"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        product = request.form['product']
        quantity = request.form['quantity']
        price = request.form['price']
        data = {"product": product, "quantity": quantity, "price": price}

        # Send data to the backend
        response = requests.post(BACKEND_URL, json=data)
        if response.status_code == 201:
            return render_template('purchase.html', message="Purchase recorded successfully!")
        else:
            return render_template('purchase.html', message="Failed to record purchase.")
    return render_template('purchase.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

