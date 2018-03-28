import hou
class SelectNode:
    def selectNode1(self):
        selectNodes = hou.selectedNodes()[0]
        serachName = hou.ui.readInput('Innput constraint name',buttons=['Ok','Cancle'])[1]
        if serachName =='0':
            for node in hou.selectedNodes():
                serachName = node.name()[0:2]
                spNmae = serachName.split()
                for node in selectNodes.parent().children():
                    for a in spNmae:
                        if  node.name()[0:len(a)].lower() == a.lower():
                            node.setSelected(1)
        
        else:     
            spNmae = serachName.split()
            for node in selectNodes.parent().children():
                for a in spNmae:
                    if  node.name()[0:len(a)].lower() == a.lower():
                        node.setSelected(1)
    def run(self):                
        if len(hou.selectedNodes()) == 0:
            hou.ui.displayMessage('Please select at least one node to specify the receiving module!')
        else:
            
            self.selectNode1()