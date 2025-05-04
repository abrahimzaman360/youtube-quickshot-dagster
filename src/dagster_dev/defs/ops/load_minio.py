from dagster import op
from minio import Minio
import json
import io
from ..config.load_env import minio_endpoint, minio_access_key, minio_secret_key, minio_bucket

@op
def save_to_minio(data):
    client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False
    )

    bucket = minio_bucket
    key = "video_data.json"
    content = json.dumps(data).encode("utf-8")

    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)

    client.put_object(
        bucket,
        key,
        io.BytesIO(content),
        length=len(content),
        content_type="application/json"
    )
    return f"s3://{bucket}/{key}"
