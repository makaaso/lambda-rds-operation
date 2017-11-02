#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# lambda-rds-stop.py

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

    """ Stop RDS Instance """
    try:
        client.stop_db_instance(DBInstanceIdentifier=os.environ['TAG_NAME'])
    except:
        print('Stop RDS Error')
        return 1

    return 0
