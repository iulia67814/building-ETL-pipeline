## ETL Pipeline

An ETL pipeline is a set of processes to extract data from one system, transform it, and load it into a target repository.

### Introduction

Building an ETL pipeline that carries out the following tasks:

- Extracts transactional data of 400k invoices from Redshift
- Transforms the data by identifying and removing duplicates
- Transforms the invoice_date field by fixing the data type
- Loads the transformed data to an AWS S3 bucket

### Requirements

The minimum requirements:
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/docker-for-mac/install/)
- Docker for Windows:
Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)

### Instructions

Copy the ``.env.example`` file to `.env` and fill out the environment vars.

Make sure you are executing the code from the etl_pipeline folder. 

To run it locally first build the image.

```bash
  docker image build -t etl-pipeline:0.1 .
```

Then run the job:
```bash
  docker run --env-file .env etl-pipeline:0.1
```