# importing from pyvis and streamlit for frontend lineage graph visualizations
from pyvis.network import Network
import streamlit.components.v1 as components

def render_lineage_graph():
    net = Network(height="500px", directed=True)
    nodes = ["Policy_Master", "Claims_DB", "Reserve_Model"]
    edges = [("Policy_Master", "Claims_DB"), ("Claims_DB", "Reserve_Model")]

    for node in nodes:
        net.add_node(node, label=node)
    for edge in edges:
        net.add_edge(edge[0], edge[1])

    net.save_graph("data/lineage.html")
    components.html(open("data/lineage.html", "r").read(), height=550)
