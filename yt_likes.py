from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'AIzaSyAKV3YPounOIQHNNOPnML_ABnv9uO3rqYk'

# Function to fetch views and likes for a YouTube video
def get_video_stats(video_id):
    # Create a YouTube Data API client
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    try:
        # Fetch video statistics
        response = youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        # Extract views and likes from the response
        if 'items' in response and len(response['items']) > 0:
            stats = response['items'][0]['statistics']
            views = int(stats['viewCount'])
            likes = int(stats.get('likeCount', 0))  # Some videos may not have likes count
            return views, likes
        else:
            print("No statistics found for the video.")
            return None, None

    except Exception as e:
        print("Error fetching video statistics:", e)
        return None, None

# Example usage:
if __name__ == "__main__":
    # Replace 'VIDEO_ID' with the ID of the YouTube video you want to fetch statistics for
    video_id = 'J4IvRbhKQ9E'  # Just the ID, not the full URL
    views, likes = get_video_stats(video_id)
    if views is not None and likes is not None:
        print(f"Video ID: {video_id}")
        print(f"Views: {views}")
        print(f"Likes: {likes}")
    
