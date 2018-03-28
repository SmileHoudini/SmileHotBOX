import hou
import os
class ImportCamImage:
    def get_path_w(self):
        path_x = hou.hipFile.path()
        list_path = path_x.split('/')
        list_path[0] = 'w:'

        list_path_w = []
        for i in range(4):
            list_path_w.append(list_path[i])

        try:
            path_w = '/'.join(list_path_w)
            list_var = os.listdir(path_w)
            return path_w

        except:
            try:
                repl = list_path_w[2]
                list_path_w[2] = repl.replace('-', '_')
                path_w = '/'.join(list_path_w)
                list_var = os.listdir(path_w)
                return path_w
            except:
                repl = list_path_w[3]
                list_path_w[3] = repl.replace('-', '_')
                path_w = '/'.join(list_path_w)
                list_var = os.listdir(path_w)
                return path_w

    def run(self):
        try:
            list_var = os.listdir(self.get_path_w() + "/plate")
            path_w_jpg = self.get_path_w() + '/' + "plate/" + list_var[-1] + '/jpg'
            # print path_w_jpg
        except:
            list_var = os.listdir(self.get_path_w())
            path_w_jpg = self.get_path_w() + '/' + list_var[-1] + '/jpg'
            # print path_w_jpg

        list_all = os.listdir(path_w_jpg)

        suffix_jpg = []
        for jpg in list_all:
            suffix = jpg.split('.')
            if suffix[-1] == 'jpg':
                suffix_jpg.append(jpg)

        list_jpg = suffix_jpg[0].split('.')
        list_jpg[-2] = '$F4'
        jpg_name = '.'.join(list_jpg)
        # get jpg path
        path_w_jpg = path_w_jpg + '/' + jpg_name

        # set parm
        node_sel = hou.selectedNodes()
        for node in node_sel:
            node.parm('vm_background').set(path_w_jpg)

        # set playbackRange
        list_s_n = suffix_jpg[0].split('.')
        list_e_n = suffix_jpg[-1].split('.')
        s_n = int(list_s_n[-2])
        e_n = int(list_e_n[-2])
        hou.playbar.setPlaybackRange(s_n, e_n)
        hou.setFrame(s_n)