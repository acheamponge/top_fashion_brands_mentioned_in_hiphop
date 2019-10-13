import lyricsgenius as genius

api = genius.Genius("esd3Wcql14aTFzENxk4lWMCFVowq_e5nUbyzrEbJ1hnw9xiX_b3F__9almjyhOn5")



list = [
'Drake']

for i in list:
    artist = api.search_artist(i,max_songs=119, sort="title")
    artist.save_lyrics()
