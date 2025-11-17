bash
   pip install requests
import requests
from urllib.parse import urlparse, parse_qs

def get_redirected_url(original_url):
    try:
        # Perform a GET request to the original URL
        response = requests.get(original_url)
        
        # Check if there is a redirect
        if 300 <= response.status_code < 400:
            location = response.headers['Location']
            return location
        else:
            raise ValueError("No redirection found or invalid status code")
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def main():
    # Example original URL provided by a remote API
    original_url = "http://example.com/api/redirect?param=value"
    
    # Get the redirected URL
    redirected_url = get_redirected_url(original_url)
    
    if redirected_url:
        print(f"Redirected URL: {redirected_url}")
        
        # If you need to handle specific query parameters or parse them, you can do so here
        parsed_url = urlparse(redirected_url)
        query_params = parse_qs(parsed_url.query)
        print("Query Parameters:", query_params)
    else:
        print("Failed to get the redirected URL.")

if __name__ == "__main__":
    main()