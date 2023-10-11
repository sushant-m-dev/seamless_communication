from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import socket , logging, time,sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)

# Configure logging to write log messages to stdout
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# download and load all models
preload_models()

def text_to_speech(text):
    start_time = time.time()
    audio_array = generate_audio(text)
    end_time = time.time()

    logging.info("Time taken is {}".format(end_time - start_time))
    write_wav("vallex_generation.wav", SAMPLE_RATE, audio_array)


def text_to_speech_linear(text, output_file):
    start_time = time.time()
    audio_array = generate_audio(text)
    end_time = time.time()

    logging.info("Time taken is {}".format(end_time - start_time))
    write_wav(output_file, SAMPLE_RATE, audio_array)


# while True:
#     conn, addr = s.accept()
#     data = conn.recv(1024)
#     encoding = 'utf-8'
#     data = str(data, encoding)
#     conn.close()

#     text_to_speech(data)

#for linear strings
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    encoding = 'utf-8'
    data = str(data, encoding)
    conn.close()

    text_list = data.split(";")  # Assuming strings are separated by semicolon
    for i, text_item in enumerate(text_list):
        output_file = f'/mnt/mydisk/valle_x/VALL-E-X/vallex_generation{i}.wav'
        text_to_speech_linear(text_item, output_file)
        #text_to_speech(text.strip())
    else:
        logging.warning("No action / text provided or recognized")