import time


# Iterate live moderator
def iterate_live_moderator(youtube_api, channel_detail, live_chat_id, callback):
    request = youtube_api.liveChatModerators().list(
        part='id,snippet',
        liveChatId=live_chat_id,
        maxResults=50
    )
    while request:
        response = request.execute()
        for item in response.get('items', []):
            callback(channel_detail, item['snippet']['moderatorDetails'])
        time.sleep(2)
        request = youtube_api.liveChatMessages().list_next(
            request, response
        )
