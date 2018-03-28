import hou
class Basicsmoke:
    def run(self):
    
        node = hou.node("/shop")
        node.createNode("vopmaterial")
        