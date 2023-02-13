import time


# Iterate broadcasts
def iterate_broadcasts(youtube_api, broadcast_status, channel_detail, callback):
    request = youtube_api.liveBroadcasts().list(
        part='id,snippet,contentDetails,status',
        broadcastStatus=broadcast_status,
        maxResults=50
    )
    while request:
        response = request.execute()
        for item in response.get('items', []):
            callback(channel_detail, item)
        time.sleep(2)
        request = youtube_api.liveChatMessages().list_next(
            request, response
        )
