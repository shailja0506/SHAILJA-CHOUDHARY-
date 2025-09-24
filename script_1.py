# Create sample implementation templates for key project components

# 1. Grid Environment Class
grid_world_code = '''
"""
Grid-based environment for autonomous delivery agent
"""
import numpy as np
from typing import List, Tuple, Optional
from enum import Enum

class CellType(Enum):
    FREE = 0
    OBSTACLE = 1
    START = 2
    GOAL = 3
    MOVING_OBSTACLE = 4

class GridWorld:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.start = None
        self.goal = None
        self.dynamic_obstacles = {}  # time -> [(x, y), ...]
        
    def add_static_obstacle(self, x: int, y: int):
        """Add a static obstacle to the grid"""
        if self.is_valid_position(x, y):
            self.grid[y, x] = CellType.OBSTACLE.value
            
    def add_dynamic_obstacle(self, positions: List[Tuple[int, int, int]]):
        """Add dynamic obstacle with time-position pairs"""
        for x, y, time in positions:
            if time not in self.dynamic_obstacles:
                self.dynamic_obstacles[time] = []
            self.dynamic_obstacles[time].append((x, y))
            
    def set_start_goal(self, start: Tuple[int, int], goal: Tuple[int, int]):
        """Set start and goal positions"""
        self.start = start
        self.goal = goal
        if self.is_valid_position(*start):
            self.grid[start[1], start[0]] = CellType.START.value
        if self.is_valid_position(*goal):
            self.grid[goal[1], goal[0]] = CellType.GOAL.value
            
    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if position is within grid bounds"""
        return 0 <= x < self.width and 0 <= y < self.height
        
    def is_obstacle(self, x: int, y: int, time: int = 0) -> bool:
        """Check if position is obstacle at given time"""
        if not self.is_valid_position(x, y):
            return True
        
        # Check static obstacles
        if self.grid[y, x] == CellType.OBSTACLE.value:
            return True
            
        # Check dynamic obstacles
        if time in self.dynamic_obstacles:
            return (x, y) in self.dynamic_obstacles[time]
            
        return False
        
    def get_neighbors(self, x: int, y: int, time: int = 0) -> List[Tuple[int, int]]:
        """Get valid neighboring positions (4-connected)"""
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid_position(nx, ny) and not self.is_obstacle(nx, ny, time):
                neighbors.append((nx, ny))
                
        return neighbors
        
    def get_terrain_cost(self, x: int, y: int) -> int:
        """Get movement cost for a cell (can be extended for different terrain types)"""
        if self.is_obstacle(x, y):
            return float('inf')
        return 1  # Default cost
        
    def save_to_file(self, filename: str):
        """Save grid to file"""
        with open(filename, 'w') as f:
            f.write(f"{self.width} {self.height}\\n")
            if self.start:
                f.write(f"START {self.start[0]} {self.start[1]}\\n")
            if self.goal:
                f.write(f"GOAL {self.goal[0]} {self.goal[1]}\\n")
            
            for y in range(self.height):
                for x in range(self.width):
                    f.write(f"{self.grid[y, x]} ")
                f.write("\\n")
                
    @classmethod
    def load_from_file(cls, filename: str):
        """Load grid from file"""
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        width, height = map(int, lines[0].strip().split())
        grid = cls(width, height)
        
        line_idx = 1
        while line_idx < len(lines) and not lines[line_idx].strip().split()[0].isdigit():
            parts = lines[line_idx].strip().split()
            if parts[0] == "START":
                grid.start = (int(parts[1]), int(parts[2]))
            elif parts[0] == "GOAL":
                grid.goal = (int(parts[1]), int(parts[2]))
            line_idx += 1
            
        # Load grid data
        for y in range(height):
            if line_idx + y < len(lines):
                row = list(map(int, lines[line_idx + y].strip().split()))
                for x in range(min(width, len(row))):
                    grid.grid[y, x] = row[x]
                    
        return grid
'''

print("1. Grid World Environment Implementation:")
print("=" * 50)
print(grid_world_code)

# Save to file
with open("grid_world_sample.py", "w") as f:
    f.write(grid_world_code)

print("\n\nSaved to 'grid_world_sample.py'")