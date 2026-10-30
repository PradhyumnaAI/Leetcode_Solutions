import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: u -> list of (v, weight)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Min-heap priority queue storing (current_distance, current_node, consecutive_count)
        # Initial state at node 0 with count 1 and distance 0
        pq = [(0, 0, 1)]
        
        # Distance dictionary to store the minimum weight to reach (node, count)
        # Using a dict or 2D array since constraints are n <= 50,000 and k <= 50
        dist = {}
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            # If we reached the destination node, return the distance
            if u == n - 1:
                return d
                
            if (u, count) in dist and dist[(u, count)] < d:
                continue
                
            for v, w in adj[u]:
                # Determine the consecutive count for the next node
                if labels[v] == labels[u]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                # Check constraint
                if next_count > k:
                    continue
                    
                next_d = d + w
                
                if (v, next_count) not in dist or next_d < dist[(v, next_count)]:
                    dist[(v, next_count)] = next_d
                    heapq.heappush(pq, (next_d, v, next_count))
                    
        return -1