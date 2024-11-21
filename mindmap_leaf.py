class MindMapLeaf:
    """constructs leaves"""

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def __str__(self):
        return f'{self.get_shape_representation().format(self.name)}'

    def display(self,indent=0):
        if indent == 0:
            print("mindmap\nroot",end='')
        print(" " * indent + str(self))

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