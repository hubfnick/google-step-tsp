#!/usr/bin/env python3

import sys
import math
import random
TEMP=1000
DECAY=0.99
ITER_NUM=300

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def if_node_cross(i,j,cities,path_list):
    #print(i,j)
    x1=cities[path_list[i][0]][0]
    y1=cities[path_list[i][0]][1]
    x2=cities[path_list[i][1]][0]
    y2=cities[path_list[i][1]][1]
    x3=cities[path_list[j][0]][0]
    y3=cities[path_list[j][0]][1]
    x4=cities[path_list[j][1]][0]
    y4=cities[path_list[j][1]][1]
    crossed=True
    s=(x1 - x2) * (y3 - y1) - (y1 - y2) * (x3 - x1)
    t = (x1 - x2) * (y4 - y1) - (y1 - y2) * (x4 - x1)
    if(s*t>0):
        crossed=False

    s=(x3 - x4) * (y1 - y3) - (y3 - y4) * (x1 - x3)
    t = (x3 - x4) * (y2 - y3) - (y3 - y4) * (x2 - x3)
    if(s*t>0):
        crossed=False



    return crossed,(distance(cities[path_list[i][0]],cities[path_list[j][0]])+distance(cities[path_list[j][1]],cities[path_list[i][1]])-distance(cities[path_list[i][0]],cities[path_list[i][1]])-distance(cities[path_list[j][0]],cities[path_list[j][1]]))

def swap_node(i,j,path_list):
    for k in range(1,(j-i+1)//2):
        tmp=path_list[i+k].copy()
        path_list[i+k]=path_list[j-k].copy()
        path_list[j-k]=tmp.copy()
    for k in range(1,(j-i)):
        tmp2=path_list[i+k][0]
        path_list[i+k][0]=path_list[i+k][1]
        path_list[i+k][1]=tmp2
    tmp2=path_list[i][1]
    path_list[i][1]=path_list[j][0]
    path_list[j][0]=tmp2
    #print(path_list)
    return



def solve(cities):
    path_list=[]
    N = len(cities)
    #print("print",N)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        #tour.append(next_city)
        path_list.append([current_city,next_city])
        current_city = next_city




    endswap=True
    while(True):
        endswap=True
        for i in range(N-1):#N-1 is a number of path

            for j in range(i+2, N-1):

                ifcrossed,_=if_node_cross(i,j,cities,path_list)
                if(ifcrossed):
                    swap_node(i,j,path_list)
                    endswap=False


        if(endswap):
            break



    for i in path_list:
        tour.append(i[1])

    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
