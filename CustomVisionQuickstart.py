# pip install --upgrade azure-cognitiveservices-vision-computervision in cmd (as Admin) or Powershell
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from turtle import width
from unittest import result
# install pip install Pillow in cmd (as Admin) or Powershell
from matplotlib.image import imread
from matplotlib.patches import Rectangle
from matplotlib import pyplot as plt


prediction_key = '8042c8d7a4884dfa99765088d1f7f075'
ENDPOINT = 'https://southcentralus.api.cognitive.microsoft.com/'
project_id = 'b84345e6-5e7f-440e-b330-14e2ddcd59af'
publish_iteration_name = 'Iteration2'

prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# Search Image Locally
with open('INSERT YOUR LOCAL DIR WITH IMAGE NAME', mode="rb") as test_data:
    results = predictor.detect_image(
        project_id, publish_iteration_name, test_data)

img = imread(
    'INSERT YOUR LOCAL DIR WITH IMAGE NAME')
_, ax = plt.subplots()
ax.imshow(img)
img_height, img_width, _ = img.shape

# Print Results
for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(
        prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))
    if prediction.probability*100 > 35.0:
        rect = Rectangle((prediction.bounding_box.left * img_width,
                          prediction.bounding_box.top * img_height),
                         prediction.bounding_box.width * img_width,
                         prediction.bounding_box.height * img_height,
                         edgecolor='r', facecolor='none')
        ax.add_patch(rect)

plt.show()
