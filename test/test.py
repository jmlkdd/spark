# coding=utf-8

from pyspark import SparkContext, SparkConf

# conf = SparkConf().setAppName('wordcount').setMaster('spark://10.10.10.196:7077')
conf = SparkConf().setAppName('wordcount').setMaster('local')
sc = SparkContext(conf=conf)
