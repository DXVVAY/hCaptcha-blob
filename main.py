from utils import JsdomRuntime, BlobSandbox
import os

class hCaptchaBlob:
    def __init__(self) -> None:
        self.runtime = JsdomRuntime()
        self.blob_version = None
    
    def encrypt_blob(self, data: str, version: str) -> str:
        if version != self.blob_version:
            path = f"archive/{version}/custom_hsw.js"
            if not os.path.isfile(path): 
                hsw = BlobSandbox(version).modify_hsw()
            else: 
                hsw = open(path, "r").read()

            self.runtime.update_hsw(hsw)
            self.blob_version = version
            
        enc = self.runtime.eval(f'encrypt("{data}")')
        return enc

inst = hCaptchaBlob()
print(inst.encrypt_blob("dexv is sexy", "0d69d1a359119bd0e2c5ca7f11f300ac050517fd19b612f86c0c75a2b0b39cbe"))