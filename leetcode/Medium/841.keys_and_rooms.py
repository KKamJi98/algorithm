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
    
s = Solution()
print(s.canVisitAllRooms([[1],[2],[3],[]]))
