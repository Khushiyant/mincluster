# mincluster

mincluster is a package that allows to minimize the maximum intercluster distance

## Overview
<center>
    <img src="https://github.com/Khushiyant/mincluster/assets/69671407/4a47c95a-5274-4998-956f-3cdbd3e34b4c" width=40% align="center">
</center>

The problem of clustering a set of points so as to minimize the maximum intercluster distance is studied. An O(kn) approximation algorithm, where n is the number of points and k is the number of clusters, that guarantees solutions with an objective function value within two times the optimal solution value is presented. This approximation algorithm succeeds as long as the set of points satisfies the triangular inequality. We also show that our approximation algorithm is best possible, with respect to the approximation bound, if P ≠ NP.

## Installation

```python
pip install mincluster
```

## Usage

```python
from mincluster.cluster import ClusterMinimization

k = 3
data = [231, 22, 73, 54, 60, 29, 10, 192, 115]
c = ClusterMinimization(k, data)
clusters, cluster_heads = c.expand_clusters(c.clusters, c.cluster_heads)

try:
    for i in range(k):
        print(f'Cluster {i + 1}: Head = {cluster_heads[i]}, Elements = {clusters[i]}')
except IndexError as e:
        print(e)
```

### Output
```output
Cluster 1: Head = 60, Elements = {192, 231, 73, 10, 115, 54, 22, 29}
Cluster 2: Head = 231, Elements = {192, 231, 73, 10, 115, 54, 22, 60, 29}
Cluster 3: Head = 115, Elements = {192, 231, 73, 10, 115, 54, 22, 60, 29}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## References

Gonzalez, Teofilo F. “Clustering to Minimize the Maximum Intercluster Distance.” Theoretical Computer Science, vol. 38, Elsevier BV, Jan. 1985, pp. 293–306, https://doi.org/10.1016/0304-3975(85)90224-5. Accessed 26 Oct. 2023.
