from subprocess import Popen, PIPE
import pexpect
import os

def song ():
    song = Popen(['fzf'],
        stdout=PIPE,
        universal_newlines=True).communicate()[0].strip()
    return song

def album ():
    album = Popen(['fzf'],
        stdout=PIPE,
        universal_newlines=True).communicate()[0].strip()
    if album:
        albumDir = os.path.dirname(album)
        songList = sorted(os.listdir(albumDir))
        return list(map(lambda song:albumDir+'/'+song, songList))

# def song ():
#     choice = pexpect.spawn('/bin/fzf')
#     choice.interact()
#     return choice.read()

# def album ():
#     command = 'find ./ -type d | fzf'
#     album = pexpect.spawn('/bin/bash', ['-c', command])
#     album.interact()
#     return album
