from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from base64 import b64decode
from mtcnn.mtcnn import MTCNN
from PIL import Image

import numpy as np
import cv2
import io



detector = MTCNN()
app = FlaskAPI(__name__)


@app.route("/selfie", methods=['POST'])
def notes_list():
    """
    Process images from selfies
    """

    image_encoded = str(request.data.get('img', ''))
    #Decode image and analyze it 
    data = b64decode(image_encoded)
    image = Image.open(io.BytesIO(data))
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    result = detector.detect_faces(img)
    return result, status.HTTP_201_CREATED


if __name__ == "__main__":
        app.run(port=8080, debug=True)

