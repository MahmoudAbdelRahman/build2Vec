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
@inproceedings{10.5555/3465085.3465155,
author = {Abdelrahman, Mahmoud M. and Chong, Adrian and Miller, Clayton},
title = {Build2Vec: Building Representation in Vector Space},
year = {2020},
abstract = {In this paper, we represent a methodology of a graph embeddings algorithm that is
used to transform labeled property graphs obtained from a Building Information Model
(BIM). Industrial Foundation Classes (IFC) is a standard schema for BIM, which is
utilized to convert the building data into a graph representation. We used node2Vec
with biased random walks to extract semantic similarities between different building
components and represent them in a multi-dimensional vector space. A case study implementation
is conducted on a net-zero-energy building located at the National University of Singapore
(SDE4). This approach shows promising machine learning applications in capturing the
semantic relations and similarities of different building objects, more specifically,
spatial and spatio-temporal data.},
booktitle = {Proceedings of the 11th Annual Symposium on Simulation for Architecture and Urban Design},
articleno = {70},
numpages = {4},
keywords = {graph embeddings, STAR, node2vec, feature learning, representation learning},
location = {Virtual Event, Austria},
series = {SimAUD '20},
}
```
