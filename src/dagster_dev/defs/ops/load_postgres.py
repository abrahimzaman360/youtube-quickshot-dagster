from dagster import op
from sqlalchemy import create_engine

@op
def load_to_postgres(df):
    engine = create_engine("postgresql+psycopg://mrtux:mrtux360@localhost:5432/etl-db")
    df.to_sql("youtube_videos", engine, if_exists="replace", index=False)
