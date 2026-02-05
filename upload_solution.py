import os
import json
from datetime import datetime
from pathlib import Path

class LeetCodeUploader:
    def __init__(self, solutions_dir='.', tracking_file='uploaded_solutions.json'):
        self.solutions_dir = Path(solutions_dir)
        self.tracking_file = Path(tracking_file)
        self.uploaded = self.load_tracking()
    
    def load_tracking(self):
        """Load the tracking file to see what's been uploaded"""
        # Initialize default structure
        default_data = {'uploaded': [], 'last_upload_date': None}
        
        # If file doesn't exist, return default
        if not self.tracking_file.exists():
            return default_data
        
        # Try to read and parse the file
        try:
            with open(self.tracking_file, 'r', encoding='utf-8') as f:
                file_content = f.read()
                
            # Check if file is empty
            if not file_content or file_content.strip() == '':
                print("Warning: Tracking file is empty. Initializing with default data.")
                return default_data
            
            # Parse JSON
            data = json.loads(file_content)
            
            # Validate structure
            if not isinstance(data, dict) or 'uploaded' not in data:
                print("Warning: Invalid tracking file structure. Resetting.")
                return default_data
            
            return data
            
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse JSON ({e}). Resetting tracking file.")
            return default_data
        except Exception as e:
            print(f"Warning: Error reading tracking file ({e}). Resetting.")
            return default_data
    
    def save_tracking(self):
        """Save the tracking file"""
        try:
            with open(self.tracking_file, 'w', encoding='utf-8') as f:
                json.dump(self.uploaded, f, indent=2, ensure_ascii=False)
                f.write('\n')  # Add newline at end
        except Exception as e:
            print(f"Error saving tracking file: {e}")
            raise
    
    def get_all_solutions(self):
        """Get all solution folders"""
        if not self.solutions_dir.exists():
            print(f"Error: Directory {self.solutions_dir} not found!")
            return []
        
        # Get all directories that don't start with '.'
        folders = [
            f for f in self.solutions_dir.iterdir() 
            if f.is_dir() and not f.name.startswith('.')
        ]
        folders.sort()
        return folders
    
    def get_next_solution(self):
        """Get the next solution to upload"""
        all_solutions = self.get_all_solutions()
        uploaded_set = set(self.uploaded['uploaded'])
        
        for solution in all_solutions:
            if solution.name not in uploaded_set:
                return solution
        
        return None
    
    def upload_solution(self):
        """Upload the next solution"""
        next_solution = self.get_next_solution()
        
        if not next_solution:
            print("All solutions have been uploaded! 🎉")
            return False
        
        print(f"Uploading solution: {next_solution.name}")
        
        # Add to uploaded list
        self.uploaded['uploaded'].append(next_solution.name)
        self.uploaded['last_upload_date'] = datetime.now().isoformat()
        
        # Save tracking
        self.save_tracking()
        
        print(f"✅ Successfully uploaded: {next_solution.name}")
        total = len(self.get_all_solutions())
        uploaded_count = len(self.uploaded['uploaded'])
        print(f"Progress: {uploaded_count}/{total}")
        
        return True

if __name__ == "__main__":
    uploader = LeetCodeUploader()
    uploader.upload_solution()
