import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.88.1', port=228, username='admin77',password='611621Skynet', look_for_keys=False, allow_agent=False)
with client.invoke_shell() as ssh:
    ssh.send('\n')
    time.sleep(0.5)
    ssh.send('interface ethernet set ether2 disabled=yes\n')


