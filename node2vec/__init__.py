"""
Reference implementation of node2vec. 

Author: Aditya Grover

For more details, refer to the paper:
node2vec: Scalable Feature Learning for Networks
Aditya Grover and Jure Leskovec 
Knowledge Discovery and Data Mining (KDD), 2016
"""

import argparse

from node2vec.core import learn_embeddings, read_graph, Graph, WalkSimulation


def parse_args():
    """
    Parses the node2vec arguments.
    """
    parser = argparse.ArgumentParser(description="Run node2vec.")

    parser.add_argument('--input', nargs='?', default='graph/karate.edgelist',
                        dest='input_path', help='Input graph path')

    parser.add_argument('--output', nargs='?', default='emb/karate.emb',
                        dest='output_path', help='Embeddings path')

    parser.add_argument('--dimensions', type=int, default=128,
                        help='Number of dimensions. Default is 128.')

    parser.add_argument('--walk-length', type=int, default=80,
                        help='Length of walk per source. Default is 80.')

    parser.add_argument('--num-walks', type=int, default=10,
                        help='Number of walks per source. Default is 10.')

    parser.add_argument('--window-size', type=int, default=10,
                        help='Context size for optimization. Default is 10.')

    parser.add_argument('--iter', default=1, type=int, dest='n_iter',
                        help='Number of epochs in SGD')

    parser.add_argument('--workers', type=int, default=8,
                        help='Number of parallel workers. Default is 8.')

    parser.add_argument('--p', type=float, default=1,
                        help='Return hyperparameter. Default is 1.')

    parser.add_argument('--q', type=float, default=1,
                        help='Inout hyperparameter. Default is 1.')

    parser.add_argument('--weighted', dest='weighted', action='store_true',
                        help='Boolean specifying (un)weighted. '
                             'Default is unweighted.')
    parser.add_argument('--no-randomisation', dest='no_shuffle',
                        action='store_true', help='Turn off graph sample '
                                                  'randomisation.')
    parser.add_argument('--unweighted', dest='unweighted',
                        action='store_false')
    parser.set_defaults(weighted=False)

    parser.add_argument('--directed', dest='is_directed', action='store_true',
                        help='Graph is (un)directed. Default is undirected.')
    parser.add_argument('--undirected', dest='undirected',
                        action='store_false')
    parser.set_defaults(directed=False)

    return parser.parse_args()


def main():
    """
    Pipeline for representational learning for all nodes in a graph.
    """
    args = parse_args().__dict__
    nx_graph = read_graph(**args)
    G = Graph(nx_graph, **args)
    G.preprocess_transition_probs()
    walks = WalkSimulation(G, **args)
    learn_embeddings(walks, **args)


if __name__ == "__main__":
    main()
