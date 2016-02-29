# This code performs collision testing of convex 2D polyedra by means
# of the Hyperplane separation theorem, also known as Separating axis theorem (SAT).
#
# For more information visit:
# https://en.wikipedia.org/wiki/Hyperplane_separation_theorem
#
# Copyright (C) 2016, Juan Antonio Aldea Armenteros
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


# -*- coding: utf8 -*-

def normalize(v):
    from math import sqrt
    norm = sqrt(v[0] ** 2 + v[1] ** 2)
    return (v[0] / norm, v[1] / norm)

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1];

def edge_direction(p0, p1):
    return (p1[0] - p0[0], p1[1] - p0[1]);

def orthogonal(v):
    return (v[1], -v[0])

def vertices_to_edges(vertices):
    return [edge_direction(vertices[i], vertices[(i + 1) % len(vertices)]) \
        for i in range(len(vertices))]

def project(vertices, axis):
    dots = [dot(vertex, axis) for vertex in vertices]
    return [min(dots), max(dots)]

def contains(n, range_):
    a = range_[0]
    b = range_[1]
    if b < a:
        a = range_[1]
        b = range_[0]
    return (n >= a) and (n <= b);

def overlap(a, b):
    if contains(a[0], b):
        return True;
    if contains(a[1], b):
        return True;
    if contains(b[0], a):
        return True;
    if contains(b[1], a):
        return True;
    return False;

def separating_axis_theorem(vertices_a, vertices_b):
    edges_a = vertices_to_edges(vertices_a);
    edges_b = vertices_to_edges(vertices_b);

    edges = edges_a + edges_b

    axes = [normalize(orthogonal(edge)) for edge in edges]

    for i in range(len(axes)):
        projection_a = project(vertices_a, axes[i])
        projection_b = project(vertices_b, axes[i])
        overlapping = overlap(projection_a, projection_b)
        if not overlapping:
            return False;
    return True


def main():
    a_vertices = [(0, 0), (70, 0), (0, 70)]
    b_vertices = [(70, 70), (150, 70), (70, 150)]
    c_vertices = [(30, 30), (150, 70), (70, 150)]

    print (separating_axis_theorem(a_vertices, b_vertices))
    print (separating_axis_theorem(a_vertices, c_vertices))
    print (separating_axis_theorem(b_vertices, c_vertices))


if __name__ == "__main__":
    main()
