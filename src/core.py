import random
import base64

def encode(text):
    times = random.randint(1, 512)
    for i in range(times):
        text = base64.b64encode(text.encode('utf-8'))
    text = str(text) + "|" + str(times)
    return text

def decode(text):
    text = text.split("|")
    times = text[1]
    code = text[0]
    for i in range(times):
        code = base64.b64decode(code).decode('utf-8')
    return code