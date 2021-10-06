import os
import time

# Start the timer to see how long our program runs
start_timer = time.time()

# Fake loading technique -- often used for 'realistic timing'
print("[+] Initializing..")

# Setup a Set of songs to ensure no duplicates
print("[+] Setting up local variables..")
set_of_songs = set()

# Load our URLs from songs.txt into our Set
print("[+] Collecting URLs for download..")
try:
    songs = open("./songs.txt")
except:
    print("    [-] Cant find songs.txt -- Make sure all files exist before running me!")
    exit()


# Loop through each URL and add to the Set
for song in songs:
    if song == "":
        print("    [-] You need to add URLs, 1 per line in the songs.txt file!")
        exit()
    print(f"    [+] Attempting to pull: {song}")
    try:
        set_of_songs.add(song.rstrip())
    except:
        print("    [-] Error adding URL to set.")
        print(f"    [-] Error URL: {song}")
    print("    [+] Looking for next song..")

print("[+] Finished Song Harvesting")
print(f"[+] Current Song List ({len(set_of_songs)} songs): {set_of_songs}")
print("[+] Preparing to download and convert to MP3..")

# Download and extract via youtube-dl
# https://ytdl-org.github.io/youtube-dl/index.html
def extract_mp3(url):
    print(f"    [+] Extracting url.. {url}")
    try:
        os.system(f"youtube-dl --extract-audio --audio-format mp3 {url}")
    except:
        print(f"    [-] Error extracting url: {url}")

for url in set_of_songs:
    extract_mp3(url)

# Finish our program and wrap up
songs.close()
end_timer = time.time() - start_timer

# If seconds go over minutes convert to minutes
if end_timer > 60:
    end_timer /= 60 
    print(f"[+] Program has finshed in {end_timer} minutes. Enjoy.")
else:
    print(f"[+] Program has finshed in {end_timer} seconds. Enjoy.")
    