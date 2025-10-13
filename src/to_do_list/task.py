from datetime import datetime
from typing import Literal
class Task:
    
    def __init__(self, id : int, title : str, description : str, deadline : datetime) -> None:
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
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline_date
        self.status = "todo"

    def change_title(self ,new_title):
        if len(new_title) > 30 or len(new_title) < 1:            
            raise ValueError("task's title must be less than 30 characters and not empty")
        self.title = new_title
    
    def change_description(self ,new_description):
        if len(new_description) > 150 or len(new_description) < 1:            
            raise ValueError("task's description must be less than 150 characters and not empty") 
        self.description = new_description
    
    def change_status(self ,new_status : Literal["todo", "doing" ,"done"]):
        self.status = new_status 
    
    def change_deadline(self ,new_deadline : datetime):
        try:
            deadline_date = datetime.strptime(new_deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        if deadline_date < datetime.now():
            raise ValueError("Deadline cannot be in the past.")
        self.deadline = deadline_date
        
    def task_status(self):
        return self.status
    
    def __repr__(self):
        return f"Task(id='{self.id}', title='{self.title}')"
       
        
if __name__ == "__main__":
    task1 = Task("home work" ,"the math home woek to do" , "2026-12-23")
    print(task1.title)
    task1.change_description("jfjbibfisfbvjdnvfjbf ")
    print(task1.deadline)
    print(task1.task_status())