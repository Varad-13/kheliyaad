import re

def extract_youtube_id(url):
    # Regular expression to match YouTube video IDs
    pattern = r'(?:v=|\/v\/|embed\/|youtu\.be\/|\/shorts\/|\/watch\?v=|\/watch\?.+&v=)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None
