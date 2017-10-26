#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# lambda-rds-operation

This repository is AWS Lambda function's upload files.
"""

__authour__ = "masaru.kawabata"
__version__ = 1.1

import botocore
import boto3

def rds_start(event, context):
    """ Create Connection """
    try:
        client = boto3.client('rds', region_name='ap-northeast-1')
    except:
        print('Connection Error')
        return 1

    """ Start RDS Instance """
    try:
        client.start_db_instance(DBInstanceIdentifier="<DB_Instance>")
    except: 
        print('Start RDS Error')
        return 1

    return 0

def rds_stop(event, context):
    """ Create Connection """
    try:
        client = boto3.client('rds', region_name='ap-northeast-1')
    except:
        print('Connection Error')
        return 1

    """ Stop RDS Instance """
    try:
        response = client.stop_db_instance(DBInstanceIdentifier="<DB_Instance>")
        print(response)
    except:
        print('Stop RDS Error')
        return 1

    return 0
