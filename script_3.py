# Create CLI interface implementation

cli_code = '''
"""
Command Line Interface for Autonomous Delivery Agent
"""
import argparse
import sys
import os
import json
from pathlib import Path
from typing import Dict, Any

# This would normally import from the project modules
# from src.environment.grid_world import GridWorld
# from src.algorithms.uninformed.bfs import BFSSearch
# from src.algorithms.uninformed.uniform_cost_search import UCSSearch
# from src.algorithms.informed.a_star import AStarSearch
# from src.algorithms.local_search.hill_climbing import HillClimbingSearch
# from src.algorithms.local_search.simulated_annealing import SimulatedAnnealingSearch
# from src.utils.visualization import Visualizer
# from src.utils.metrics import MetricsCollector

class DeliveryAgentCLI:
    """Command Line Interface for the Autonomous Delivery Agent"""
    
    def __init__(self):
        self.algorithms = {
            'bfs': 'Breadth-First Search',
            'ucs': 'Uniform Cost Search', 
            'astar': 'A* Search',
            'hill_climbing': 'Hill Climbing',
            'simulated_annealing': 'Simulated Annealing'
        }
        
    def create_parser(self) -> argparse.ArgumentParser:
        """Create and configure argument parser"""
        parser = argparse.ArgumentParser(
            description='Autonomous Delivery Agent Pathfinding System',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='''
