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

## Todos:

1. Add automatic grid generation method.
2. Add automatic graph construction method.
3. Add visualization moddule.
4. Add ML clustering, classification, and prediction moduels.
5. Define other builing-related random walks methods.

## Citation:

```bib
@inproceedings{abdelrahmanbuild2vec,
    title = {{Build2Vec: Building Representation in Vector Space}},
    year = {2020},
    booktitle = {SimAUD 2020},
    author = {Abdelrahman, Mahmoud M and Chong, Adrian and Miller, Clayton},
    number = {May},
    pages = {101--104},
    publisher = {Society for Modeling {\&} Simulation International (SCS)},
    url = {http://simaud.org/2020/proceedings/102.pdf},
    address = {Online},
    arxivId = {2007.00740},
    keywords = {Feature learning, Graph embeddings, Representation learning, STAR, node2vec}
}
```
