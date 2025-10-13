from datetime import datetime

class Task:
    
    def __init__(self, title : str, deadline : datetime) -> None:
        if len(title) > 30 or len(title) < 1:            
            raise ValueError("task title must be less than 30 characters and not empty")
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        if deadline_date < datetime.now():
            raise ValueError("Deadline cannot be in the past.")
        
        self.title = title
        self.deadline = deadline
        self.status = "todo"
