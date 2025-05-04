from dagster import job, ScheduleDefinition, Definitions
from .ops.extract import fetch_youtube_data
from .ops.load_minio import save_to_minio
from .ops.transform import transform_youtube_data
from .ops.load_postgres import load_to_postgres

@job(metadata={"owner": "data-team", "description": "ETL job for YouTube data"})
def youtube_etl_job():
    data = fetch_youtube_data()
    save_to_minio(data)
    df = transform_youtube_data(data)
    load_to_postgres(df)



daily_schedule = ScheduleDefinition(
    job=youtube_etl_job,
    cron_schedule="*/2 * * * *",  # Runs every 2 minute
    execution_timezone="UTC",
)


defs = Definitions(
    jobs=[youtube_etl_job],
    schedules=[daily_schedule],
)