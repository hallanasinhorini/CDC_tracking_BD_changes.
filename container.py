import os
import sys
import pymysql 
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

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# initialize mysql db
def init_mysql():
    cnx = pymysql.connect(user='root', 
        password='myluke',
        host='127.0.0.1')

    # create cursor
    cursor = cnx.cursor()

    # delete previous db
    query = ("DROP DATABASE IF EXISTS `pluto`;")
    cursor.execute(query)

    # create db
    query = ("CREATE DATABASE IF NOT EXISTS pluto")
    cursor.execute(query)

    # use db
    query = ("USE pluto")
    cursor.execute(query)

    # create table
    query = ('''
    CREATE TABLE posts(
        id VARCHAR(36),
        stamp VARCHAR(20)
    )
    ''')
    cursor.execute(query)

    # clean up
    cnx.commit()
    cursor.close()
    cnx.close()    
  

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 3306:3306 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=myluke -d mysql', 'mysql')
    create('docker run -p 1000:1000 --name final_cassandra_container -d cassandra', 'cassandra')
    create('docker run -p 1800:1800 --name final_mongo_container -d mongo', 'mongo')
    create('docker run -p 2400:2400 --name final_redis_container -d redis', 'redis')
    sys.exit()

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('final_mysql_container')
    delete('final_mongo_container')
    delete('final_redis_container')
    delete('final_cassandra_container')
    sys.exit()

# if -init, init mysql, mongodb does not need it
if(argument == '-init'):
    init_mysql()
    sys.exit()