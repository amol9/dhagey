

class Refs:

    def __init__(self):
        self.refs = {}


    def count(self, messages, names):
        for n in names.get_all_names():
            self.refs[n] = {}

        for msg in messages:
            frm = names.lookup_alias(msg.sender.lower())
            #print(frm)
            if frm is None:
                print("error: %s not known"%frm)

            for t in self.findall(names, msg.body.lower()):
                d = self.refs[frm]
                if d.get(t, None) is None:
                    d[t] = 1
                else:
                    d[t] += 1

                if frm == "rupesh" and t == "rupesh":
                    print(msg.body)

        
    def findall(self, names, body):
        to_list = []
        for alias in names.get_all_aliases():
            if body.find(alias) > -1:
                to_list.append(names.lookup_alias(alias))
        
        return to_list


    def print_refs(self):
        for frm in self.refs.keys():
            for to, count in self.refs[frm].items():
                if count > 0:
                    print("%s => %s : %d"%(frm, to, count))
    

    def get_undirected_edges(self):
        pass


    def loop_refs(self, cb):
        for frm in self.refs.keys():
            for to, count in self.refs[frm].items():
                cb(frm, to, count)


    def loop_und_refs(self, cb):
        paired = []

        for frm in self.refs.keys():
            for to, count in self.refs[frm].items():
                if not to in paired:
                    if to != frm and self.refs[to].get(frm, None) is not None:
                        cb(frm, to, count + self.refs[to][frm])
                    else:
                        cb(frm, to, count)
            paired.append(frm)

        
    def print_und_refs(self):
            def prnt(f, t, c):
                if c > 0: print("%s => %s : %d"%(f, t, c))

            self.loop_und_refs(prnt)