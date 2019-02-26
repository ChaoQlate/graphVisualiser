This project was created after COMP2521 and I wanted to visualise the graph data structure we had been covering during that course. The algorithm for the visualisation is based off force directed drawings and was iterated to form a realtively stable position. Nodes of graph interact with each other by pushing and pulling where these individual force interactions depend on distance and connectivity. This was plotted in pyqtgraph using PyQt5.

To run this do the following

pip install virtualenv
virtualenv <name>
source <name>/bin/activate
pip install pyqtgraph
pip install pyqt5

python3 dfs.py
