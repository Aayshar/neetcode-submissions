class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[ [] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited=set()
        components=0
        def dfs(node):
            visited.add(node)

            for neighbors in graph[node]:
                if neighbors not in visited:
                    dfs(neighbors)

        for node in range(n):
            if node not in visited:
                components+=1
                dfs(node)
        return components
        