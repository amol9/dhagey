import sys

from .extract import extract_messages
from .names import Names
from .refs import Refs
from .graph import Graph

msgs = extract_messages()
print("found %d messages in the thread\n"%len(msgs))

names = Names()
refs = Refs()
refs.count(msgs, names)
refs.print_refs()

def render_graph():
    g = Graph(1, 10)

    for n in names.get_all_names():
        g.add_node(n, n)

    def add_edge(f, t, c):
        if c > 0: g.add_edge(f, t, c)

    refs.loop_und_refs(add_edge)
    g.render()

if len(sys.argv) > 1 and sys.argv[1] == 'g':
    render_graph()