load_dotenv()
class Project:
    
    def __init__(self, name : str, description : str) -> None:
        self.name = name
        self.description = description

    def change_name(self, new_name : str):
        self.name = new_name
    
    def change_description(self, new_description : str):
        self.description = new_description
    
       
    
    