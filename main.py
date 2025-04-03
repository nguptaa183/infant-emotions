from googleapiclient.discovery import build

API_KEY = "YOUR_YOUTUBE_API_KEY"
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)

def search_videos(query, max_results=10):
    request = YOUTUBE.search().list(
        q=query,
        part="snippet",
        maxResults=max_results,
        type="video",
        videoLicense="creativeCommon",  # Only Creative Commons (CC BY) videos
        videoDuration="short"  # Videos under 4 minutes
    )
    response = request.execute()
    
    video_data = []
    for item in response.get('items', []):
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_data.append({"title": title, "url": video_url})
    
    return video_data

videos = search_videos("infant emotions")
for video in videos:
    print(video)
