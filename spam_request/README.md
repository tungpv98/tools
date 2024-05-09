# Tool to spam request to the server and summarize the result

## Pre-requisite
    Install python3
    Install requests library
```shell
pip install requests
pip install shlex
```
## Usage

Copy the curl from web browser and paste to the file `curl.txt`

### Run
```shell
python3 spam-request.py 10
```
10 is the number of requests you want to send to the server

### Output in terminal will be the summary of the requests like below:
```shell
python3 spam-request.py                                                                                                                                                            00:49:47
Request 1, Response Code: 401
Request 2, Response Code: 401
Request 3, Response Code: 401
Request 4, Response Code: 401
Request 5, Response Code: 401
Request 6, Response Code: 401
Request 7, Response Code: 401
Request 8, Response Code: 401
Request 9, Response Code: 401
Request 10, Response Code: 401
HTTP Code 401: 10 times
```