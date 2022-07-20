from pyarr import SonarrAPI
from sys import argv
from time import time

def unmonitor_all_downloaded(host, api_key):
    def __unmonitor(episode):
        episode['monitored'] = False
        sonarr.upd_episode(episode['id'], episode)
        counter[series['title']] = counter.get(series['title'], 0) + 1

    start = time()
    sonarr = SonarrAPI(host, api_key)
    series_list = sonarr.get_series()
    counter = {}
    try:
        for series in series_list:
            episodes = sonarr.get_episodes_by_series_id(series['id'])
            episodes = [__unmonitor(episode) for episode in episodes if episode['hasFile'] and episode['monitored']]
                    
    finally:
        print('Unmonitored:')
        [print(f'\t{title}: {count} episodes') for title, count in counter.items()]
        print(f'\n\nElapsed Time: {time()-start:.2f} seconds')

def main():
    if len(argv) < 3:
        print("Usage: python unmonitor-downloaded-episodes.py baseURL API-KEY")
        return

    API_KEY = argv[2]
    host = argv[1]
    unmonitor_all_downloaded(host, API_KEY)


if __name__ == "__main__":
    main()