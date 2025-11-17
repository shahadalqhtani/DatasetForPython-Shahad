import os
import sys

def create_upload_directories(base_dir):
    # List of directories to be created
    upload_dirs = ['uploads', 'uploads/images', 'uploads/documents']
    
    for dir_name in upload_dirs:
        full_path = os.path.join(base_dir, dir_name)
        
        if not os.path.exists(full_path):
            try:
                os.makedirs(full_path, mode=0o777)
                print(f"Created directory: {full_path} with permissions 0o777")
            except Exception as e:
                print(f"Failed to create directory {full_path}: {e}")
        else:
            print(f"Directory already exists: {full_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <base_directory>")
        sys.exit(1)
    
    base_dir = sys.argv[1]
    
    create_upload_directories(base_dir)
sh
python script.py /path/to/base/directory