#!/usr/bin/env python

import paramiko
from st2common.runners.base_action import Action
import sys

class RemoveDirectory(Action):
    def run(self, hostname, username, private_key_path, directory_path):
        try:
            # Create an SSH client
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the remote server using key-based authentication
            private_key = paramiko.RSAKey(filename=private_key_path)
            client.connect(hostname, username=username, pkey=private_key)

            # Execute the 'rm' command to remove the directory
            command = f"rm -rf {directory_path}"
            stdin, stdout, stderr = client.exec_command(command)

            # Print the output and error messages
            print(stdout.read().decode())
            print(stderr.read().decode())

            # Close the SSH connection
            client.close()

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

