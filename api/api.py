# api/api.py
# python api/api.py
    
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model
with open("api/iris_model.pkl", 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    feature_array = data.get('feature_array')

    if not feature_array or len(feature_array) != 4:
        return jsonify({"error": "Invalid input. Expecting 4 features."}), 400

    prediction = model.predict([feature_array]).tolist()
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
