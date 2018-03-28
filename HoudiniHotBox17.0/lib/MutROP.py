import hou

class MutROP:
    def run(self):
        node = hou.selectedNodes()
        size = len(node)
        if size ==1:
        
            
            import MutRopUI
            selectM = MutRopUI.MutROP()
            checkOpen = selectM.run()
            if checkOpen ==1:
            
                import MutRopUI2
                reload (MutRopUI2)
        else:
            
           
            
            import MMutRopUI
            selectM = MMutRopUI.MutROP()
            checkOpen = selectM.run()
            
            