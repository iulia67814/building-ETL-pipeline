## ETL Pipeline

An ETL pipeline is a set of processes to extract data from one system, transform it, and load it into a target repository.

### What was done?

Was built an ETL pipeline that carries out the following tasks:

- Extracts transactional data of 400k invoices from Redshift
- Transforms the data by identifying and removing duplicates
- Transforms the invoice_date field by fixing the data type
- Loads the transformed data to an AWS S3 bucket

### Requirements

To upload Docker on your machine:
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/docker-for-mac/install/)
- Docker for Windows: [Docker](https://docs.docker.com/desktop/install/windows-install/)
- 
### Why Docker?
Docker is a platform designed to help developers build, share, and run modern applications inside isolated containers.
- to make sure that my code will work on any machine -

## Instructions

### How do I use .env variables?

You just create a new file called . env in your project and slap your variables in there on different lines. 
To read these values, there are a couple of options, but the easiest is to use the dotenv package from npm. 
Then you just require that package in your project wherever you need to use environment variables.

Copy the ``.env.example`` file to `.env` and fill out the environment variables. (An environment variable is a dynamic-named value that can affect the way running processes will behave on a computer. 
Environment variables are part of the environment in which a process runs.)

!Make sure you are executing the code from the etl_pipeline folder!

###To run it locally first build the image.

```bash
  docker image build -t etl-pipeline:0.1 .
```

Then run the job:
```bash
  docker run --env-file .env etl-pipeline:0.1
```