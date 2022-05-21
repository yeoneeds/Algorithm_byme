from collections import deque
import sys

def dfs(graph, this_node, visited, res1): #dfs
    visited[this_node]=1 #들어온 점 방문처리
    res1.append(this_node) #방문한 노드 순서에 현재 노드 추가
    for node in graph[this_node]: #현재 노드가 있는 그래프와 연결된 노드 탐색
        if visited[node]!=1 and min(graph[this_node]): #만약 연결된 노드가 아직 방문하지 않은 노드라면
            dfs(graph, node, visited, res1) #dfs적용

def bfs(graph, start, visited): #bfs
    res2 = []
    q = deque()
    q.append(start)
    while q:
        node1 = q.popleft()
        visited[node1] = 1 #꺼냈으면 방문 처리
        res2.append(node1) #방문한 노드 방문 순서 리스트에 추가
        for nodes in graph[node1]:
            if (nodes not in q) and visited[nodes]!=1: #연결된 노드 중 덱에 없고 방문하지 않았다면 큐에 추가 
                q.append(nodes) #미방문 노드들만 추가
    return res2

def main():
    node, edge, start_node = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(node+1)]
    visited = [0] * (node+1)
    res1 = []
    for i in range(edge): #그래프 생성
        n1,n2 = map(int, sys.stdin.readline().split()) 
        graph[n1].append(n2) 
        graph[n2].append(n1)
        graph[n1].sort() #그래프에 새로운 노드 추가할 때 마다 해당 그래프 정렬
        graph[n2].sort()     
    
    dfs(graph, start_node, visited, res1) 
    visited = [0] * (node+1) #dfs 탐색 후 visited 리스트 초기화
    res2 = bfs(graph, start_node, visited)

    for i in res1:
        print(i, end= ' ')
    print()
    for i in res2:
        print(i, end=' ')

if __name__ == "__main__":
    main()