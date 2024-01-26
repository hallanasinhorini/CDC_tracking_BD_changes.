import os
import sys

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]  

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 6379:2400 --name final_redis_container -d redis', 'redis')
    sys.exit()