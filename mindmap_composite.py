import os

class MindMapComposite:
    """gathers the leaves"""

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def __str__(self):
        return f'{self.get_shape_representation().format(self.name)}'

    def get_mind_map(self,indent=0):
        result = ''
        if indent == 0:
            result += 'mindmap' + os.linesep + 'root'
        result += ' ' * indent + str(self) + os.linesep
        for child in self.children:
            result += child.get_mind_map(indent + 2)
        return result

    def display(self, indent=0):
        if indent == 0:
            print("mindmap\nroot",end='')
        print(" " * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    def get_shape_representation(self):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}(("
        }
        return shapes.get(self.shape,"{}")