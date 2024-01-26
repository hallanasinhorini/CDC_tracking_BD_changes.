import os
import sys
import pymysql

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]  

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 3306:3606 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=myluke -d mysql', 'mysql')
    sys.exit()

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('final_mysql_container')
    delete('final_mongo_container')
    delete('final_redis_container')
    delete('final_cassandra_container')
    sys.exit()

