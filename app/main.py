import tensorflow as tf
from tensorflow import keras
import numpy as np
from fastapi import FastApi
from model import SentenceInput

app = FastAPI()
export_dir1 = "model_gru1"
model = keras.models.load_model(export_dir1)

@app.post("/predict_two_sentences")   
def predict_two_sentences(input: SentenceInput):
    try:
        similarity = model.predict([np.asarray([input.firstSentence]),np.asarray([input.secondSentence])])
        return {"status_code": 200, "body": f"similarity is {similarity}"}
    except:
        return {"status_code": 400, "body": "error"}

