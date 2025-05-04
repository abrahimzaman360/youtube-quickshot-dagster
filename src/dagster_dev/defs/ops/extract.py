from dagster import op
from googleapiclient.discovery import build
from ..config.load_env import youtube_api_key

@op
def fetch_youtube_data():
    """
    Fetches data from the YouTube API.

    using Query: 
    Param:
        query
    """
    query = "Python Programming"

    youtube = build("youtube", "v3", developerKey=youtube_api_key)
    request = youtube.search().list(
        part="snippet",
        q=query,
        maxResults=30
    )

    response = request.execute()
    return response["items"]
