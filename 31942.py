def get_connected_vertex_count(vertex):
    count = 0

    connected_vertex = [0 for _ in range(vertex_count)]
    connected_vertex = get_connected_vertex(vertex, connected_vertex)

    for i in range(vertex_count):
        if connected_vertex[i] == 1:
            count += 1
    
    return count

def get_connected_vertex(vertex, connected_vertex):
    connected_vertex[vertex] = 1

    for i in range(vertex_count):
        if adj_matrix[vertex][i] == 1:
            connected_vertex[i] = 1

    for i in range(vertex_count):
        min = i
        if connected_vertex[i] == 1:
            for j in range(vertex_count):
                if connected_vertex[j] == 0 and adj_matrix[i][j] == 1:
                    connected_vertex[j] = 1
                    if j < min:
                        min = j
        if min < i:
            i = min

    return connected_vertex

def convert_connected_vertex_color(vertex):
    connected_vertex = [0 for _ in range(vertex_count)]
    connected_vertex = get_connected_vertex(vertex, connected_vertex)

    for i in range(vertex_count):
        if connected_vertex[i] == 1 and vertex_color[i] == 1:
            vertex_color[i] = 0
        elif connected_vertex[i] == 1 and vertex_color[i] == 0:
            vertex_color[i] = 1

def execute_query_1(v1, v2):
    if vertex_color[v1] == vertex_color[v2]:
        if get_connected_vertex_count(v1) < get_connected_vertex_count(v2):
            convert_connected_vertex_color(v1)
        else:
            convert_connected_vertex_color(v2)
    
    adj_matrix[v1][v2] = 1
    adj_matrix[v2][v1] = 1

def execute_query_2(vertex):
    convert_connected_vertex_color(vertex)

def execute_query_3(color):
    max_count = 0
    min_vertex_num = 0
    visited_vertex = [0 for _ in range(vertex_count)]

    for i in range(vertex_count):
        if visited_vertex[i] == 1:
            continue

        count = 0

        connected_vertex = [0 for _ in range(vertex_count)]
        connected_vertex = get_connected_vertex(i, connected_vertex)

        for m in range(vertex_count):
            if connected_vertex[m] == 1:
                visited_vertex[m] = 1
        
        for j in range(vertex_count):
            if connected_vertex[j] == 1 and vertex_color[j] == color:
                count += 1
        
        if max_count < count:
            max_count = count
            min_vertex_num = i

    return min_vertex_num + 1

if __name__ == '__main__':
    global adj_matrix, vertex_color, vertex_count

    vertex_count, query_count = map(int, input().split())
    vertex_color = list(map(int, input().split()))
    adj_matrix = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]

    for _ in range(query_count):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            execute_query_1(query[1] - 1, query[2] - 1)
        elif query[0] == 2:
            execute_query_2(query[1] - 1)
        elif query[0] == 3:
            print(execute_query_3(query[1]))
        else:
            print("잘못된 쿼리입니다.")
            exit(1)