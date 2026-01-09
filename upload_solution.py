import os
import json
import shutil
from datetime import datetime
from pathlib import Path

class LeetCodeUploader:
    def __init__(self, solutions_dir='leetcode-solutions', tracking_file='uploaded_solutions.json'):
        self.solutions_dir = Path(solutions_dir)
        self.tracking_file = Path(tracking_file)
        self.uploaded = self.load_tracking()
    
    def load_tracking(self):
        """Load the tracking file to see what's been uploaded"""
        if self.tracking_file.exists():
            with open(self.tracking_file, 'r') as f:
                return json.load(f)
        return {'uploaded': [], 'last_upload_date': None}
    
    def save_tracking(self):
        """Save the tracking file"""
        with open(self.tracking_file, 'w') as f:
            json.dump(self.uploaded, f, indent=2)
    
    def get_all_solutions(self):
        """Get all solution folders"""
        if not self.solutions_dir.exists():
            print(f"Error: Directory {self.solutions_dir} not found!")
            return []
        
        folders = [f for f in self.solutions_dir.iterdir() if f.is_dir()]
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
        print(f"Progress: {len(self.uploaded['uploaded'])}/100")
        
        return True

if __name__ == "__main__":
    uploader = LeetCodeUploader()
    uploader.upload_solution()