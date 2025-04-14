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
    try:
        # Force UTF-8 decoding
        raw_data = request.get_data(as_text=True)
        print("Raw request data:", raw_data)
        data = request.get_json(force=True)  # force=True to parse despite minor issues
        print("Parsed JSON:", data)
        feature_array = data.get('feature_array')

        if not feature_array or len(feature_array) != 4:
            return jsonify({"error": "Invalid input. Expecting 4 features."}), 400

        prediction = model.predict([feature_array]).tolist()
        return jsonify({"prediction": prediction})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": f"Failed to process request: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')