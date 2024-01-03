# first signup in https://genius.com
# then go to http://genius.com/api-clients and create your API
# install lyricsgenius pakage
# pip install lyricsgenius
# enjoy :)

import lyricsgenius
api_key = '[your_api_key]'
genius = lyricsgenius.Genius(api_key)
artist_name = "Shayea"
song_name = "Seyl"
artist = genius.search_artist(artist_name,
                              max_songs=5,sort="title")
song = artist.song(song_name)
with open(f"{song_name}_{artist_name}.txt", "w", encoding="utf-8") as f:
    f.write(song.lyrics)
