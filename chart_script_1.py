import plotly.graph_objects as go
import plotly.io as pio

# Data for the pathfinding algorithms comparison table
algorithms = ["BFS", "UCS", "A* Search", "Hill Climbing", "Sim. Anneal"]

algorithm_types = ["Uninformed", "Uninformed", "Informed", "Local Search", "Local Search"]
optimality = ["Optimal*", "Optimal", "Optimal**", "Sub-optimal", "Sub-optimal"]
completeness = ["Complete", "Complete", "Complete", "Incomplete", "Complete"]
time_complexity = ["O(b^d)", "O(b^(C*/ε))", "O(b^d)", "O(∞)", "O(∞)"]
space_complexity = ["O(b^d)", "O(b^(C*/ε))", "O(b^d)", "O(1)", "O(1)"]
best_use_case = ["Simple grids", "Weighted grids", "Static env", "Quick solutions", "Dynamic replan"]

# Create the table
fig = go.Figure(data=[go.Table(
    columnwidth=[80, 80, 70, 70, 80, 80, 90],
    header=dict(
        values=['<b>Algorithm</b>', '<b>Algorithm Type</b>', '<b>Optimality</b>', '<b>Completeness</b>', 
                '<b>Time Complex</b>', '<b>Space Complex</b>', '<b>Best Use Case</b>'],
        line_color='darkslategray',
        fill_color='#1FB8CD',
        align='center',
        font=dict(color='white', size=12),
        height=40
    ),
    cells=dict(
        values=[algorithms, algorithm_types, optimality, completeness, 
                time_complexity, space_complexity, best_use_case],
        line_color='darkslategray',
        fill_color=[['#F8F9FA', '#E9ECEF'] * 3],  # Alternating row colors
        align='center',
        font=dict(color='black', size=11),
        height=35
    ))
])

# Update layout
fig.update_layout(
    title='Pathfinding Algorithm Comparison',
    font=dict(family="Arial", size=12)
)

# Save as PNG and SVG
fig.write_image("pathfinding_comparison.png")
fig.write_image("pathfinding_comparison.svg", format="svg")

fig.show()