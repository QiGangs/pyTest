#!/usr/bin/python
# -*- coding: UTF-8 -*-



debug = 0
MAX_NUM = 10000
v_num = 6

grapharr = [[0, 6, 1, 5, MAX_NUM, MAX_NUM],
            [6, 0, 5, MAX_NUM, 3, MAX_NUM],
            [1, 5, 0, 5, 5, 4],
            [5, MAX_NUM, 5, 0, MAX_NUM, 2],
            [MAX_NUM, 3, 6, MAX_NUM, 0, 6],
            [MAX_NUM, MAX_NUM, 4, 2, 6, 0],
            ]

######################################
# U放已经匹配好的顶点:
U = []
# V初始化为所有顶点的集合:
V = []
# T放各个边:
T = []


def init():
    if (debug):
        print ("grapharr=","")
        print(grapharr)
    i = 0
    while i < v_num:
        V.append(i + 1)
        i = i + 1
    if (graph_check() == "合法"):
        print("合法")
    else:
        print("非法")
        exit(1)


def graph_check():
    print("检查图表数组是否合法")
    return "合法"


def prim_start_vertex(start):
    if (start < 1):
        print("ERROR:start=", start)
        print("ERROR:change start to 1 by default!")
        start = 1

    U.append(start)
    del V[start - 1]


def list_sort(l):
    if (len(l) < 1):
        print("ERROR:len of l =", len(l))
        exit(1)

    index = 0
    i = 0
    min_val = l[0]
    while i < len(l):
        if min_val > l[i]:
            min_val = l[i]
            index = i

        i = i + 1
    if (debug):
        print("[list_sort]:l=", l, ";index=", index)
    return index


def min_wui():
    m = MAX_NUM
    close_edge = {'u': -1, 'v': -1}
    edge_list = []
    vertex_list = []
    i = 0
    j = 0
    # 算出U和V之间所有边的长度:
    lu = len(U)
    lv = len(V)
    if (debug):
        print("##############entry min_wui###########")
        print("lu=", lu, ";lv=", lv)
    while i < len(U):
        while j < len(V):
            if (debug):
                print("i=", i, ";j=", j)
                print("U[i]=", U[i], ";V[j]=", V[j])
            temp = grapharr[U[i] - 1][V[j] - 1]
            if (temp > 0):
                if (temp < MAX_NUM):
                    close_edge = {'u': U[i], 'v': V[j]}
                if (debug):
                    print("close_edge=", close_edge)
                vertex_list.append(close_edge)
                edge_list.append(temp)

            j = j + 1
        # for i:
        i = i + 1
        j = 0
    # end of :for while i
    if (debug):
        print("vertex_list=", vertex_list)
        print("edge_list=", edge_list)
    min_index = list_sort(edge_list)
    close_edge = vertex_list[min_index]
    U.append(close_edge['v'])
    del V[V.index(close_edge['v'])]
    if (debug):
        print("U=", U)
        print("V=", V)
    return close_edge


def py_prim(start):
    init()
    prim_start_vertex(start)
    print("init values:")
    print("U=", U)
    print("V=", V)
    print("T=", T)
    while (len(U) != v_num):
        if (debug):
            print("len(U)=", len(U))
        our_edge = min_wui()
        T.append(our_edge)

    print("========RESULT============")
    print("U=", U)
    print("V=", V)
    print("T=", T)


######################################
if (__name__ == "__main__"):
    # 开始主程序:
    debug = 0
    py_prim(1)



