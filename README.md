# build2Vec

Graph Neural Networks based building representation in the vector space

## Installation

```
$ pip install build2vec
```

## Examples

```Python
import networkx as nx
from build2vec import Build2Vec
emb_dimensions = 10
# Create a graph using networkx -- you can generate the graph from dataframe of edges
graph = nx.from_pandas_edgelist(df_links_graph)

build2vec = Build2Vec(graph, dimensions=emb_dimensions, walk_length=50, num_walks=50, workers=1)

model = build2vec.fit(window=50, min_count=1, batch_words=10)
```
