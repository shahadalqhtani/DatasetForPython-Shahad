import tempfile
import os

# Create a temporary file using mkstemp
fd, temp_filename = tempfile.mkstemp(suffix='_example', prefix='prefix_', dir='/tmp')

try:
    # Open the temporary file for writing (or reading and writing)
    with open(temp_filename, 'w+') as f:
        # Write some data to the file
        f.write('Hello, this is a temporary file!')
        
        # Optionally, read back the written data
        f.seek(0)  # Move cursor to the beginning of the file
        content = f.read()
        print("File content:", content)
    
    # Optionally, you can delete the file after usage if not needed anymore
    os.remove(temp_filename)
except Exception as e:
    print("An error occurred:", e)