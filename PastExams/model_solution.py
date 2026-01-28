import random

def squares_of_some_numbers(lst, k):
    return [x*x for x in lst if x%k == 0]

def separation(string):
    result = []
    cur_run = 0
    for i in range(1, len(string)):
        if string[i] == 'b':
            result.append(cur_run)
            cur_run = 0
        else:
            cur_run += 1
    return result

def find_boundary(lst):
    left, right = 0, len(lst)-1
    while left < right - 1:
        mid = (left + right)//2
        if lst[mid]:
            right = mid
        else:
            left = mid
    return left


def randomized_average(f, n, sample_size):
    return sum([ f(random.randint(0, n)) for _ in range(sample_size)]) / sample_size

def DFS(cur_vertex, graph, visited):
    visited[cur_vertex] = True
    for other in graph[cur_vertex]:
        if not visited[other]:
            DFS(other)

def count_connected_components(graph):
    visited = [ False for _ in graph ]
    connected_components = 0
    for v in range(len(graph)):
        if not visited[v]:
            connected_components += 1
            DFS(v, graph, visited)
    return connected_components

def backtracking(prefix, n, k):
    if len(prefix) == n:
        return 1
    start = max(0, len(prefix) - k)
    stop = min(n-1, len(prefix) + k)
    return sum([backtracking(prefix + [i], n, k) for i in range(start, stop+1) if i not in prefix])

def count_local_permutations(n, k):
    return backtracking([], n, k)
