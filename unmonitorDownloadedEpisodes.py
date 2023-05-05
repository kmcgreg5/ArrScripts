from pyarr import SonarrAPI
from sys import argv

def unmonitor_all_downloaded(host, api_key):
    def __unmonitor(episode):
        episode['monitored'] = False
        sonarr.upd_episode(episode['id'], {"monitored": False})
        counter[series['title']] = counter.get(series['title'], 0) + 1

    sonarr = SonarrAPI(host, api_key)
    series_list = sonarr.get_series()
    counter = {}
    try:
        for series in series_list:
            episodes = sonarr.get_episode(series['id'], True)
            print(episodes)
            #[__unmonitor(episode) for episode in episodes if episode['hasFile'] and episode['monitored']]
                    
    finally:
        print('\nUnmonitored:')
        [print(f'\t{title}: {count} episodes') for title, count in counter.items()]


def main():
    if len(argv) < 3:
        print("Usage: python unmonitor-downloaded-episodes.py baseURL API-KEY")
        return

    api_key = argv[2]
    host = argv[1]
    unmonitor_all_downloaded(host, api_key)


if __name__ == "__main__":
    main()