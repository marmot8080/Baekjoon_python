from sys import stdin


def convert_connected_vertex_color(vertex):
    for i in range(vertex_count):
        if connected_vertex[vertex][i] == 1:
            if vertex_color[i] == 1:
                vertex_color[i] = 0
            elif vertex_color[i] == 0:
                vertex_color[i] = 1


def query_1(v1, v2):
    global vertex_count

    if vertex_color[v1] == vertex_color[v2]:
        if sum(connected_vertex[v1]) < sum(connected_vertex[v2]):
            convert_connected_vertex_color(v1)
        else:
            convert_connected_vertex_color(v2)
    
    adj_matrix[v1][v2] = 1
    adj_matrix[v2][v1] = 1
    
    for i in range(vertex_count):
        if connected_vertex[v1][i] == 1:
            connected_vertex[v2][i] = 1
            connected_vertex[i][v2] = 1
        elif connected_vertex[v2][i] == 1:
            connected_vertex[v1][i] = 1
            connected_vertex[i][v1] = 1


def query_2(vertex):
    convert_connected_vertex_color(vertex)


def query_3(color):
    global vertex_count

    max_count = 0
    min_vertex = 0
    visited_vertex = [0 for _ in range(vertex_count)]

    for i in range(vertex_count):
        if visited_vertex[i] == 1:
            continue

        count = 0

        for m in range(vertex_count):
            if connected_vertex[i][m] == 1:
                visited_vertex[m] = 1
        
        for j in range(vertex_count):
            if connected_vertex[i][j] == 1 and vertex_color[j] == color:
                count += 1
        
        if max_count < count:
            max_count = count
            min_vertex = i

    return min_vertex + 1


if __name__ == '__main__':
    vertex_count, query_count = map(int, stdin.readline().split())
    vertex_color = list(map(int, stdin.readline().split()))
    adj_matrix = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]
    connected_vertex = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]
    for i in range(vertex_count):
        connected_vertex[i][i] = 1

    for _ in range(query_count):
        query = list(map(int, stdin.readline().split()))
        
        if query[0] == 1:
            query_1(query[1] - 1, query[2] - 1)
        elif query[0] == 2:
            query_2(query[1] - 1)
        elif query[0] == 3:
            print(query_3(query[1]))