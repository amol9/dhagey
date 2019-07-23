import json

from pdb import set_trace as pdbst


class Names:
    names_filename = "names.json"

    def __init__(self):
        self.names = {}
        self.lookup = {}

        self.load()
        self.make_lookup_dict()


    def load(self):
        with open(self.names_filename, "r") as f:
            self.names = json.load(f)
            

    def make_lookup_dict(self):
        for name in self.names.keys():
            for alias in self.names[name]:
                self.lookup[alias] = name


    def lookup_alias(self, alias):
        return self.lookup.get(alias, None)

    
    def get_all_aliases(self):
        all_aliases = []
        for name in self.names.keys():
            all_aliases += self.names[name]
        return all_aliases


    def get_all_names(self):
        return self.names.keys()
