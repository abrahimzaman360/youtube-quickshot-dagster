from dagster import op
from googleapiclient.discovery import build

@op
def fetch_youtube_data():
    api_key = "AIzaSyCxjRENHyVmbqeZALFmqaDK62QrEGa6FcM"
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id="Ks-_Mh1QhMc"
    )
    response = request.execute()
    return response["items"]
