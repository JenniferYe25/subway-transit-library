from Edge import Edge, WeightedEdge
from GraphBuilder import GraphBuilder
from PathFinders.AStar import a_star, generate_path_from_parents


graph = (GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],WeightedEdge,'undirected'))
start = '100'
dest = '11'

distances,parent = a_star(graph, start, dest)
print('optimal path => ', generate_path_from_parents(parent,start,dest))