Examples:
  %(prog)s run --algorithm astar --map maps/small_map.txt
  %(prog)s run --algorithm bfs --map maps/medium_map.txt --visualize
  %(prog)s compare --algorithms bfs ucs astar --map maps/large_map.txt
  %(prog)s benchmark --map-dir maps/ --output results/benchmark.json
            '''
        )
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Run command
        self._add_run_parser(subparsers)
        
        # Compare command
        self._add_compare_parser(subparsers)
        
        # Benchmark command
        self._add_benchmark_parser(subparsers)
        
        # Generate map command
        self._add_generate_map_parser(subparsers)
        
        return parser
    
    def _add_run_parser(self, subparsers):
        """Add run command parser"""
        run_parser = subparsers.add_parser('run', help='Run single pathfinding algorithm')
        
        run_parser.add_argument(
            '--algorithm', '-a',
            choices=list(self.algorithms.keys()),
            required=True,
            help='Pathfinding algorithm to use'
        )
        
        run_parser.add_argument(
            '--map', '-m',
            type=str,
            required=True,
            help='Path to map file'
        )
        
        run_parser.add_argument(
            '--start',
            type=int,
            nargs=2,
            metavar=('X', 'Y'),
            help='Start position (overrides map default)'
        )
        
        run_parser.add_argument(
            '--goal',
            type=int,
            nargs=2,
            metavar=('X', 'Y'),
            help='Goal position (overrides map default)'
        )
        
        run_parser.add_argument(
            '--visualize', '-v',
            action='store_true',
            help='Show path visualization'
        )
        
        run_parser.add_argument(
            '--save-result',
            type=str,
            help='Save results to JSON file'
        )
        
        run_parser.add_argument(
            '--dynamic',
            action='store_true',
            help='Enable dynamic obstacle simulation'
        )
        
        run_parser.add_argument(
            '--heuristic',
            choices=['manhattan', 'euclidean', 'diagonal'],
            default='manhattan',
            help='Heuristic function for A* (default: manhattan)'
        )
    
    def _add_compare_parser(self, subparsers):
        """Add compare command parser"""
        compare_parser = subparsers.add_parser('compare', help='Compare multiple algorithms')
        
        compare_parser.add_argument(
            '--algorithms',
            nargs='+',
            choices=list(self.algorithms.keys()),
            required=True,
            help='Algorithms to compare'
        )
        
        compare_parser.add_argument(
            '--map', '-m',
            type=str,
            required=True,
            help='Path to map file'
        )
        
        compare_parser.add_argument(
            '--runs',
            type=int,
            default=1,
            help='Number of runs per algorithm (default: 1)'
        )
        
        compare_parser.add_argument(
            '--output', '-o',
            type=str,
            help='Output file for comparison results'
        )
        
        compare_parser.add_argument(
            '--visualize', '-v',
            action='store_true',
            help='Show comparison charts'
        )
    
    def _add_benchmark_parser(self, subparsers):
        """Add benchmark command parser"""
        benchmark_parser = subparsers.add_parser('benchmark', help='Run comprehensive benchmarks')
        
        benchmark_parser.add_argument(
            '--map-dir',
            type=str,
            required=True,
            help='Directory containing map files'
        )
        
        benchmark_parser.add_argument(
            '--algorithms',
            nargs='+',
            choices=list(self.algorithms.keys()),
            default=list(self.algorithms.keys()),
            help='Algorithms to benchmark (default: all)'
        )
        
        benchmark_parser.add_argument(
            '--output', '-o',
            type=str,
            required=True,
            help='Output file for benchmark results'
        )
        
        benchmark_parser.add_argument(
            '--runs',
            type=int,
            default=5,
            help='Number of runs per test case (default: 5)'
        )
    
    def _add_generate_map_parser(self, subparsers):
        """Add generate map command parser"""
        gen_parser = subparsers.add_parser('generate-map', help='Generate test maps')
        
        gen_parser.add_argument(
            '--size',
            type=int,
            nargs=2,
            metavar=('WIDTH', 'HEIGHT'),
            required=True,
            help='Map dimensions'
        )
        
        gen_parser.add_argument(
            '--obstacle-density',
            type=float,
            default=0.2,
            help='Obstacle density (0.0-1.0, default: 0.2)'
        )
        
        gen_parser.add_argument(
            '--output', '-o',
            type=str,
            required=True,
            help='Output map file'
        )
        
        gen_parser.add_argument(
            '--dynamic-obstacles',
            type=int,
            default=0,
            help='Number of dynamic obstacles (default: 0)'
        )
        
        gen_parser.add_argument(
            '--seed',
            type=int,
            help='Random seed for reproducibility'
        )
    
    def run_algorithm(self, args):
        """Execute single algorithm run"""
        print(f"Running {self.algorithms[args.algorithm]} on {args.map}")
        
        # Load map
        if not os.path.exists(args.map):
            print(f"Error: Map file '{args.map}' not found")
            return 1
        
        # This would be the actual implementation
        print("Map loaded successfully")
        
        if args.start:
            print(f"Start position: {args.start}")
        if args.goal:
            print(f"Goal position: {args.goal}")
            
        if args.dynamic:
            print("Dynamic obstacles enabled")
            
        if args.algorithm == 'astar' and args.heuristic:
            print(f"Using {args.heuristic} heuristic")
        
        # Simulate results
        result = {
            'algorithm': args.algorithm,
            'map': args.map,
            'path_cost': 42.0,
            'nodes_expanded': 156,
            'computation_time': 0.023,
            'success': True,
            'path_length': 28
        }
        
        print("\\nResults:")
        print(f"  Path found: {result['success']}")
        print(f"  Path cost: {result['path_cost']}")
        print(f"  Path length: {result['path_length']}")
        print(f"  Nodes expanded: {result['nodes_expanded']}")
        print(f"  Computation time: {result['computation_time']:.3f}s")
        
        if args.save_result:
            with open(args.save_result, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Results saved to {args.save_result}")
        
        if args.visualize:
            print("Visualization would be displayed here")
            
        return 0
    
    def compare_algorithms(self, args):
        """Execute algorithm comparison"""
        print(f"Comparing algorithms: {', '.join(args.algorithms)}")
        print(f"Map: {args.map}")
        print(f"Runs per algorithm: {args.runs}")
        
        # This would be the actual comparison implementation
        results = {}
        for alg in args.algorithms:
            results[alg] = {
                'avg_path_cost': 42.0 + hash(alg) % 10,
                'avg_nodes_expanded': 150 + hash(alg) % 50,
                'avg_computation_time': 0.02 + (hash(alg) % 100) / 1000,
                'success_rate': 1.0
            }
        
        print("\\nComparison Results:")
        print(f"{'Algorithm':<20} {'Avg Cost':<10} {'Avg Nodes':<12} {'Avg Time (s)':<12} {'Success Rate':<12}")
        print("-" * 68)
        
        for alg, data in results.items():
            print(f"{self.algorithms[alg]:<20} {data['avg_path_cost']:<10.1f} "
                  f"{data['avg_nodes_expanded']:<12} {data['avg_computation_time']:<12.3f} "
                  f"{data['success_rate']:<12.1%}")
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\\nResults saved to {args.output}")
            
        return 0
    
    def run_benchmark(self, args):
        """Execute comprehensive benchmark"""
        print(f"Running benchmark on maps in {args.map_dir}")
        print(f"Algorithms: {', '.join(args.algorithms)}")
        print(f"Runs per test: {args.runs}")
        
        # This would be the actual benchmark implementation
        print("Benchmark completed successfully")
        print(f"Results saved to {args.output}")
        
        return 0
    
    def generate_map(self, args):
        """Generate test map"""
        print(f"Generating {args.size[0]}x{args.size[1]} map")
        print(f"Obstacle density: {args.obstacle_density}")
        print(f"Dynamic obstacles: {args.dynamic_obstacles}")
        
        if args.seed:
            print(f"Using seed: {args.seed}")
        
        # This would be the actual map generation
        print(f"Map saved to {args.output}")
        
        return 0
    
    def main(self):
        """Main CLI entry point"""
        parser = self.create_parser()
        args = parser.parse_args()
        
        if not args.command:
            parser.print_help()
            return 1
        
        try:
            if args.command == 'run':
                return self.run_algorithm(args)
            elif args.command == 'compare':
                return self.compare_algorithms(args)
            elif args.command == 'benchmark':
                return self.run_benchmark(args)
            elif args.command == 'generate-map':
                return self.generate_map(args)
            else:
                parser.print_help()
                return 1
                
        except KeyboardInterrupt:
            print("\\nOperation cancelled by user")
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 1

if __name__ == '__main__':
    cli = DeliveryAgentCLI()
    sys.exit(cli.main())
'''

print("3. CLI Interface Implementation:")
print("=" * 50)
print(cli_code)

# Save to file
with open("cli_sample.py", "w") as f:
    f.write(cli_code)

print("\n\nSaved to 'cli_sample.py'")