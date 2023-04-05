## ETL Pipeline

### Introduction

### Requirements
The minimum requirements:
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/docker-for-mac/install/)

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