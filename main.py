import csv
import networkx as nx
import os
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout


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


os.environ["PATH"] += os.pathsep + 'B:/Program Files (x86)/Graphviz2.38/bin/'

departments = []

graph = nx.DiGraph()

with open('departments.csv', encoding='utf-8', errors='replace',newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        dep = Department(row[0], row[2], row[1])
        departments.append(dep)
        graph.add_node(row[2])
        print(row[2])

for dep in departments:
    graph.add_edge(search_dep(dep.parent, departments), dep.name)

# write_dot(graph, 'test.dot')

plt.title('draw_networkx')
pos = graphviz_layout(graph, prog='dot')
nx.draw(graph, with_labels=True, arrows=True)
plt.savefig('nx_test.png')

# p.write_pdf('example.pdf')