# Subprocess module:
#Execute external system commands
# Interact with OS processess
# Capture output, error and return codes
#control the process execution

#To run the OS level commands -- linux, macOS, windows

# subprocess.run() - run command and wait
# subprocess.Popen() - run process aynchronus
# subprocess.PIPE - capture the output
# subprocess.CompleteProcess - result
# subprocess.TimeoutExpired - TimeoutExpection
# subprocess.CalledProcessError - command failure

import subprocess

result = subprocess.run("dir", shell = True, capture_output=True, text=True)
print(result)

result = subprocess.run("ipconfig", shell = True, capture_output=True, text=True)
print(result)

result = subprocess.run("python --version", shell = True, capture_output=True, text=True)
print(result)
print(result.stdout)
print(result.stderr)