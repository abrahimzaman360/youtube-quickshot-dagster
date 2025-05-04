from dagster import op
from minio import Minio
import json
import io

@op
def save_to_minio(data):
    client = Minio(
        "localhost:9000",
        access_key="u6cjd0aLfJ1HhBL8pInT",
        secret_key="OfASIjz9fzT3Fxdn1O74NPjWp3VinT60y2oZ5V0H",
        secure=False
    )

    bucket = "youtube-raw"
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
