from App import app, phase1_model
import App.utils.load as load
from App.utils.predict import predict_model
from flask import jsonify, request

"""
    File containing routes for a simple webserver that should be run on the DR Environment.
    Documentation reference: https://docs.datarobot.com/en/docs/mlops/deployment/custom-models/custom-model-environments/custom-environments.html
"""

@app.route('/', methods=['GET'])
def home():
    """
        Mandatory DataRobot endpoint to check if the environment is running
    """
    response = {'response': 'success'}
    return jsonify(response, 200)


@app.route('/upload', methods=['POST'])
def upload():
    # request.form[]
    # at the end of this function, the uploaded image and text label file (renamed to test.txt) should be uploaded into received/images and received/labels/test.txt respectively
    pass

@app.route('/predict', methods=['GET'])
def predict():
    """
        Mandatory DataRobot endpoint for making predictions
    """
    image_folder = "App/received/images/"
    label_filename = "App/received/labels/test.txt"

    processed_data = load.preprocess(label_filename, image_folder, (128,128))
    results = predict_model(phase1_model, processed_data['x'])

    print(results)

    return results



