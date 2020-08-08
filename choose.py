from subprocess import Popen, PIPE
import pexpect
import os
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()

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

def directory ():
    directories = []
    for root, dirs, files in os.walk('.'):
        directories.append(root)
    dir = fzf.prompt(directories)[0]
