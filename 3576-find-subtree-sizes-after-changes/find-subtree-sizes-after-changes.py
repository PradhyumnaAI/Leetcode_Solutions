from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Step 1: Build initial tree adjacency list
        initial_children = []
        for _ in range(n):
            initial_children.append([])

        for node in range(1, n):
            p = parent[node]
            initial_children[p].append(node)

        # Step 2: Find final parent for each node via DFS with backtracking
        final_parent = [-1] * n
        last_seen = [-1] * 26  # Most recent ancestor for each character 'a'-'z'

        def dfs_reparent(u: int) -> None:
            char_index = ord(s[u]) - ord("a")
            prev_ancestor = last_seen[char_index]

            if u == 0:
                final_parent[u] = -1
            elif prev_ancestor != -1:
                final_parent[u] = prev_ancestor
            else:
                final_parent[u] = parent[u]

            last_seen[char_index] = u

            for child in initial_children[u]:
                dfs_reparent(child)

            # Restore previous ancestor state when backtracking
            last_seen[char_index] = prev_ancestor

        dfs_reparent(0)

        # Step 3: Build final tree adjacency list
        final_children = []
        for _ in range(n):
            final_children.append([])

        for node in range(1, n):
            new_p = final_parent[node]
            final_children[new_p].append(node)

        # Step 4: Compute subtree sizes in the final tree
        ans = [0] * n

        def dfs_size(u: int) -> int:
            subtree_count = 1
            for child in final_children[u]:
                subtree_count += dfs_size(child)
            ans[u] = subtree_count
            return subtree_count

        dfs_size(0)
        return ans