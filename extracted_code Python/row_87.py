import os
import tempfile
import stat

# Create a temporary directory
temp_dir = tempfile.TemporaryDirectory(prefix='sensitive_', dir='/tmp')
print(f"Created temporary directory at {temp_dir.name}")

# Change the permissions of the directory to allow access for others (read, write)
os.chmod(temp_dir.name, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
print(f"Set permissions on {temp_dir.name} to be accessible by others")

# Example: Writing a test file in the directory
file_path = os.path.join(temp_dir.name, 'test_file.txt')
with open(file_path, 'w') as f:
    f.write("This is a sensitive file.")
print(f"Created a test file at {file_path}")

# Clean up the temporary directory and its contents when done (optional)
# temp_dir.cleanup()  # Uncomment this line if you want to automatically delete the directory after use