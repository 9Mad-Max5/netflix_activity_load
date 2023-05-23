import trakt.core
import trakt.sync
import trakt.tv
import os
from datetime import datetime
from login_details import client_id, client_secret, username, application_id

# trakt.APPLICATION_ID = application_id
# trakt.init()
# trakt.get_device_token

# to get an id for your app, visit https://trakt.tv/oauth/applications
# trakt.core.AUTH_METHOD = trakt.core.DEVICE_AUTH
# trakt.init(client_id=client_id, client_secret=client_secret, store=True)
# trakt.init(store=True)
# if not os.path.isfile("~/.pytrakt.json"):
# else:
#     trakt.init(username="9_Mad-Max_5", store=True)
# trakt.device_auth(client_id=client_id, client_secret=client_secret, acce)
# trakt.
# print(trakt.sync.get_watched())
# Beispiel: Hinzufügen einer Episode zum Verlaufsstatus (History)
# show_id = 'SHOW_ID'  # ID der Serie
# season = 1  # Staffelnummer
# episode = 1  # Episodennummer

# # Hinzufügen der Episode zum Verlaufsstatus
# trakt.sync.add_to_history('episodes', show_id, season, episode)
# print(trakt.tv.watched_shows())

# as there is no information about the actual played time this seams to be the best approach with fixed time
time_watched = "20:15:00"

# res = trakt.sync.search("Physical: 100", search_type="show")
res = trakt.sync.search("Verlust und Niederlage", search_type="episode")
print(res)
for s in res:
    print(s)
    if s.title == "Physical: 100":
        print(s.episodes)
# episode = trakt.tv.TVEpisode(show="Physical: 100", season=1, number=1)
# watched_at = datetime.strptime(date + " " + time_watched, '%d.%m.%y %H:%M:%S')
# trakt.sync.add_to_history(media=episode, watched_at=watched_at)