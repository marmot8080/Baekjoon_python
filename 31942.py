
def execute_query_1():
    return

def execute_query_2():
    return

def execute_query_3():
    return

if __name__ == '__main__':
    vertex_count, query_count = input().split(" ")
    vertex_color = input().split(" ")

    print(vertex_color)

    for i in range(int(query_count)):
        query = input().split(" ")
        
        if query[0] == 1:
            execute_query_1()
        elif query[0] == 2:
            execute_query_2()
        elif query[0] == 3:
            execute_query_3()
        else:
            print("잘못된 쿼리입니다.")
            exit(1)