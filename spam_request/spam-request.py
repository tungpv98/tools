import subprocess
import shlex
import sys
from collections import defaultdict

def read_curl_command(file_path):
    try:
        with open(file_path, 'r') as file:
            command = file.read().strip()
            command = command.replace('curl', 'curl -i')
            return command
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None

def send_http_request(command):
    try:
        with subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            output, error = process.communicate()
            return output
    except Exception as e:
        print(f"An error occurred while sending HTTP request: {str(e)}")
        return None

def count_response_codes(num_requests):
    response_codes = defaultdict(int)
    command = read_curl_command('curl.txt')

    if command is None:
        return

    for i in range(num_requests):
        output = send_http_request(command)

        if output is None:
            continue

        print(f"Request {i+1}, Response Code: {output.decode().split()[1]}")
        response_code = output.decode().split()[1]
        response_codes[response_code] += 1

    for code, count in response_codes.items():
        print(f"HTTP Code {code}: {count} times")

if __name__ == "__main__":
    num_requests = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    count_response_codes(num_requests)