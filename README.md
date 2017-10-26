# lambda-rds-operation

This repository is AWS Lambda function's upload files.

## Language

- python3.6.2

## Package

- botocore
- boto3

## How To Use

### 1.clone git repository

```
git clone https://github.com/makaaso/lambda-rds-operation.git
```

### 2.edit tag name

```
cd lambda-rds-operation
vi lambda-rds-operation.py
-----------
set db instance on "<DB_Instance>"
-----------
```

### 3.prepare upload zip file

```
zip -r ../lambda-rds-operation.zip .
```

