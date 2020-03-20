import csv
import networkx as nx


class Department:
    def __init__(self, ID, name, parent):
        self.name = name
        self.parent = parent
        self.id = ID


def add_edge(f_item, s_item, graph=None):
  graph.add_edge(f_item, s_item)
  graph.add_edge(s_item, f_item)


def search_dep(to_find, arr=None):
    for item in arr:
        if item.id == to_find:
            return item.name


departments = []

graph = nx.DiGraph()

with open('input/resourse_types.csv', encoding='utf-8', errors='replace',newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        dep = Department(row[0], row[2], row[1])
        departments.append(dep)
        if row[2] is not None:
            graph.add_node(row[2])

for dep in departments:
    parentname = search_dep(dep.parent, departments)
    if parentname is not None:
        graph.add_edge(parentname, dep.name)

p = nx.drawing.nx_pydot.to_pydot(graph)

p.write_pdf('output/resourse_types.pdf')
