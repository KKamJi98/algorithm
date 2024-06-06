from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        q = deque()
        for i in rooms[0]:
            visited[i] = True
            q.append(i)
        visited[0] = True
        
        while q:
            cur_room = q.popleft()
            for i in rooms[cur_room]:
                if visited[i] == False :
                    q.append(i)
                    visited[i] = True
    
        for ele in visited:
            if ele == False:
                return False
            
        return True
    
    def solution_dfs(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        def dfs(room_idx):
            visited[room_idx] = True
            for next_idx in rooms[room_idx]:
                if visited[next_idx] == False:
                    dfs(next_idx)
        dfs(0)
        
        return all(visited)
            
            
s = Solution()
print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
print(s.solution_dfs([[1,3],[3,0,1],[2],[0]]))
