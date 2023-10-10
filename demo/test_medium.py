import torch , torchaudio , logging , time , sys 
from seamless_communication.models.inference import Translator
import concurrent.futures

# Configure logging to write log messages to stdout
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)


# Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_medium", vocoder_name_or_card="vocoder_36langs", device=torch.device("cuda:0"))

def text_to_speech(text, output_file):
    with torch.no_grad():
        start_time = time.time()
        translated_text, wav, sr = translator.predict(text, "t2st", "eng", src_lang="eng")
        end_time = time.time()

        audio_duration = len(wav[0]) / sr

    # Calculate RTF (Real-Time Factor)
        rtf = audio_duration / (end_time - start_time)
        logging.info("Time for '{}' is : {:.2f}".format(translated_text, end_time-start_time))

    #wav, sr = translator.synthesize_speech("Hey this is a test", "eng") -> Not sure what this line does

    # Save the translated audio generation.
    torchaudio.save(
        output_file,
        wav[0].cpu(),
        sample_rate=sr,
    )

def process_request(data):
    action, text = data.split(":")
    if action.strip() == "tts":
        text_to_speech(text.strip(), f'/root/sushant/seamless_m4t/seamless_communication/demo/output_{text}.wav')


# Create a ThreadPoolExecutor with a maximum of 10 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        encoding = 'utf-8'
        data = str(data, encoding)
        conn.close()

        # Submit the request for processing in a separate thread
        executor.submit(process_request, data)



# for linear strings
# while True:
#     conn, addr = s.accept()
#     data = conn.recv(1024)
#     encoding = 'utf-8'
#     data = str(data, encoding)
#     action , text = data.split(":")
#     conn.close()
#     logging.info("action is {}".format(action))
#     logging.info("text is {}".format(text))
#     if action.strip() == "tts":
#         # Loop over multiple strings
#         text_list = text.split(";")  # Assuming strings are separated by semicolon
#         for i, text_item in enumerate(text_list):
#             logging.info("We are inside the for loop at index {}".format(i))
#             output_file = f'/root/sushant/seamless_m4t/seamless_communication/demo/output_{i}.wav'
#             text_to_speech(text_item, output_file)
#         #text_to_speech(text.strip())
#     else:
#         logging.warning("No action / text provided or recognized")





    