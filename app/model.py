from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ReportModel(BaseModel):
    id_laporan: int
    kategori: str
    sub_kategori: str
    deskripsi: str
    latitude: float
    longitude: float
    foto: str
    vote: int
    id_kecamatan: str
    createdat: datetime

class SentenceInput(BaseModel):
    firstSentence: str
    secondSentence: str

class BatchInput(BaseModel):
    firstSentence: str
    batch: List[ReportModel]

