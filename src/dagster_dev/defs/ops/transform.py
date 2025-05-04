from dagster import op
import pandas as pd

@op
def transform_youtube_data(data):
    rows = []
    for video in data:
        snippet = video.get("snippet", {})
        stats = video.get("statistics", {})
        rows.append({
            "title": snippet.get("title"),
            "views": int(stats.get("viewCount", 0)),
            "likes": int(stats.get("likeCount", 0)),
            "published_at": snippet.get("publishedAt"),
        })
    return pd.DataFrame(rows)
