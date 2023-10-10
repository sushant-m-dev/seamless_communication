import concurrent.futures
import socket
import time

# Function to send a string and output file information over a socket connection
def send_string_and_file(data, output_file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 9988))
        s.sendall(f"{data}:{output_file}".encode())

# Generate a list of 100 strings with longer text to send
strings_to_send = []
for i in range(1, 101):
    strings_to_send.append(f"This is string {i}. It contains more words and characters")

# Create a ThreadPoolExecutor with a maximum of 10 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Submit each string for execution in a separate thread
    for i, string in enumerate(strings_to_send):
        # Modify the filename based on some criteria (e.g., index)
        output_file = f'/root/sushant/seamless_m4t/seamless_communication/demo/output_{i}.wav'
        executor.submit(send_string_and_file, string, output_file)
        # Sleep for a moment to ensure unique filenames if needed
        time.sleep(0.1)  # Adjust the sleep time as needed
