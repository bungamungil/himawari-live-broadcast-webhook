import argparse

from googleapiclient.errors import HttpError

import fetch_user_credential as auth
from errors import ChannelDetailNotFound
from fetch_channel_detail import fetch_channel_detail
from handle_broadcast_item import handle_broadcast_item
from iterate_broadcasts import iterate_broadcasts

parser = argparse.ArgumentParser()
parser.add_argument('--credential', '-c', help='Use credential file')
parser.add_argument('--status', '-s', help='Broadcast status', default='active')
args = parser.parse_args()


# Main function
if __name__ == '__main__':
    arg_credential = args.credential
    arg_status = args.status
    youtube_api = auth.fetch_user_credential(arg_credential)
    try:
        channel_details = fetch_channel_detail(youtube_api)
        if len(channel_details) > 0:
            channel_detail = channel_details[0]
        else:
            raise ChannelDetailNotFound
        iterate_broadcasts(youtube_api, arg_status, channel_detail, handle_broadcast_item)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    except ChannelDetailNotFound:
        print("Channel detail not found")
