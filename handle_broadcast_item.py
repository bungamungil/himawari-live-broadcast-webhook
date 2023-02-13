from dateutil import parser, tz
from time_locale import months, days


# Handle broadcast item
def handle_broadcast_item(channel, broadcast):
    # Todo store to db and push to webhook
    if is_valid_broadcast_to_proceed(broadcast):
        print('Title       : %s' % broadcast['snippet']['title'])
        print('URL         : https://www.youtube.com/watch?v=%s' % broadcast['id'])
        print('Schedule    : %s' %
              print_datetime(convert_timezone(broadcast['snippet']['scheduledStartTime']))
              )
        print('Thumbnail   : https://i.ytimg.com/vi/%s/maxresdefault_live.jpg' % broadcast['id'])
        print('Description : %s' % broadcast['snippet']['description'].split('\n')[0])
        print('---\n')


# Check if the broadcast is valid to proceed
def is_valid_broadcast_to_proceed(broadcast):
    return broadcast['snippet']['isDefaultBroadcast'] is False \
           and 'scheduledStartTime' in broadcast['snippet'] \
           and broadcast['status']['privacyStatus'] == 'public'


# Convert string datetime from UTC to desired timezone
def convert_timezone(src_time_str):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Jakarta')
    utc = parser.parse(src_time_str).replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)


# Print datetime to desired format
def print_datetime(dt):
    weekday_index = int(dt.strftime('%w'))
    month_index = int(dt.strftime('%m')) - 1
    day_of_month = int(dt.strftime('%d'))
    year = int(dt.strftime('%Y'))
    time_str = dt.strftime('%H:%M:%S %Z')
    return '%s, %s %s %s - %s' % (days[weekday_index], day_of_month, months[month_index], year, time_str)
