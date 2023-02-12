from peewee import Model, CharField, DateTimeField
from database import db
import datetime


class LiveModerator(Model):
    uuid = CharField(index=True)
    owner_channel_id = CharField()
    owner_channel_name = CharField()
    moderator_channel_id = CharField()
    moderator_channel_name = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = "live_moderators"
