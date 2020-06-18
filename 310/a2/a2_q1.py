# a2_q1

'''
generate a new random graph with n nodes numbered 0 to n-1 s.t.
every different pair of nodes is connected with probability p
Assume n > 1, and 0 <= p <= 1
'''

import random


def rand_graph(p, n):
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if j not in graph[i]:
                # generate a random number compare to p
                pr = random.randint(1, 101) / 100
                if pr <= p:
                    graph[i].append(j)
                    graph[j].append(i)
    return graph


def main():
    graph = rand_graph(0.5, 10)
    print(graph)


if __name__ == '__main__':
    main()
