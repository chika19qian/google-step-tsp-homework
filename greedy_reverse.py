#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def distlist(cities):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    return dist

def greedy(cities):
    N = len(cities)

    dist = distlist(cities)

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]
    total_distance = 0
    step_distances = []

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        distance1 = dist[current_city][next_city]
        step_distances.append(distance1)
        total_distance += dist[current_city][next_city]
        current_city = next_city
    
    total_distance += dist[current_city][tour[0]]
    step_distances.append(dist[current_city][tour[0]])

    #print(tour)
    #print(total_distance)
    #print(step_distances)
    return tour, total_distance

def solve(cities):
    tour,total_distance_before = greedy(cities)
    N = len(cities)
    dist = distlist(cities)
    current_city = tour[-1]
    unvisited_cities = set(range(N))
    unvisited_cities.remove(current_city)
    total_distance = 0
    step_distances = []
    t = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        t.append(next_city)
        distance1 = dist[current_city][next_city]
        step_distances.append(distance1)
        total_distance += dist[current_city][next_city]
        current_city = next_city

    total_distance += dist[current_city][t[0]]
    step_distances.append(dist[current_city][t[0]])

    #print(step_distances)
    #print("正着的",total_distance_before)
    #print("tour_new",t)
    #print("反着来的",total_distance)
    if total_distance_before <= total_distance:
        return tour
    else: 
        return t


if __name__ == '__main__':
    print(sys.argv)
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
