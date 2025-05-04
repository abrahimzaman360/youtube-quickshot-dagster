# Getting Hands Dirty with Dagster 101

## Youtube Pipeline (ETL):

This is absolutely simple ETL pipeline that pulls data from youtube api,
stores raw information in MinIO storage and then transforms that data and then 
stores it in Postgres.

It's like:
Source (YT) [E] -> MinIO (Raw Storage) -> Transformation [T] -> Postgres [L]


### To run the pipeline:
first install the uv and then setup virtual environment:

```shell
uv venv # Optional if already have a virtual environment
uv sync --all-groups # Installing required packages
```

### Run dagster webserver using:

Dagster (new experimental tool) dg needs to be installed:
(dg)[https://docs.dagster.io/guides/labs/dg/]


```shell
dg dev # Start Dagster webserver
```


### Manually Running the Job:

Go to Job Section and Select `Youtube ETL ...`,
And then Run Click