# Remove all instances of WUB in a string and return single space separated characters that remain
# This is a CodeWars challenge


def song_decoder(song):
    song = song.replace("WUB", " ")
    song = " ".join(song.split())
    return song


print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))
