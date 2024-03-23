from pytube import YouTube

def download_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        if stream:
            print("Downloading video:", yt.title)
            stream.download(output_path)
            print("Video downloaded successfully to:", output_path)
        else:
            print("Error: No stream available for the given video URL.")
    except Exception as e:
        print("Error occurred:", str(e))

if __name__ == "__main__":
    # Example usage:
    video_url = "https://youtu.be/mtdrCqU58rE?si=HzoLUDBZE0Z1lI9M"
    output_path = "/var/lib/jenkins/workspace/stube/"
    download_video(video_url, output_path)

    
