from dagster import op
from sqlalchemy import create_engine
from ..config.load_env import postgres_user, postgres_password, postgres_host, postgres_port, postgres_db

@op
def load_to_postgres(df):
    engine = create_engine(f"postgresql+psycopg://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}")
    df.to_sql("youtube_videos", engine, if_exists="replace", index=False)
