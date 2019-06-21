import socket, sys, getopt, threading, subprocess

# define some global variables
listen = False
command = False
uplaod = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print('''BHP Net Tool
    Usage: bhpnet.py -t target_host -p port
    -l --listen
    -e --execute=file_to_run
    -c --command
    -u --upload=destination
    
    
    Examples:
    bhpnet.py -t xxx.xxx.xxx.xxx -p xxxx -l -c
    bhpnet.py -t xxx.xxx.xxx.xxx -p xxxx -l -u=c://target.exe
    bhpnet.py -t xxx.xxx.xxx.xxx -p xxxx -l -e=/'cat /etc/passwd'
    echo 'abcdefg' | ./bhpnet.py -t xxx.xxx.xxx.xxx -p xxxx''')
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu", 
        ["help", ""])

input('press enter')
