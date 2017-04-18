# coding=utf-8

from pyhdfs import HdfsClient
import pyhdfs

client = HdfsClient(hosts='10.10.10.196', user_name='root')
print client.list_status('/')
print client.get_home_directory()
print client.listdir('/data')
print pyhdfs.FileStatus()
# client.mkdirs('/spark/test')
print client.listdir('/')
print client.get_file_status('/hbase')
