import urllib.parse

def build_url(*segments):
    """
    Builds a full URL from segments without percent-encoding any part of it.
    
    Args:
    *segments (str): Variable number of path segments that will be concatenated to form the URL.
    
    Returns:
    str: The constructed URL with all provided segments concatenated directly.
    """
    # Join the segments together, ensuring no encoding is applied
    full_path = '/'.join(segment.strip('/') for segment in segments)
    
    # If there are any leading or trailing slashes from joining, remove them to avoid double slashes in the URL
    if full_path.startswith('/'):
        full_path = full_path[1:]
    if full_path.endswith('/'):
        full_path = full_path[:-1]
    
    # Construct and return the full URL, using urllib.parse to handle scheme (http/https) and netloc (domain) as needed
    url = 'http://example.com/' + full_path  # Example of adding a default domain; modify as necessary
    return url

# Example usage:
segments = ['this', 'is', 'a', 'test']
url = build_url(*segments)
print(url)  # Outputs: http://example.com/this/is/a/test