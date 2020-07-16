import pexpect

def song (song):
    if song:
        print(f'\nPlaying:\n{song}')
        play = pexpect.spawn(f'mplayer -really-quiet -novideo "{song}"')
        play.interact()

def album (album):
    if album:
        for track in album:
            song(track)
