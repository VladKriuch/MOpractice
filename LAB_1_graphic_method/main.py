#
#
# -x1 + x2 -> min(max)

# x1 + x2 <= 1
# x1-2x2 <=1
# 2x1 + 3x2 <= 2
# 3x1 + 2x2 <= 3
# x1 + x2 >= 0.5

# Solving linear problem
import pulp
import matplotlib.pyplot as plt
import numpy as np


def solve_linear_problem(target, objective_func, *ineqs):
    Linear_problem = pulp.LpProblem('Linear_Problem', target)
    # Create problem Variables
    x1 = pulp.LpVariable("x1")
    x2 = pulp.LpVariable("x2")

    Linear_problem += (-1) * x1 + x2

    Linear_problem += x1 + x2 <= 1
    Linear_problem += x1 - 2 * x2 <= 1
    Linear_problem += 2 * x1 + 3 * x2 <= 2
    Linear_problem += 3 * x1 + 2 * x2 <= 3
    Linear_problem += x1 + x2 >= 0.5

    print(Linear_problem)

    status = Linear_problem.solve()

    print(pulp.LpStatus[status])  # The solution status

    # Printing the final solution
    print(pulp.value(x1), pulp.value(x2), pulp.value(Linear_problem.objective))

def draw_graphs():
    x1 = np.arange(-5, 5)
    # x1 + x2 <= 1
    # x1-2x2 <=1
    # 2x1 + 3x2 <= 2
    # 3x1 + 2x2 <= 3
    # x1 + x2 >= 0.5
    plt.plot(x1, 1-x1, label='x1 + x2 <= 1')
    plt.plot(x1, (x1 - 1) / 2, label='x1- 2*x2 <=1')
    plt.plot(x1, (2 - 2 * x1) / 3, label='2x1 + 3x2 <= 2')
    plt.plot(x1, (3 - 3 * x1) / 2, label='3x1 + 2x2 <= 3')
    plt.plot(x1, 0.5 - x1, label='x1 + x2 >= 0.5')

    x1_points = [-0.5, 1, 2/3]
    x2_points = [1, 0, -1/6]

    plt.plot(x1_points, x2_points, 'ro')
    for i_x, i_y in zip(x1_points, x2_points):
        plt.text(i_x, i_y, '({:.2f}, {:.2f})'.format(i_x, i_y))

    plt.fill(x1_points, x2_points)

    plt.axis([-2, 2, -2, 2])
    plt.grid(True)
    plt.legend()
    plt.show()

solve_linear_problem(pulp.LpMinimize)
print('-' * 10)
solve_linear_problem(pulp.LpMaximize)
draw_graphs()

