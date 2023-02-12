# Fetch last broadcast
def fetch_last_broadcast(youtube_api):
    request = youtube_api.liveBroadcasts().list(
        part='id,snippet,contentDetails,status',
        mine=True,
        maxResults=1
    )
    return request.execute().get('items', [])
