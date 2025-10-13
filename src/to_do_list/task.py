from datetime import datetime

class Task:
    
    def __init__(self, title : str, description : str, deadline : datetime) -> None:
        if len(title) > 30 or len(title) < 1:            
            raise ValueError("task's title must be less than 30 characters and not empty")
        
        if len(description) > 150 or len(description) < 1:            
            raise ValueError("task's description must be less than 150 characters and not empty")
        
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        if deadline_date < datetime.now():
            raise ValueError("Deadline cannot be in the past.")
        
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = "todo"

