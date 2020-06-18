# a2_q2

'''
check if the given CSP solution dictionary csp_sol satisfies all the constraints in the friendship graph
yes: return true
no:  return false
'''
def check_teams(graph, csp_sol):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if csp_sol[graph[i][j]] == csp_sol[i]:
                return False
    return True


def main():
    # test case from assignment description page
    graph = {0: [1, 2], 1: [0], 2: [0], 3: []}

    # true case:
    csp_sol_true = {0:0, 1:1, 2:1, 3:0}
    print("True case test result: ", check_teams(graph, csp_sol_true))

    #false case:
    csp_sol_false = {0:1, 1:1, 2:1, 3:0}
    print("False case test result: ", check_teams(graph, csp_sol_false))

if __name__ == '__main__':
    main()


