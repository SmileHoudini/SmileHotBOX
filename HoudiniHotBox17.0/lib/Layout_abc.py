import hou


class Layout_abc:
    def __init__(self):

        self.node_name = ['front', 'persp', 'side', 'top']

    # node_null = hou.node('/obj').createNode('null','scale')

    def allSubChildren(self, node):
        yield node
        for child_node in node.children():
            for n in self.allSubChildren(child_node):
                yield n

    def run(self):
        for node in hou.selectedNodes():
            keep_name = []
            for node in self.allSubChildren(node):
                if node.type().name() == 'cam':
                    path = node.path()
                    keep_name.append(path.split('/')[3])

        for node in hou.selectedNodes():
            for node_c in node.children():
                if node_c.name() not in keep_name:
                    node_c.destroy()
                elif node_c.name() in self.node_name:
                    node_c.destroy()

            node.createInputNode(0, 'null', 'scale')
            hou.node('/obj/scale').createOutputNode('geo', 'import_abc')

            node_scale = hou.node('/obj/scale')
            node_import_abc = hou.node('/obj/import_abc')

            pos = node.position()
            node_scale.setPosition((pos[0] + 1, pos[1] + 1))
            node_import_abc.setPosition((pos[0] + 2, pos[1]))

            parm_path = node.parm('fileName')

        # create node and set parm
        for node_c_import_abc in node_import_abc.children():
            node_c_import_abc.destroy()

        node_c_abc = node_import_abc.createNode('alembic')
        node_out_abc = node_c_abc.createOutputNode('null', 'Out_abc')

        node_c_abc.parm('fileName').set(parm_path)

        node_scene_abc = hou.node('/obj').createNode('geo', 'scene_abc')
        node_scene_abc.setPosition((pos[0] + 2, pos[1] - 1))

        for node_c_scene in node_scene_abc.children():
            node_c_scene.destroy()
        node_c_scene = node_scene_abc.createNode('object_merge', 'merge_abc')
        node_out_scene_abc = node_c_scene.createOutputNode('null', 'Out_scene_abc')

        out_abc_path = node_out_abc.path()

        node_c_scene.parm('objpath1').set(out_abc_path)
        node_c_scene.parm('xformtype').set(1)

        # set display
        node_scale.setDisplayFlag(False)
        node_import_abc.setDisplayFlag(False)


