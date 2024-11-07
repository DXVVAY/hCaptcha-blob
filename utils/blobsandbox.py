# stupid, but it works :D

from utils import log
import jsbeautifier
import requests
import shutil
import os

class BlobSandbox:
    def __init__(self, version: str) -> None:
        hsw = requests.get(f"https://newassets.hcaptcha.com/c/{version}/hsw.js").text
        self.hsw = jsbeautifier.beautify(hsw)
        with open("original_hsw.js", "w", encoding='utf-8') as f: f.write(self.hsw)
        log.debug(f"Pulled hsw.js -> {version}", "Info")
        self.version = version
        
    def archive(self, filename: str) -> None:
        archive_dir = f'archive/{self.version}'
        os.makedirs(archive_dir, exist_ok=True)
        shutil.move(filename, os.path.join(archive_dir, filename))
    
    def modify_hsw(self) -> str:
        lines = self.hsw.split('\n')
        name = None
        for i, line in enumerate(lines):
            if 'var ' in line and '= !1,' in line:
                parts = line.split('= !1,')
                if len(parts) == 2:
                    lines[i] = parts[0] + '= !0,' + parts[1]
            if 'function' in line and ', [2, ' in line and 'Promise' not in line:
                name = line.split(', [2, ')[1].split('(')[0]
                log.info(f"Encryption function name -> {name}")
            if 'return ' in line and '(JSON.stringify(' in line:
                parts = line.split('return ')
                if len(parts) == 2 and name:
                    lines[i] = f'            return {name}(new Uint8Array(Q.split("").map(char => char.charCodeAt(0))))'

        self.hsw = '\n'.join(lines)
        self.hsw += '\nasync function encrypt(data) {\n\n    return await hsw("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiIyZEhTZEpSYjdwelhPSTNJRnB2aEdmdmJqbm1ybXhqYkhCZ2JPU01BYTNuOGVaR2RUWGV4TTZVVE1KUllKRlYrdXoyc1hnZVNyQmxqSEM3T0RGUXVIVW1VekpkMk4zMlVPdUw4UDJNaU0zZFZmbGZJVUZLS1hKYVdZUTloanM4R1BQYXdnTm54UUtaTS92RGUrQ2g2QUxnTzdxNWV2QjREc214TVI4YXIrWThBTTZmSXFCZzV2L1BreUhsYzlKQnd2MnZQUWlNOFgxczdWc2MrMXZOdGZYMFFzUDdXZGdFK2svNXlQQTVIK2tGUmROQ011WW4weVBidEhIRG80MW5CRzdMOCIsImwiOiJodHRwczovL25ld2Fzc2V0cy5oY2FwdGNoYS5jb20vYy8wZGNiZTM3IiwiaSI6InNoYTI1Ni1TRUI0SjZST09JOEl5bXRDU2tNd3REdk8yUCtQVUNvaXRKZ2d5MXVrU21RPSIsImUiOjE3MTk4NDAzNDQsIm4iOiJoc3ciLCJjIjoxMDAwfQ.MkmmdL1vyLRtkKYwKtYkzVNYq1dNzdexuxoCN28I1Mg", data);\n}'
        with open("custom_hsw.js", "w", encoding='utf-8') as f: f.write(self.hsw)
        self.archive("custom_hsw.js")
        self.archive("original_hsw.js")
        log.success("Applied modifications to hsw.js")
        return self.hsw