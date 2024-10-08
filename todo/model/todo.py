# TODO: Add code here

class Todo:

    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]) -> None:
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list = []

    def mark_completes(self):
        self.completed: bool = True
    
    def add_tag (self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def __str__(self) -> str:
        return f"{self.code_id - self.title}"
    

class TodoBook:
    
    def __init__(self) -> None:
        self.todos: dict[int, Todo] = {}
    
    def add_todo(self, title: str, description: str) -> int:
        id = len(self.todos) + 1
        new_todo = Todo(id, title, description)
        self.todos[id] = new_todo
        return id
    
    def pending_todos(self) -> list[Todo]:
        return [Todo for Todo in self.todos.values() if not Todo.completed]
    
    def completed_todos(self) -> list[Todo]:
        return [Todo for Todo in self.todos.values() if Todo.completed]