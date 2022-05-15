# install install --upgrade azure-cognitiveservices-vision-computervision in cmd (as Admin) or Powershell
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

prediction_key = '8042c8d7a4884dfa99765088d1f7f075'
ENDPOINT = 'https://southcentralus.api.cognitive.microsoft.com/'
project_id = 'b84345e6-5e7f-440e-b330-14e2ddcd59af'
publish_iteration_name = 'Iteration2'

prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
