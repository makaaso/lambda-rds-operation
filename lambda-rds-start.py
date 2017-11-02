#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# lambda-rds-start.py

This repository is AWS Lambda function's upload files.
"""

__authour__ = "masaru.kawabata"
__version__ = 1.2

import botocore
import boto3
import os

def lambda_handler(event, context):
    """ Create Connection """
    try:
        client = boto3.client('rds', region_name='ap-northeast-1')
    except:
        print('Connection Error')
        return 1

    """ Start RDS Instance """
    try:
        client.start_db_instance(DBInstanceIdentifier=os.environ['TAG_NAME'])
    except: 
        print('Start RDS Error')
        return 1

    return 0

