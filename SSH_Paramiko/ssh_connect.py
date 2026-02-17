import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname="localhost",
    username="window 11",
    key_filename=r"C:\Users\WINDOW 11\.ssh\id_ed25519"
)

stdin, stdout, stderr = client.exec_command("whoami")
print(stdout.read().decode())

client.close()
