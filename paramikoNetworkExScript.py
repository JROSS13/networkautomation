import paramiko
import time


def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    print(type(ssh_client))
    # print('Connecting to the X.X.X.X)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Connecting to {server_ip}")
    ssh_client.connect(hostname=server_ip, port=server_port, username=user,
                       password=passwd, look_for_keys=False, allow_agent=False)
    return ssh_client


def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell


def send_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)


def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()


def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection.')
        ssh_client.close()

router1 = {'server_ip': 'X.X.X.X', 'server_port': '22', 'user': 'cisco', 'passwd': 'password'}
router2 = {'server_ip': 'X.X.X.X', 'server_port': '22', 'user': 'cisco', 'passwd': 'password'}
router3 = {'server_ip': 'X.X.X.X', 'server_port': '22', 'user': 'cisco', 'passwd': 'password'}

routers = [router1, router2, router3]
for router in routers:

    client = connect(**router)
    shell = get_shell(client)
    # shell = ssh_client.invoke_shell()
    send_command(shell, 'enable')
    send_command(shell, 'cisco')
    send_command(shell, 'term length 0')
    # send_command(shell, 'sh version')
    send_command(shell, 'sh ip int brief')

    output = show(shell)
    print(output)
    close(client)
