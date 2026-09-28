"""
network_view.py
River network / confluence diagrams using networkx + plotly (no graphviz
dependency needed, so it runs anywhere streamlit runs).
"""
import networkx as nx
import plotly.graph_objects as go


def build_river_network_figure(rivers_dict):
    """
    Builds a directed graph of rivers -> confluence points -> downstream
    rivers, using the RIVERS dict structure from data_loader.
    """
    G = nx.DiGraph()
    for river, info in rivers_dict.items():
        G.add_node(river, kind="river")
        for conf in info.get("confluences", []):
            conf_node = f"Confluence: {conf}"
            G.add_node(conf_node, kind="confluence")
            G.add_edge(river, conf_node)

    pos = nx.spring_layout(G, seed=42, k=0.9)

    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color="#888"),
                             hoverinfo="none", mode="lines")

    node_x, node_y, node_text, node_color = [], [], [], []
    for n, attrs in G.nodes(data=True):
        x, y = pos[n]
        node_x.append(x); node_y.append(y); node_text.append(n)
        node_color.append("#1f77b4" if attrs.get("kind") == "river" else "#ff7f0e")

    node_trace = go.Scatter(
        x=node_x, y=node_y, mode="markers+text", text=node_text,
        textposition="top center", hoverinfo="text",
        marker=dict(size=16, color=node_color, line=dict(width=1, color="white")),
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        showlegend=False, height=600, margin=dict(l=10, r=10, t=30, b=10),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        title="River Network: Rivers and Confluence Points",
    )
    return fig


def build_canal_link_figure(link_canals):
    """Simple bipartite-style diagram: link canal -> connects (source -> destination river)."""
    G = nx.DiGraph()
    for lc in link_canals:
        name = lc["name"]
        connects = lc["connects"]
        G.add_node(name, kind="canal")
        parts = [p.strip() for p in connects.split("->")]
        if len(parts) == 2:
            G.add_node(parts[0], kind="river")
            G.add_node(parts[1], kind="river")
            G.add_edge(parts[0], name)
            G.add_edge(name, parts[1])

    pos = nx.spring_layout(G, seed=7, k=1.0)
    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]; x1, y1 = pos[v]
        edge_x += [x0, x1, None]; edge_y += [y0, y1, None]
    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color="#aaa"), hoverinfo="none", mode="lines")

    node_x, node_y, node_text, node_color = [], [], [], []
    for n, attrs in G.nodes(data=True):
        x, y = pos[n]
        node_x.append(x); node_y.append(y); node_text.append(n)
        node_color.append("#2ca02c" if attrs.get("kind") == "canal" else "#1f77b4")

    node_trace = go.Scatter(x=node_x, y=node_y, mode="markers+text", text=node_text,
                             textposition="top center", hoverinfo="text",
                             marker=dict(size=14, color=node_color, line=dict(width=1, color="white")))
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(showlegend=False, height=550, margin=dict(l=10, r=10, t=30, b=10),
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       title="Link Canal Network")
    return fig
