"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = [None]*101
        copy_node = Node(node.val)
        visited[copy_node.val] = copy_node
        for current in node.neighbors:
            if not visited[current.val]:
                new_node = Node(current.val)
                copy_node.neighbors.append(new_node)
                self.dfs(current, new_node, visited)
            else:
                copy_node.neighbors.append(visited[current.val])
        return copy_node
    
    def dfs(self, curr_original: 'Node', node: 'Node',
            visited: List['Node']):
        """
        curr_original: Original node to traverse its neighbors
        node : current node, to build its neighbors from curr_original
        visited: List of visited nodes
        """
        visited[node.val] = node
        for neighbor in curr_original.neighbors:
            if not visited[neighbor.val]:
                new_node = Node(neighbor.val)
                node.neighbors.append(new_node)
                self.dfs(neighbor, new_node, visited)
            else:
                node.neighbors.append(visited[neighbor.val])
        
        
        