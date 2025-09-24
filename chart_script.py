# Create the mermaid flowchart for autonomous delivery agent architecture
diagram_code = """
flowchart TD
    A[Initialize Agent] --> B[Load Environment<br/>Grid, Obstacles,<br/>Start, Goal]
    B --> C{Algorithm Type?}
    C -->|Uninformed| D[Execute BFS/UCS]
    C -->|Informed| E[Execute A*<br/>with Heuristic]
    C -->|Local Search| F[Execute Hill<br/>Climbing/SA]
    D --> G[Generate Path]
    E --> G
    F --> G
    G --> H[Execute Path<br/>Step by Step]
    H --> I{Dynamic Obstacle<br/>Detected?}
    I -->|Yes| J[Trigger<br/>Replanning]
    J --> C
    I -->|No| K[Continue Path<br/>Execution]
    K --> L{Goal Reached?}
    L -->|No| H
    L -->|Yes| M[Mission<br/>Complete]
    
    %% Performance metrics
    N[Record: Cost,<br/>Nodes, Time]
    D --> N
    E --> N
    F --> N
    
    %% Styling for different algorithm types
    classDef uninformed fill:#B3E5EC
    classDef informed fill:#FFCDD2
    classDef local fill:#A5D6A7
    
    class D uninformed
    class E informed
    class F local
"""

# Create the diagram using the mermaid helper function
png_path, svg_path = create_mermaid_diagram(diagram_code, "autonomous_delivery_flowchart.png", "autonomous_delivery_flowchart.svg")

print(f"Flowchart saved as: {png_path} and {svg_path}")