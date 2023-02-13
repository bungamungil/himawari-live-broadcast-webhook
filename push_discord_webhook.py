import json

import requests
from config import read_config


def push_discord_webhook(**kwargs):
    webhook_url = read_config()['webhook_url']
    data = {
        'embeds': [
            {
                'title': kwargs['title'],
                'description': kwargs['description'],
                'url': kwargs['embed_url'],
                'color': kwargs['color'],
                'image': {
                    'url': kwargs['thumbnail_url']
                },
                'footer': {
                    'text': kwargs['footer_text'],
                },
                'author': {
                    'name': kwargs['author_name'],
                    'url': kwargs['author_url'],
                    'icon_url': kwargs['author_icon_url']
                }
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    return requests.post(webhook_url, headers=headers, data=json.dumps(data))
