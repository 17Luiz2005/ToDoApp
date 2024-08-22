# TODO: Add code here
class Todo:
    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]) -> None:
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list = []