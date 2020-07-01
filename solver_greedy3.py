#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

mostclose_index_and_dist={}

def find_crossednode_and_swap(i,j,cities,path_list):
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

    if(crossed):
        #print(i,j)
        #print(x1,x2,x3,x4,y1,y2,y3,y4)
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
    return crossed



def solve(cities):
    path_list=[]
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])



    current_city = 0
    unvisited_cities = set(range(1, N))
    for i in range(N):
        closecity=min(set(range(N))-{i},
                        key=lambda city: dist[city][i])
        mostclose_index_and_dist[i]=[closecity,dist[closecity][i]]

    #print(mostclose_index_and_dist)

    tour = [current_city]

    while unvisited_cities:

        choose_list=[]#to put city whose closest sity is current_city
        for i in unvisited_cities:
            if mostclose_index_and_dist[i][0]==current_city:
                choose_list.append([mostclose_index_and_dist[i],i])

        if(len(choose_list)==0):
            print("case1")
            next_city = min(unvisited_cities,
                            key=lambda city: dist[current_city][city])
        else:
            print("case2_5")
            index=0#the last state of this is the index to choose.
            distchange=0
            if(len(unvisited_cities)>1):
                print("case2")
                for i in choose_list:
                    new_closest=min(unvisited_cities-{i[1]},
                                    key=lambda city: dist[i[1]][city])
                    tmp=i[0][1]
                    i[0][1]=dist[i[1]][new_closest]
                    i[0][0]=new_closest
                    print(i,new_closest,"new_closest")
                    #print(tmp,i[0][1],i[1],i[0][0])
                    if((i[0][1]-tmp)>distchange):
                        distchange=(i[0][1]-tmp)
                        index=i[1]
                new_closest=min(unvisited_cities-{mostclose_index_and_dist[current_city][0]},
                                key=lambda city: dist[i[1]][city])


                #print(tmp,i[0][1],i[1],i[0][0])
                if((new_closest-mostclose_index_and_dist[current_city][1])>distchange):
                    next_city=mostclose_index_and_dist[current_city][0]
                else:
                    next_city=index
            else:
                print("Last one",current_city)

                next_city=mostclose_index_and_dist[current_city][0]
                print("line 117",next_city)



        print(next_city)
        print(unvisited_cities)
        unvisited_cities.remove(next_city)
        path_list.append([current_city,next_city])
        #tour.append(next_city)
        current_city = next_city

        endswap=True

    while(True):
        endswap=True
        for i in range(N-1):#N-1 is a number of path

            for j in range(i+2, N-1):

                ifcrossed=find_crossednode_and_swap(i,j,cities,path_list)
                if(ifcrossed):
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
