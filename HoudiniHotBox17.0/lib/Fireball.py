import hou
class Fireball:
    def run(self):
    
        node = hou.node("/shop")
        node.createNode("pyro::3.0")
        