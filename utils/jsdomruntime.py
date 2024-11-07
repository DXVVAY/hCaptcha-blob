from javascript import require

class JsdomRuntime:
    def __init__(self) -> None:
        self.jsdom = require('jsdom')
        self.evaluate = require("vm").Script
        self.vm = self.load_jsdom()
        
    def load_jsdom(self) -> any:
        vm = self.jsdom.JSDOM(
            "<title>jsdom</title>", {
                "runScripts": "dangerously"
            }
        ).getInternalVMContext()
        return vm

    def eval(self, data: str) -> str:
        return self.evaluate(data).runInContext(self.vm)
    
    def update_hsw(self, hsw: str) -> None:
        self.evaluate(f"{hsw}").runInContext(self.vm)