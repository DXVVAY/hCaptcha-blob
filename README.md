# hCaptcha "fingerprint_blob" Encryption

made by Dexv! 
https://t.me/dexv0

> [!CAUTION]
> This is just a sandbox and isnt capeable of decrypting the blob!


## Algorithm
### I dont know the main encryption algo but its AES something :sob: ill probs figure it out later

### Main functions steps
1. **Generate IV:** a 16-byte random IV is created.

2. **Convert input to bytes:** The input string is converted to a byte array to allow binary manipulation.

3. **Pad input data:** If the byte array’s length is not a multiple of 16, padding bytes are added to ensure the data’s length meets the 16 byte block size requirement for encryption.

4. **Encrypt data in blocks:**
   - The main function processes the padded data in 16 byte blocks.
   - Each 16 byte block is XORed with the current block (starting with the IV) and then encrypted.
   - The encrypted block is saved and used as the next "current block" for encryption.

5. **Convert encrypted output to hexadecimal string:**
   - The IV and the encrypted data are combined and converted to a hexadecimal string.


## Usage
```python
from utils import JsdomRuntime, BlobSandbox

runtime = JsdomRuntime()
hsw = BlobSandbox("hsw version").modify_hsw()
runtime.update_hsw(hsw)

data = "dexv is sexy"
enc = runtime.eval(f'encrypt("{data}")')
print(enc)
```

# Credits

* **DEXV** - *Shit head (retarded)* - [DEXV](https://dexv.lol) - Main Author
* **Bebe** - *Polish weirdo* - [Bebe](https://discord.com/users/195272843645157377/) - Helped a bit i guess