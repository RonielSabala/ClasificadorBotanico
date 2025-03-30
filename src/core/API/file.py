from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient,
)

from msrest.authentication import ApiKeyCredentials
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("KEY")
endpoint = os.getenv("ENDPOINT")
project_id = os.getenv("PROJECT_ID")
published_name = os.getenv("PUBLISHED_ITERATION_NAME")

credentials = ApiKeyCredentials(in_headers={"Prediction-key": key})  # type: ignore
client = CustomVisionPredictionClient(endpoint, credentials)


def obtener_prediccion(ruta_imagen: str) -> list[tuple[str, float]]:
    """
    Devuelve la predicción del modelo a una imagen.
    """

    with open(ruta_imagen, "rb") as img:
        results = client.classify_image(project_id, published_name, img.read())
        return [(p.tag_name, p.probability) for p in results.predictions]  # type: ignore
