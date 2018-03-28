import hou
class mantrasurface:
    def run(self):
    
        node = hou.node("/shop")
        node.createNode("mantrasurface")
        