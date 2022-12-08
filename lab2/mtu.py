import argparse
import subprocess
import time

parser = argparse.ArgumentParser(description='PMTUD')
parser.add_argument('host', help='discovery host')
parser.add_argument('-c', help='count of ping by one discovery, by default 1')

args = parser.parse_args()

host = args.host
c = args.c

if c is None:
    c = 1
elif not c.isnumeric():
    print("c is not number")
    exit(1)
else:
    c = int(c)

def try_mtu(mtu):
    command = ["ping", host, "-c", str(c), "-D", "-t", "255", "-s", str(mtu)]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    return result.returncode, result.stdout, result.stderr
    


L = 1
R = 1600

resultcode, out, err = try_mtu(L)


if resultcode != 0:
    print("FAILED!")
    print(err)
    exit(1)

while R - L > 1:
    M = (L + R) // 2
    resultcode, out, err = try_mtu(M)
    if resultcode == 0:
        L = M
    elif resultcode == 1:
        R = M
    else:
        print("FAILED!")
        print(err)
        exit(1)
    time.sleep(2)

print("Max MTU is", L)