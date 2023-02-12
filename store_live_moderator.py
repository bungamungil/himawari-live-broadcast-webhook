from live_moderator import LiveModerator
import uuid


def store_live_moderator(channel_detail, live_moderator_data):
    print('Moderator %s : %s (%s)' % (
        channel_detail['snippet']['title'],
        live_moderator_data['channelId'],
        live_moderator_data['displayName']
    ))
    moderator = LiveModerator()
    moderator.uuid = uuid.uuid4()
    moderator.owner_channel_id = channel_detail['id']
    moderator.owner_channel_name = channel_detail['snippet']['title']
    moderator.moderator_channel_id = live_moderator_data['channelId']
    moderator.moderator_channel_name = live_moderator_data['displayName']
    moderator.save()
