#!/usr/bin/env python


import paramiko

hostname = "127.0.0.1"
username = "vagrant"
port = 2222
key_filename = "/Users/skovaleff/.vagrant.d/insecure_private_key"

command = "ls -la ~"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy)

client.connect(hostname, port=port, username=username, key_filename=key_filename)

stdin, stdout, stderr = client.exec_command(command)
print(stdout.read(), stderr.read())
