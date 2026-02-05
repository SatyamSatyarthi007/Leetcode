import os
import json
import shutil
from datetime import datetime
from pathlib import Path

class LeetCodeUploader:
    def __init__(self, solutions_dir='.', tracking_file='uploaded_solutions.json'):
        # default to current working directory so script works from repo root
        self.solutions_dir = Path(solutions_dir)
        self.tracking_file = Path(tracking_file)
        self.uploaded = self.load_tracking()
    
    def load_tracking(self):
        """Load the tracking file to see what's been uploaded"""
        if self.tracking_file.exists():
            try:
                with open(self.tracking_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if not content:
                        print(f"Warning: tracking file {self.tracking_file} is empty; resetting.")
                        return {'uploaded': [], 'last_upload_date': None}
                    data = json.loads(content)
                # validate structure
                if not isinstance(data, dict) or 'uploaded' not in data:
                    raise ValueError('tracking file has invalid structure')
                return data
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Warning: tracking file {self.tracking_file} is corrupted or invalid ({e}); resetting.")
                # Try to restore from backup if it exists
                backup_file = Path(str(self.tracking_file) + '.bak')
                if backup_file.exists():
                    try:
                        with open(backup_file, 'r', encoding='utf-8') as f:
                            backup_data = json.load(f)
                        print(f"Restored from backup file: {backup_file}")
                        return backup_data
                    except:
                        pass
                return {'uploaded': [], 'last_upload_date': None}

        return {'uploaded': [], 'last_upload_date': None}
    
    def save_tracking(self):
        """Save the tracking file"""
        # Create backup before saving
        if self.tracking_file.exists():
            backup_file = Path(str(self.tracking_file) + '.bak')
            shutil.copy2(self.tracking_file, backup_file)
        
        # Write to temporary file first, then rename (atomic operation)
        temp_file = Path(str(self.tracking_file) + '.tmp')
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(self.uploaded, f, indent=2)
            # Atomic rename
            temp_file.replace(self.tracking_file)
        except Exception as e:
            if temp_file.exists():
                temp_file.unlink()
            raise e
    
    def get_all_solutions(self):
        """Get all solution folders"""
        if not self.solutions_dir.exists():
            print(f"Error: Directory {self.solutions_dir} not found!")
            return []
        
        # ignore hidden dot-folders (e.g. .git) and any non-directory entries
        folders = [f for f in self.solutions_dir.iterdir() if f.is_dir() and not f.name.startswith('.')]
        folders.sort()  # Sort to maintain consistent order
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
        print(f"Progress: {len(self.uploaded['uploaded'])}/{total}")
        
        return True

if __name__ == "__main__":
    uploader = LeetCodeUploader()
    uploader.upload_solution()
