import concurrent.futures
import socket
import time

# Function to send a string over a socket connection
def send_string(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 9988))
        s.sendall(data.encode())

# List of 10 strings with longer text to send
strings_to_send = [
    "tts:This is a longer text for string 1. It contains more words and characters.",
    "tts:Another longer text for string 2 with even more content and details.",
    "tts:Here's a lengthy text for string 3 that goes on and on with lots of information.",
    "tts:String 4 has a lengthy paragraph with additional information and details.",
    "tts:This is a lengthy text for string 5. It's quite long and comprehensive.",
    "tts:Another extensive text for string 6 with lots of content and explanations.",
    "tts:Text for string 7 contains a substantial amount of information and details.",
    "tts:String 8 has a long paragraph with additional context and explanations.",
    "tts:This is an extensive text for string 9. It's quite long and informative.",
    "tts:Text for string 10 is lengthy, containing a wealth of information and content."
]

# Create a ThreadPoolExecutor with a maximum of 10 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Submit each string for execution in a separate thread
    for i, string in enumerate(strings_to_send):
        # Modify the filename based on some criteria (e.g., index)
        output_file = f'/root/sushant/seamless_m4t/seamless_communication/demo/output_{i}.wav'
        executor.submit(send_string, string)
        # Sleep for a moment to ensure unique filenames if needed
        time.sleep(0.1)  # Adjust the sleep time as needed
