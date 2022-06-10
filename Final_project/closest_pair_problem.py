"""
The closest pair of points problem or closest pair problem is a problem of computational geometry:
 given n points in metric space, find a pair of points with the smallest distance between them.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.spatial as spatial
from mpl_toolkits.mplot3d import Axes3D


def show_2d(r_pts, closest):
    if closest == None:
        plt.plot(r_pts[:, 1], r_pts[:, 0], 'b.')
        plt.show()
    else:
        plt.plot(r_pts[:, 1], r_pts[:, 0], 'b.')
        # recolour closest points
        plt.plot([r_pts[closest[0], 1], r_pts[closest[1], 1]],
                 [r_pts[closest[0], 0], r_pts[closest[1], 0]],
                 'ro')
        plt.show()
    plt.close()


def show_3d(r_pts, closest):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if closest == None:
        ax.scatter(r_pts[:, 0], r_pts[:, 1], r_pts[:, 2], s=5, marker='.')  # x,y,z
        plt.show()
    else:
        ax.scatter(r_pts[:, 0], r_pts[:, 1], r_pts[:, 2], s=5, marker='.')  # x,y,z
        ax.scatter(r_pts[closest[0], 0], r_pts[closest[0], 1], r_pts[closest[0], 2], s=50, c='r')
        ax.scatter(r_pts[closest[1], 0], r_pts[closest[1], 1], r_pts[closest[1], 2], s=50, c='r')
        plt.show()
    plt.close()


def get_closest_pair(r_pts):
    # make kdtree and self compare
    # compute the distances (take the 2 closest as the
    # first distance is a self-comparison.
    distances, indexes = spatial.cKDTree(r_pts).query(r_pts, 2)

    # find minimum non self-reference distance
    mindist_pos = np.argmin(distances[:, 1])
    print('L2-norm distance', distances[mindist_pos, 1])
    print('pt1 coords', r_pts[mindist_pos])
    print('pt2 coords', r_pts[indexes[mindist_pos, 1]])

    # return the two indexes associated with the minimum distance
    return mindist_pos, indexes[mindist_pos, 1]


def main():
    # get grid size
    n_points = int(input('please enter number of random points: '))
    dims = int(input('please enter the number (e.g. 2,3,4,...) of dimensions (2D or 3D will plot): '))

    # make random x and y values
    random_points = np.random.rand(n_points, dims)

    # find the closest point pair
    closest_index = get_closest_pair(random_points)

    # replot
    if dims == 2:
        show_2d(random_points, closest_index)
    if dims == 3:
        show_3d(random_points, closest_index)


if __name__ == '__main__':
    sys.exit(main())
