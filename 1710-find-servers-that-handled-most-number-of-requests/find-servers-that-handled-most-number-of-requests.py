import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to store (free_time, server_id)
        busy_servers = []
        
        # We can use a sorted list or an array with bisect to manage available servers.
        # Python's built-in bisect on a sorted list of available servers:
        available = list(range(k))
        
        request_counts = [0] * k
        
        for i, (arr_time, l) in enumerate(zip(arrival, load)):
            # 1. Free up servers whose tasks have finished by arr_time
            while busy_servers and busy_servers[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy_servers)
                # Insert back into available while maintaining sorted order
                bisect.insort(available, server_id)
            
            if not available:
                # All servers are busy, drop this request
                continue
            
            # 2. Find the next available server >= (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)
            
            if idx == len(available):
                # Wrap around to the beginning of the available servers list
                idx = 0
            
            server_id = available.pop(idx)
            
            # 3. Assign the request to the chosen server
            request_counts[server_id] += 1
            heapq.heappush(busy_servers, (arr_time + l, server_id))
            
        # 4. Find all servers with the maximum number of handled requests
        max_requests = max(request_counts)
        return [i for i, count in enumerate(request_counts) if count == max_requests]