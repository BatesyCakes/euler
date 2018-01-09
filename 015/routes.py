"""The problem is simplified in that you may only move right or down
in order to reach the end goal. In the 20x20 grid there will only
be 40 possible moves with 20 moves right and 20 moves down. The solution
involves finding all of the combinations of right and down moves.
This is a simple combinatorics problem."""

from scipy.special import comb

def grid_routes(n,m):
    """Takes an n x m grid and computes the number of routes through
    the grid."""

    routes = comb(n + m, n)
    return routes

print (grid_routes(20,20))
