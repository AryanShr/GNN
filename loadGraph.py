import dgl
# Load the graph
graphs, _ = dgl.load_graphs('graph.dgl')
g = graphs[0]
print(g)
