import hou
class Pyro:
    def run(self):
    
        node = hou.node("/shop")
        node.createNode("pyro")
        