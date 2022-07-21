from pyarr import RadarrAPI
from sys import argv

def unmonitor_all_downloaded(host, api_key):
    def __unmonitor(movie):
        movie['monitored'] = False
        radarr.upd_movie(movie)
        print(f'\t{movie["title"]}')

    radarr = RadarrAPI(host, api_key)
    movies_list = radarr.get_movie()
    print("Unmonitored:")
    [__unmonitor(movie) for movie in movies_list if movie['hasFile'] and movie['monitored']]

def main():
    if len(argv) < 3:
        print("Usage: python unmonitor-downloaded-movies.py baseURL API-KEY")
        return

    API_KEY = argv[2]
    host = argv[1]
    unmonitor_all_downloaded(host, API_KEY)

if __name__ == "__main__":
    main()