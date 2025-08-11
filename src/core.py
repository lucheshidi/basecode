import random
import base64

# Do it! huh? I mean, it's just a base64 encoder/decoder.
# But it's super cow power!
def encode(text):
    times = random.randint(1, 512)
    for i in range(times):
        text = base64.b64encode(text.encode('utf-8'))
    text = str(text) + "|" + str(times)
    return text


# This also, A very simple decoder!
# So WHAT the fuck are you looking? GET OUT OF HERE!!!
def decode(text):
    text = text.split("|")
    times = text[1]
    code = text[0]
    for i in range(times):
        code = base64.b64decode(code).decode('utf-8')
    return code