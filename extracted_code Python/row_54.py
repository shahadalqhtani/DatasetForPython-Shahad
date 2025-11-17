import pickle
import os
from datetime import datetime, timedelta

# Define the path where the cache will be stored
CACHE_FILE = 'oauth_cache.pkl'

class OAuthTokenCache:
    def __init__(self, token=None, expires_at=None):
        self.token = token
        self.expires_at = expires_at

    @classmethod
    def load(cls):
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                data = pickle.load(f)
            return cls(**data)
        else:
            return cls()

    def save(self):
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump({
                'token': self.token,
                'expires_at': self.expires_at
            }, f)

    def is_valid(self):
        if not self.expires_at:
            return False
        return datetime.now() < self.expires_at

# Example usage
if __name__ == "__main__":
    # Simulate fetching a new token and its expiration time
    fetched_token = "your_new_oauth_token"
    expires_in_seconds = 3600  # For example, an hour from now
    expires_at = datetime.now() + timedelta(seconds=expires_in_seconds)

    # Load or create the cache
    token_cache = OAuthTokenCache.load()

    # Check if the current token is valid and not expired
    if not token_cache.is_valid():
        # Update the cache with new values
        token_cache.token = fetched_token
        token_cache.expires_at = expires_at
        token_cache.save()

    print(f"Token: {token_cache.token}")
    print(f"Expires at: {token_cache.expires_at}")