class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def push(self, node):
        if self.lazy[node]:
            val = self.lazy[node]
            self.tree[2 * node] ^= val
            self.lazy[2 * node] ^= val
            self.tree[2 * node + 1] ^= val
            self.lazy[2 * node + 1] ^= val
            self.lazy[node] = 0

    def update_range(self, node, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self.tree[node] ^= val
            self.lazy[node] ^= val
            return
        self.push(node)
        mid = (l + r) // 2
        if ql <= mid:
            self.update_range(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update_range(2 * node + 1, mid + 1, r, ql, qr, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query_point(self, node, l, r, idx):
        if l == r:
            return self.tree[node]
        self.push(node)
        mid = (l + r) // 2
        if idx <= mid:
            return self.query_point(2 * node, l, mid, idx)
        else:
            return self.query_point(2 * node + 1, mid + 1, r, idx)


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        import sys
        sys.setrecursionlimit(200000)
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        sz = [0] * n
        
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            sz[u] = 1
            max_sub = 0
            for v in adj[u]:
                if v != p:
                    dfs1(v, u, d + 1)
                    sz[u] += sz[v]
                    if sz[v] > max_sub:
                        max_sub = sz[v]
                        heavy[u] = v
        dfs1(0, -1, 0)
        
        cur_pos = 0
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)
        dfs2(0, 0)
        
        seg = E = SegmentTree(n)
        
        # Initialize segment tree with character masks
        char_masks = [1 << (ord(c) - ord('a')) for c in s]
        for i in range(n):
            seg.update_range(1, 0, n - 1, pos[i], pos[i], char_masks[i])
            
        def get_path_xor(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                # Query range from pos[head[v]] to pos[v]
                # Since we want path XOR, we can extract using point queries or subtree updates
                # For HLD range query over XOR:
                pass
            return res

        # Standard LCA via Binary Lifting for speed
        LOG = 18
        up = [[-1] * LOG for _ in range(n)]
        for i in range(n):
            up[i][0] = parent[i]
        for j in range(1, LOG):
            for i in range(n):
                if up[i][j - 1] != -1:
                    up[i][j] = up[up[i][j - 1]][j - 1]
                    
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for j in range(LOG - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return parent[u]

        # Helper to query path XOR using HLD chains
        def query_path(u, v):
            ans = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                # We need range XOR from pos[head[u]] to pos[u]
                # Segment tree range XOR query helper:
                ans ^= seg_query_range(1, 0, n - 1, pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            ans ^= seg_query_range(1, 0, n - 1, pos[u], pos[v])
            return ans

        # Segment tree range query function for XOR
        def seg_query_range(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return seg.tree[node]
            seg.push(node)
            mid = (l + r) // 2
            res = 0
            if ql <= mid:
                res ^= seg_query_range(2 * node, l, mid, ql, qr)
            if qr > mid:
                res ^= seg_query_range(2 * node + 1, mid + 1, r, ql, qr)
            return res

        results = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                old_mask = char_masks[u]
                if new_mask != old_mask:
                    diff = old_mask ^ new_mask
                    seg.update_range(1, 0, n - 1, pos[u], pos[u], diff)
                    char_masks[u] = new_mask
            else:
                u, v = int(parts[1]), int(parts[2])
                path_mask = query_path(u, v)
                # Check if at most one bit is set
                if path_mask == 0 or (path_mask & (path_mask - 1)) == 0:
                    results.append(True)
                else:
                    results.append(False)
                    
        return results