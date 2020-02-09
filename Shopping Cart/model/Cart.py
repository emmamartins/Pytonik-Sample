from pytonik.Model import Model
from pytonik.Session import Session
from pytonik import Version
import ast
class Cart(Model, Session):

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None


    def find(self, item, key="", value=""):

        if self.get(item) is not "":
            try:
                d = self.get(item)

                if key is "":

                    k_dict, dict_kv= [],  {}
                    for nv in d:

                        if Version.PYVERSION_MA >= 3:
                            fn = nv.items()
                        else:
                            fn = nv.iteritems()


                        for k, v in fn:
                            dict_kv.update({k:v})
                        k_dict.append(dict_kv)

                    return ast.literal_eval(k_dict)

                elif key != "" and value != "":

                    bl = bool
                    for nv in d:

                        if Version.PYVERSION_MA >= 3:
                            fn = nv.items()
                        else:
                            fn = nv.iteritems()

                        for k, v in fn:
                            if key == k:
                                if value == v:
                                    bl=  True
                                else:
                                    bl =  False
                    return bl
                else:
                    vals = []
                    for nv in d:

                        if Version.PYVERSION_MA >= 3:
                            fn = nv.items()
                        else:
                            fn = nv.iteritems()


                        for k, v in fn:
                            if key == k:
                                vals.append(v)
                    return vals
            except Exception as err:
                return ""
        else:
            return ""

    def delete(self, item, key="", value=""):
        if self.get(item) is not "":
            list_item = self.get(item)
            if key != "" and value != "":
                for i in range(len(list_item)):

                    if list_item[i][key] == value:
                        del list_item[i]
                        break
                self.set(item, list_item)
                return True
            else:
                if Version.PYVERSION_MA <= 2 and Version.PYVERSION_MI <= 7:
                    list_item[:]
                elif Version.PYVERSION_MA == 3 and Version.PYVERSION_MI <= 3:
                    list_item[:]
                elif Version.PYVERSION_MA == 3 and Version.PYVERSION_MI >= 4:
                    list_item.clear()
                self.set(item, list_item)
                return True
        else:
            return ""

    def update(self, item, key= "", value="", newitem=""):

        if self.get(item) is not "":
            itemv = self.get(item)

            upnewitem = []
            for olditem in itemv:

                listnewitem = {}
                if Version.PYVERSION_MA >= 3:
                    fn = olditem.items()
                else:
                    fn = olditem.iteritems()

                for k, v in fn:

                    if k == key:
                        if olditem.get(k, '') == value:
                            olditem.update(newitem)
                    listnewitem.update(olditem)

                upnewitem.append(listnewitem)

            self.set(item, upnewitem)
            return True

        else:
            return ""
