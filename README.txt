This project was created after I completed COMP2521 and I wanted to
visually represent the graph data structure we had been covering
during that course. The algorithm for the visualisation is based of
force directed drawings where the nodes of graph interact with each 
other topush and pull into a stable postion, where the individual force 
interactionsdepend on distance, and connectivity. This was plotted in 
pyqtgraph using pyqt5.

To run this do the following

pip install virtualenv
virtualenv <name>
source <name>/bin/activate
pip install pyqtgraph
pip install pyqt5

python3 dfs.py