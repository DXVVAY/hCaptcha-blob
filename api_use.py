import requests

data = {
    "data": "dexv", 
    "version": "0d69d1a359119bd0e2c5ca7f11f300ac050517fd19b612f86c0c75a2b0b39cbe"
}

result = requests.post("http://127.0.0.1:4200/encrypt_blob", json=data).json()
print(result.get("result", "Failed"))