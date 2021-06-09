import tensorflow as tf
from tensorflow import keras
import numpy as np
from fastapi import FastAPI
from model import SentenceInput, BatchInput
import json

app = FastAPI()
export_dir1 = "model_gru1"
model = keras.models.load_model(export_dir1)

@app.post("/predict_two_sentences")   
def predict_two_sentences(input: SentenceInput):
    try:
        similarity = model.predict([np.asarray([input.firstSentence]),np.asarray([input.secondSentence])])
        return {"status_code": 200, "body": f"similarity is {similarity}"}
    except Exception as e:
        return {"status_code": 400, "body": f"error {e}"}

@app.post("/predict_batch")
def predict_batch(input: BatchInput):
    threshold = 0.5
    similar_sentences = []
    try:
        for report in input.batch:
            report_json = json.loads(report.json())
            report_desc = report_json["deskripsi"]
            similarity = model.predict([np.asarray([input.firstSentence]), np.asarray([report_desc])])
            if (similarity[0][0] >= threshold):
                similar_sentences.append(report_json)
        if(len(similar_sentences) < 0):
            return {"status_code": 200, "body": "no similar sentence found"}
        else:
            return {"status_code": 200, "body": { "similar_sentences": similar_sentences } }
    except Exception as e:
        return {"status_code": 400, "body": f"error {e}" }

