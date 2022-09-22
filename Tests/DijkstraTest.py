
graph=(GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected"))

d = Dijkstra(graph, 1, 7)
d.start()
d.print_path()