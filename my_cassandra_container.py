import os
import sys
from cassandra.cluster import Cluster

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
    create('docker run -p 9042:1000 --name final_cassandra_container -d cassandra', 'cassandra')
    sys.exit()