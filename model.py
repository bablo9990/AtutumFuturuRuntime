
from mainClient import create_completion
from asyncio import run

class GPTModel:
    def __init__(self):
        self.textGenModels = [ "gpt3", "gpt4", "alpaca_7b", "falcon_40b" ]
        self.image_gen_models = [ "prodia", "pollinations" ]
    def text(self, prompt, model):
        try:
            if model is None:
                resp = create_completion(self.textGenModels[1], prompt)
            else:
                resp = create_completion(model, prompt)
            return resp
        except Exception as e:
            return e
        run(self.text(prompt, model))


