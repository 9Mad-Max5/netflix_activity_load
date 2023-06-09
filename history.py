

from helpers import authenticate
from trakt import Trakt

from datetime import datetime
import logging
import os
from login_details import client_id, client_secret

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    # Configure
    # Trakt.configuration.defaults.client(
    #     id=os.environ.get('CLIENT_ID'),
    #     secret=os.environ.get('CLIENT_SECRET')
    # )
    Trakt.configuration.defaults.client(
        id=client_id,
        secret=client_secret
    )

    # Authenticate
    Trakt.configuration.defaults.oauth.from_response(
        authenticate()
    )

    now = datetime.utcnow()

    # Retrieve 10 history records (most recent)
    for item in Trakt['sync/history'].get(per_page=10):
        print(' - %-120s (watched_at: %r)' % (
            repr(item),
            item.watched_at.strftime('%Y-%m-%d %H:%M:%S')
        ))

    print('=' * 160)

    # Retrieve history records for "Family Guy"
    for item in Trakt['sync/history'].shows('1425', pagination=True, per_page=25):
        print(' - %-120s (watched_at: %r)' % (
            repr(item),
            item.watched_at.strftime('%Y-%m-%d %H:%M:%S')
        ))

    print('=' * 160)

    # Retrieve history records for this year
    for item in Trakt['sync/history'].get(pagination=True, per_page=25, start_at=datetime(now.year, 1, 1)):
        print(' - %-120s (watched_at: %r)' % (
            repr(item),
            item.watched_at.strftime('%Y-%m-%d %H:%M:%S')
        ))

    print('=' * 160)

    # Retrieve all history records
    for item in Trakt['sync/history'].get(pagination=True, per_page=25):
        print(' - %-120s (watched_at: %r)' % (
            repr(item),
            item.watched_at.strftime('%Y-%m-%d %H:%M:%S')
        ))
