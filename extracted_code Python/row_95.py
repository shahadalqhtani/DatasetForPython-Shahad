sh
   pip install requests
import os
import requests
from urllib.parse import urlparse

def download_image(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {url} to {save_path}")
        else:
            print(f"Failed to download image from {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from {url}: {e}")

def main():
    urls = []
    while True:
        url = input("Enter the URL of the image (or type 'done' to finish): ")
        if url.lower() == 'done':
            break
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            print("Invalid URL. Please enter a valid URL.")
            continue
        urls.append((url, os.path.basename(parsed_url.path)))

    save_directory = input("Enter the directory to save the images (default is 'images'): ") or 'images'
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for url, filename in urls:
        save_path = os.path.join(save_directory, filename)
        download_image(url, save_path)

if __name__ == "__main__":
    main()
Enter the URL of the image (or type 'done' to finish): https://example.com/image1.jpg
Enter the URL of the image (or type 'done' to finish): https://example.com/image2.png
Enter the directory to save the images (default is 'images'):