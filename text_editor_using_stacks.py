from stack import Stack

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def type(self, value):
        self.undo_stack.push(value)
        self.text += value
        self.redo_stack = Stack()

    def undo(self):
        if not self.undo_stack.is_empty():
            last_action = self.undo_stack.pop()
            self.redo_stack.push(last_action)
            # Remove the last action from the text
            self.text = self.text[:-len(last_action)]

    def redo(self):
        if not self.redo_stack.is_empty():
            last_undone_action = self.redo_stack.pop()
            self.undo_stack.push(last_undone_action)
            # Reapply the last undone action to the text
            self.text += last_undone_action

    def __str__(self):
        return self.text

# Example usage
editor = TextEditor()
editor.type('Hello')
editor.type(' World')

print("Text:", editor)  # Output: "Hello World"

editor.undo()
print("After undo:", editor)  # Output: "Hello"

editor.redo()
print("After redo:", editor)  # Output: "Hello World"
editor.type(' World')
editor.undo()
editor.undo()
print("After two undos:", editor)  # Output: ""

editor.redo()
print("After redo:", editor)  # Output: "Hello"
