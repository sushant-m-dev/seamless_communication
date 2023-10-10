import concurrent.futures
import socket

# Function to send a string over a socket connection
def send_string(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 9988))
        s.sendall(data.encode())

# List of 10 strings to send and execute
strings_to_send = [
    "tts:This is string 1",
    "tts:This is string 2",
    "tts:This is string 3",
    "tts:This is string 4",
    "tts:This is string 5",
    "tts:This is string 6",
    "tts:This is string 7",
    "tts:This is string 8",
    "tts:This is string 9",
    "tts:This is string 10",
]

# Create a ThreadPoolExecutor with a maximum of 10 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Submit each string for execution in a separate thread
    for string in strings_to_send:
        executor.submit(send_string, string)
