# Fetch channel detail
def fetch_channel_detail(youtube_api):
    request = youtube_api.channels().list(
        part='id,snippet,status',
        mine=True,
        maxResults=1
    )
    return request.execute().get('items', [])
