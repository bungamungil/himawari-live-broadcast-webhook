from live_moderator import LiveModerator


# Clear live moderators
def clear_live_moderators(channel_id):
    LiveModerator.delete().where(LiveModerator.owner_channel_id == channel_id).execute()
