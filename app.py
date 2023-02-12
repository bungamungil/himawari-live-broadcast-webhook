from googleapiclient.errors import HttpError
import fetch_user_credential as auth
from fetch_channel_detail import fetch_channel_detail
from clear_live_moderators import clear_live_moderators
from fetch_last_broadcast import fetch_last_broadcast
from iterate_live_moderator import iterate_live_moderator
from store_live_moderator import store_live_moderator
from errors import ChannelDetailNotFound, LastBroadcastNotFound
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--credential', '-c', help='Use credential file')
args = parser.parse_args()


# Main function
if __name__ == '__main__':
    arg_credential = args.credential
    youtube_api = auth.fetch_user_credential(arg_credential)
    try:
        channel_details = fetch_channel_detail(youtube_api)
        if len(channel_details) > 0:
            channel_detail = channel_details[0]
        else:
            raise ChannelDetailNotFound
        clear_live_moderators(channel_detail['id'])
        last_broadcasts = fetch_last_broadcast(youtube_api)
        if len(last_broadcasts) > 0:
            live_chat_id = last_broadcasts[0]['snippet']['liveChatId']
            iterate_live_moderator(youtube_api, channel_detail, live_chat_id, store_live_moderator)
        else:
            raise LastBroadcastNotFound
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    except ChannelDetailNotFound:
        print("Channel detail not found")
    except LastBroadcastNotFound:
        print("Last broadcast not found")
