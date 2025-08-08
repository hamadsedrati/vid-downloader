import pytube as pt
import customtkinter as ctk

try:
    youtube_url = input("Enter the YouTube URL: ")

except KeyboardInterrupt:
    print("Program terminated by user.")
    exit()

except Exception as e:
    print(f"Error: {e}")
    exit()

def download_video(url):
    try:
        yt = pt.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        if stream:
            stream.download()
        else:
            print("No stream found for this video.")
    except Exception as e:
        print(f"Download failed: {e}")

download_video(youtube_url)
