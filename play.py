import pexpect

def song (song):
    print(f'Playing:\n{song}')
    play = pexpect.spawn(f'mplayer -really-quiet -novideo "{song}"')
    play.interact()

def album (album):
    for track in album:
        song(track)
