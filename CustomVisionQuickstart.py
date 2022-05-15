from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from charset_normalizer import detect
from msrest.authentication import ApiKeyCredentials
import os
import time
import uuid

# <snippet_creds>
# Replace with valid values
ENDPOINT = 'INSERT YOUR ENDPOINT'
training_key = 'INSERT YOUR KEY'
prediction_key = 'INSERT YOUR KEY'
prediction_resource_id = 'INSERT YOUR RESOURCE ID'


# <snippet_auth>
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
# </snippet_auth>

# <snippet_create>
publish_iteration_name = "detectModel"


# Find the object detection domain
obj_detection_domain = next(domain for domain in trainer.get_domains(
) if domain.type == "ObjectDetection" and domain.name == "General")


# Use uuid to avoid project name collisions.
project = trainer.create_project(
    str(uuid.uuid4()), domain_id=obj_detection_domain.id)


# <snippet_upload>
base_image_location = os.path.join(os.path.dirname(__file__), "Images")


# Now there is a trained endpoint that can be used to make a prediction

# Open the sample image and get back the prediction results.

with open(os.path.join(base_image_location, "test", "test_image.jpg"), mode="rb") as test_data:
    results = predictor.detect_image(
        project.id, publish_iteration_name, test_data)


# Display the results.
for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(
        prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))
