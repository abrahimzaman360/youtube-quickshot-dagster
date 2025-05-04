import os

# Load environment variables
youtube_api_key = os.getenv('YOUTUBE_API_KEY')

minio_access_key = os.getenv('MINIO_ACCESS_KEY')
minio_secret_key = os.getenv('MINIO_SECRET_KEY')
minio_endpoint = os.getenv('MINIO_ENDPOINT')
minio_bucket = os.getenv('MINIO_BUCKET')

postgres_user = os.getenv('POSTGRES_USER') 
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_host = os.getenv('POSTGRES_HOST')
postgres_port = os.getenv('POSTGRES_PORT')
postgres_db = os.getenv('POSTGRES_DB')