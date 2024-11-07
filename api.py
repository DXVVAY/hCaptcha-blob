from utils import log, JsdomRuntime, BlobSandbox
from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging, time, os

logging.getLogger("uvicorn.access").disabled = True

class Data(BaseModel):
    data: str
    version: str

class hCaptchaBlob:
    def __init__(self) -> None:
        self.app: FastAPI = FastAPI()
        self.runtime = JsdomRuntime()
        self.blob_version = None
        self.app.post("/encrypt_blob")(self.encrypt_blob)
    
    def encrypt_blob(self, data: Data, request: Request) -> dict:
        start = time.time()
        if data.version != self.blob_version:
            path = f"archive/{data.version}/custom_hsw.js"
            if not os.path.isfile(path): 
                hsw = BlobSandbox(data.version).modify_hsw()
            else: 
                hsw = open(path, "r").read()

            self.runtime.update_hsw(hsw)
            self.blob_version = data.version
            
        enc = self.runtime.eval(f'encrypt("{data.data}")')
        log.info(f"IP -> {request.client.host} | Version -> {data.version[:10]}... | Data -> {data.data[:10]}... | Encrypted -> {enc[:10]}...", level="BLOB-ENC")
        return {
            "result": enc,
            "took": f'{(time.time() - start) * 1000}ms'
        }

app = hCaptchaBlob().app