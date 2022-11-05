import os
import time

# Start time of the scan
start_time = time.time()

# Enter the network address
Domain = input('Enter the Network address: ')

# Enter the starting network number
start_num = int(input('Enter the Starting Number: '))

#start_ip_arr = (input('Enter the Starting Number:  ')).split('.')
#end_ip_arr = (input('Enter the Last  Number: ')).split('.')

# Enter the last network number
end_num = int(input('Enter the Last  Number: '))

'''Create a file to save the results '''
with open('result_ip_scanner.txt', 'w') as f:
    # Write scanning in progress in the file
    f.write('Scanning in Progress\n')

'''Loop through the network addresses'''
for i in range(start_num, (end_num + 1)):
    '''Split the network address '''
    Domain_splits = Domain.split('.')

    '''Create the hostname'''
    hostname = Domain_splits[0] + '.' + Domain_splits[1] + \
        '.' + Domain_splits[2] + '.' + str(i)
    # Ping the host
    response = os.system('ping -c 2 ' + hostname)
    '''open the file in append mode'''
    try:
        with open('result_ip_scanner.txt', 'a') as f:
            if response == 0:  # If the host is up
                '''Write the host is live in the file'''
                f.write(hostname + ' --> Live\n')

            else:  # If the host is down
                '''Write the host is down in the file'''
                f.write(hostname + ' --> Down\n')
    except Exception as e:
        print(e)


'''Print the time taken to scan the network addresses'''
print(f'scanning complete in {round(time.time() - start_time, 3)} seconds')
