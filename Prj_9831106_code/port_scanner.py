from socket import *
import time

# Start time of the scan
start_time = time.time()

# Enter the IP address of the remote_host
remote_host = input('Enter the remote host IP scan: ')

# Get the IP address of the remote_host
rh_IP = gethostbyname(remote_host)

# Enter the start port number
start_num = int(input('Enter the start port number:  '))

# Enter the last port number
end_num = int(input('Enter the last port number:  '))
print('************************************')

'''Print the IP address of the remote_host'''
print('Scanner is working on : ', rh_IP)

print('************************************')

'''Loop through the ports'''
for i in range(start_num, (end_num + 1)):
    '''Create a socket object'''
    s = socket(AF_INET, SOCK_STREAM)
    '''Check if the port is open'''
    res = s.connect_ex((rh_IP, i))
    # try:
    with open('result_port_scanner.txt', 'a') as f:
        if(res == 0):  # If the port is open
            # Print the open port
            print('Port Open:-->     %d' % (i,))
            f.write('Port Open:-->     %d\n' % (i,))

    # except Exception as e:
    # 	print(e)

   # Close the socket
    s.close()

# Print the time taken to scan the ports
print(f'scanning complete in {round(time.time() - start_time, 3)} seconds')
