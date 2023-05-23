from trakt import Trakt
from helpers import authenticate

from login_details import client_id, client_secret

Trakt.configuration.defaults.client(
    id=client_id,
    secret=client_secret
)

# Authenticate
Trakt.configuration.defaults.oauth.from_response(
    authenticate()
)

for item in Trakt['sync/history'].get(per_page=10):
        print(' - %-120s (watched_at: %r)' % (
            repr(item),
            item.watched_at.strftime('%Y-%m-%d %H:%M:%S')
        ))
        # print(item)