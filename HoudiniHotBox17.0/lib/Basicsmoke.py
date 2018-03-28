import hou
class Billowysmoke:
    def run(self):
    
        node = hou.node("/shop")
        node.createNode("vopmaterial")
        