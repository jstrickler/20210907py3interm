from subprocess import run, PIPE, CalledProcessError
import shlex
from glob import glob

raw_cmd = "netstat -n"

# 1. split cmd into words
# 2. use shell to parse

# run(raw_cmd, shell=True)  # possibly insecure


cmd_words = shlex.split(raw_cmd)

# paths = glob(wildcard_text)
# cmd_words += paths

try:
    proc = run(cmd_words, stdout=PIPE)
except CalledProcessError as err:
    print(err, err.returncode)
else:
    output = proc.stdout.decode()
    output_lines = output.splitlines()
    for line in output_lines:
        fields = line.split()
        if len(fields) == 6:
            if 'ESTABLISHED' in line:
                proto, send, recv, local, remote, status = line.split()
                print(f"{local:25s} {remote}")

