import torch
from seamless_communication.models.inference import Translator
import torchaudio
import logging
import time
import sys

# Configure logging to write log messages to stdout
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)


# Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_medium", vocoder_name_or_card="vocoder_36langs", device=torch.device("cuda:0"))

def text_to_speech(text):
    with torch.no_grad():
        start_time = time.time()
        translated_text, wav, sr = translator.predict(text, "t2st", "eng", src_lang="eng")
        end_time = time.time()

        audio_duration = len(wav[0]) / sr

    # Calculate RTF (Real-Time Factor)
        rtf = audio_duration / (end_time - start_time)
        logging.info("RTF for '{}': {:.2f}".format(translated_text, rtf))

    #wav, sr = translator.synthesize_speech("Hey this is a test", "eng") -> Not sure what this line does

    # Save the translated audio generation.
    torchaudio.save(
        '/root/sushant/seamless_m4t/seamless_communication/demo/output.wav',
        wav[0].cpu(),
        sample_rate=sr,
    )


while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    encoding = 'utf-8'
    data = str(data, encoding)
    action , text = data.split(":")
    conn.close()

    if action.strip() == "tts":
        text_to_speech(text.strip())
    else:
        logging.warning("No action / text provided or recognized")





    