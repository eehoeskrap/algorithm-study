class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
    
        # grid의 행, 열 저장
        rows, cols = len(grid), len(grid[0])
    
        # 갈 수 있는 방향 정의, 순서대로 왼쪽, 오른쪽, 아래, 위 
        ways = ((-1, 0), (1, 0), (0, 1), (0, -1))

        # BFS로 풀기위한 deque 정의 
        queue = deque()
    
        # 방문 여부 저장하기 위한 visited 변수를 set으로 정의 (set은 중복 없는 배열)
        visited = set()
        
        # k를 찾기위한 queue 초기값 설정 (row, col, removes_left, step)
        queue.append((0, 0, k, 0))
        
        # 방문여부 저장을 위한 초기값 설정 (row, col, step)
        visited.add((0, 0, k))
        
        while queue:
            cell = queue.popleft()
            cell_row, cell_col, removes_left, step = cell 
            
            # 도착 지점에 도달하면 step 값을 리턴
            if cell_row == rows-1 and cell_col == cols-1:
                return step
            
            for way_row, way_col in ways:
                
                # 현재 지점에서 한개씩 이동하며 확인 
                row = cell_row + way_row
                col = cell_col + way_col
                
                # 이 때 갈 수 있는 방향이어야 하고, 방문된적 없어야 함 
                if (row in range(rows)) and (col in range(cols)) and ((row, col, removes_left) not in visited):
                    # 해당 grid 가 0이면 갈 수 있는 값 
                    if grid[row][col] == 0:
                        # queue에 순회하는 값 추가
                        queue.append((row, col, removes_left, step + 1))
                        #방문 노드 추가
                        visited.add((row, col, removes_left))
                    # 장애물일 때
                    elif grid[row][col] == 1:
                        # 처음부터 장애물은 아닐테니까 0보다 커야함
                        if removes_left > 0:
                            # queue에 순회하는 값 추가 단, 장애물 삭제하며 step 사이즈를 늘려줌 
                            queue.append((row, col, removes_left - 1, step + 1))
                            # 방문 노드 추가
                            visited.add((row, col, removes_left))
                
    
        return -1 