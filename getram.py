import os
import time


def getram():
    ''' Get the Machine's available RAM (Linux)
    '''
    # Try to read in the meminfo file:
    try:
        with open('/proc/meminfo') as f:
            meminfo = f.read()
    except IOError:
        # todo: try a different method of getting RAM here, since this is being
        # run on a non-Linux computer
        raise Exception('File "/proc/meminfo" Unavailable')

    # Parse meminfo file:
    for line in meminfo.split('\n'):
        if 'MemAvailable' in line:
            ram = int(line.split(' ')[-2]) / 1028
            timestamp = int(time.time())
            return timestamp, ram

    # Parsing failed:
    raise Exception('MemAvailable Couldnt be Parsed from /proc/meminfo')

def getrow():
    ''' Return
    '''
    return '%s,%sMB\n' % getram()

def writerow():
    ''' Write a timestamp/RAM row to the ram.csv
    '''
    if os.path.exists('./ram.csv'):
        with open('./ram.csv', 'a') as f:
            f.write(getrow())
    else:
        print 'Creating ram.csv...'
        with open('./ram.csv', 'w') as f:
            f.write('Timestamp,RAM\n')
            f.write(getrow())



if __name__ == '__main__':
    writerow()
