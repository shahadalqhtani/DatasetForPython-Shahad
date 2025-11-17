sh
pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

def get_final_url_content(url):
    """
    Fetches the final URL after following all redirects and returns the content.
    
    Args:
        url (str): The initial URL to fetch.
    
    Returns:
        tuple: A tuple containing the final URL and its content.
    """
    try:
        # Perform a request to the URL
        response = requests.get(url)
        
        # Follow redirects
        while True:
            if 300 <= response.status_code < 400:
                redirect_url = response.headers['Location']
                response = requests.get(redirect_url)
            else:
                break
        
        # If the content type is HTML, parse it to extract title or other metadata
        if 'text/html' in response.headers.get('Content-Type', ''):
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else "No Title"
            return redirect_url, response.content, title
        else:
            return redirect_url, response.content, None
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return url, "", None

# Example usage
if __name__ == "__main__":
    initial_url = input("Enter the URL to preview: ")
    final_url, content, title = get_final_url_content(initial_url)
    
    print(f"Final URL: {final_url}")
    # For simplicity, we're not displaying the full HTML content. You can adjust this as needed.
    if title:
        print(f"Title from HTML: {title}")