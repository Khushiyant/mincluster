"""
This module implements the main functionality of mincluster.

Author: Khushiyant
(Cite) Paper Basis: https://doi.org/10.1016/0304-3975(85)90224-5
"""

__author__ = "Khushiyant"
__email__ = "khushiyant2002@gmail.com"

import numpy as np
from typing import List, Tuple


class ClusterMinimization:

    class Cluster:
        """
        A class representing a cluster of elements.

        Attributes:
        -----------
        k : int
            The number of clusters.
        elements : np.array | List[int]
            The elements to be clustered.

        Methods:
        --------
        __init__(self, k:int ,elements: np.array | List[int]) -> None:
            Initializes the Cluster object with k clusters and elements to be clustered.
        """

        def __init__(self, k: int, elements: np.array | List[int]) -> None:
            """
            Initializes the Cluster object with k clusters and elements to be clustered.

            Parameters:
            -----------
            k : int
                The number of clusters.
            elements : np.array | List[int]
                The elements to be clustered.
            """
            self.clusters = [set(elements) for _ in range(k)]

            # Select the head for the first cluster (B1)
            head = np.random.choice(elements)
            self.clusters[0].remove(head)
            self.cluster_heads = [head]

        def _distance(self, node, cluster_head):
            '''
            Calculate the distance between a node and the head of its cluster.

            Parameters:
            node (int): The node to calculate the distance for.
            cluster_head (int): The head of the cluster.

            Returns:
            float: The distance between the node and the cluster head.
            '''
            return np.abs(node - cluster_head)

        def expand_clusters(self, clusters, cluster_heads) -> Tuple[List[set], List[int]]:
            """
            Expands the given clusters by creating new clusters and adding them to the list of clusters.

            Args:
            - clusters: A list of sets, where each set contains the nodes in a cluster.
            - cluster_heads: A list of nodes, where each node is the head of the corresponding cluster.

            Returns:
            - A tuple containing the updated list of clusters and the updated list of cluster heads.
            """
            k = len(clusters)

            for j in range(1, k):
                new_cluster = set()
                head_distances = []

                # Find the node with maximal distance to its cluster head
                for i in range(j):
                    for node in clusters[i]:
                        dist = self._distance(node, cluster_heads[i])
                        if all(dist <= self._distance(node, cluster_heads[c]) for c in range(j)):
                            new_cluster.add(node)
                            head_distances.append((node, dist))

                # Select the node with the maximum distance as the head of the new cluster
                new_head, _ = max(head_distances, key=lambda x: x[1])
                new_cluster.remove(new_head)

                # Update the cluster and head information
                clusters.append(new_cluster)
                cluster_heads.append(new_head)

            return clusters, cluster_heads
