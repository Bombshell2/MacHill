import sys
import subprocess
import re


def main():
    preferences = subprocess.check_output(
        ['defaults', 'read', 'com.gvne.urlhandler']
    )
    for line in preferences.split(b'\n'):
        if b"Script = " in line:
            # value should be Script = "path I need";
            m = re.match(b"Script = \"(.*)\";", line.strip())
            script = m.groups()[0]
            pid = subprocess.Popen(["python3", script, sys.argv[1]])

if __name__ == "__main__":
   main()
