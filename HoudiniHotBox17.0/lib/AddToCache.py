import hou

class AddToCache:
    def __init__(self):
        # have else node to cache can add in cache_node
        self.cache_node = ['filecache', 'catche_tool_1.0.1', 'ifd']
        self.node_sel = hou.selectedNodes()

    def allSubInput(self, node):
        yield node
        for node_input in node.inputs():
            for n in self.allSubInput(node_input):
                yield n

    def _cache_list_(self, node):
        cache_list = []
        for node in self.node_sel:
            for i in self.allSubInput(node):
                if i.type().name() in self.cache_node:
                    cache_list.append(i)
        return cache_list

    def main(self):
        node_outCache = hou.node('/out/out_cache_link')

        if node_outCache < 1:
            node_outCache = hou.node('/out').createNode('out_cache', 'out_cache_link')

        cache_num = node_outCache.parm('cache_node_number').eval()

        list_parm = []  # get out cache parm path
        for i in range(cache_num):
            n = i + 1
            cacheNode_parm = node_outCache.parm('cache_node_' + str(n)).eval()
            list_parm.append(cacheNode_parm)

        cache_list_a = self._cache_list_(self.node_sel)
        cache_list_rev = list(reversed(cache_list_a))
        cache_list = sorted(set(cache_list_rev), key=cache_list_rev.index)  # remove the same

        list_path_all = []  # get all selected cache path
        for i in range(len(cache_list)):
            node_to_cache = cache_list[i]
            list_path_all.append(node_to_cache.path())

        list_path = []  # remove the same cache path
        for i in range(len(list_path_all)):
            if list_path_all[i] not in list_parm:
                list_path.append(list_path_all[i])

        cache_num = node_outCache.parm('cache_node_number').eval()
        node_outCache.parm('cache_node_number').set(cache_num + len(list_path))

        for i in range(len(list_path)):
            n = i + cache_num + 1
            node_to_cache = list_path[i]
            node_outCache.parm('cache_node_' + str(n)).set(node_to_cache)

        # print hou.ui.displayMessage('sucsesful')
        if len(list_path) == 0:
            hou.ui.displayMessage('Already added or no cache')
        else:
            info = '"\n"'.join(list_path)
            print info
            hou.ui.displayMessage('Successfully added')

    def run(self):
        self.main()