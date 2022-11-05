import os

parameter = 6

hostname = input('Please Enter IP/Domain: ')  # example: www.google.com
response = os.system('ping -c ' + str(parameter) +
                     ' ' + hostname)   # ping 2 times

try:
    with open('result_ping.txt', 'w') as f:  # create file
        if response == 0:  # if ping is ok
            f.write(hostname + ' -->  Up\n')  # write to file
        else:  # if ping is not ok
            f.write(hostname + ' --> Down\n')  # write to file

except Exception as e:
    print("Invalid Hostname")
    print(e)
