from pydantic import BaseModel

class SentenceInput(BaseModel):
    firstSentence: str
    secondSentence: str