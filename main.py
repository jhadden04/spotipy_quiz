import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import random

os.environ["SPOTIPY_CLIENT_ID"] = '*'
os.environ["SPOTIPY_CLIENT_SECRET"] = '*'
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:8080'
username = "*"
device_id = '*'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


# customised playlist questions
# 1. Artist's name from song 2. exact song name from preview 3. the first song on the playlist
# 4. The last song on the playlist 5. Most popular song on the playlist 5. time signature from preview
# 6. name of album from song name

def q1():
    global score, track, playlist_info
    rand_int = random.randint(1, len(playlist_info["tracks"]["items"]))
    track = (playlist_info["tracks"]["items"][rand_int]["track"])
    while track["preview_url"] is None:
        rand_int -= 1
        track = (playlist_info["tracks"]["items"][rand_int]["track"])

    answer_1 = input(f'1) What is the name of the artist who sings this song ({track["preview_url"]})?: ')
    if answer_1 == track["artists"][0]["name"]:
        print(f'Correct!')
        score += 1
    else:
        print(f'Wrong, it was {track["artists"][0]["name"]}')


def q2():
    global score, playlist_info, track
    rand_int = random.randint(1, len(playlist_info["tracks"]["items"]))
    track = (playlist_info["tracks"]["items"][rand_int]["track"])
    while track["preview_url"] is None:
        rand_int -= 1
        track = (playlist_info["tracks"]["items"][rand_int]["track"])
    answer_2 = input(f'2) What is the name of this song ({track["preview_url"]})?: ')
    if answer_2 == track["name"]:
        print(f'Correct')
        score += 1
    else:
        print(f'Wrong it was {track["name"]}')


def q3():
    global score, playlist_info
    answer_3 = input(f'3) What is the first song of the playlist: ')
    if answer_3 == (playlist_info["tracks"]["items"][0]["track"]):
        print("Correct")
        score += 1
    else:
        print(f'Wrong, it was {(playlist_info["tracks"]["items"][0]["track"]["name"])}')


def q4():
    global score, playlist_info
    answer_4 = input(f'4) What is the last song of the playlist: ')
    if answer_4 == (playlist_info["tracks"]["items"][-1]["track"]):
        print("Correct")
        score += 1
    else:
        print(f'Wrong, it was {(playlist_info["tracks"]["items"][-1]["track"]["name"])}')


def q5():
    global playlist_info, score
    most_popular_int = 0
    most_popular = ''
    for i in range(len(playlist_info["tracks"]["items"])):
        if playlist_info["tracks"]["items"][i]["track"]["popularity"] > most_popular_int:
            most_popular = playlist_info["tracks"]["items"][i]["track"]["name"]
            most_popular_int = playlist_info["tracks"]["items"][i]["track"]["popularity"]
        else:
            continue
    answer_5 = input("5) What is the most popular song on this playlist: ")
    if answer_5 == most_popular:
        print("Correct")
        score += 1
    else:
        print(f'Wrong, it was {most_popular}')


def q6():
    global score, playlist_info
    rand_int = random.randint(1, len(playlist_info["tracks"]["items"]))
    track = (playlist_info["tracks"]["items"][rand_int]["track"])
    while track["preview_url"] is None:
        rand_int -= 1
        track = (playlist_info["tracks"]["items"][rand_int]["track"])
    answer_6 = input(f'6) What is the album name of this song ({track["name"]}): ')
    if answer_6 == track["album"]["name"]:
        print("Correct")
        score += 1
    else:
        print(f'Wrong, it was {track["album"]["name"]}')


def playlist_quiz():
    global playlist_ID, score_additions
    global playlist_info
    global score
    global track
    playlist_ID = input("spotify uri: ")[17:]
    playlist_info = spotify.playlist(playlist_ID)
    score = 0
    rand_int = random.randint(1, len(playlist_info["tracks"]["items"]))
    track = (playlist_info["tracks"]["items"][rand_int]["track"])
    q1()
    q2()
    q3()
    q4()
    q5()
    score_additions = 0
    (score_additions) = (input("If you have been unfairly cheated of some points (capital letters etc.), type how "
                               "many more points you need: "))
    try:
        score += int(score_additions)
    except:
        score = score


playlist_quiz()
