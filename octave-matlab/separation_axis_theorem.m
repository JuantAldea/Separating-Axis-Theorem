% This code performs collision testing of convex 2D polyedra by means
% of the Hyperplane separation theorem, also known as Separating axis theorem (SAT).
%
% For more information visit:
% https://en.wikipedia.org/wiki/Hyperplane_separation_theorem
%
% Copyright (C) 2016, Juan Antonio Aldea Armenteros
% This program is free software: you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
% GNU General Public License for more details.
%
% You should have received a copy of the GNU General Public License
% along with this program. If not, see <http://www.gnu.org/licenses/>.


function test = separating_axis_theorem(vertices_a, vertices_b)
    dirs_a = vertices_to_edges(vertices_a);
    dirs_b = vertices_to_edges(vertices_b);
    dirs = [dirs_a; dirs_b];
    for i = 1:length(dirs)
        dir = dirs(i, :);
        axis = [dir(2), -dir(1)];
        axis = axis/norm(axis);
        a = project(vertices_a, axis);
        b = project(vertices_b, axis);
        overlapping = overlap(a, b);
        if ~overlapping
            test = false;
            return;
        end
    end
    test = true;
end

function dirs = vertices_to_edges(vertices)
    directions = zeros(size(vertices));
    for i = 1:length(vertices) - 1
        p0 = vertices(i, :);
        p1 = vertices(i+1, :);
        directions(i,:) = (p1 - p0);
    end
    p0 = vertices(length(vertices), :);
    p1 = vertices(1, :);
    directions(length(vertices), :) = (p1 - p0);
    dirs = directions;
end

function min_max = project(vertices, axis)
    projections = zeros(1, length(vertices));
    for i = 1:length(vertices)
        projections(i) = dot(vertices(i, :), axis);
    end
    min_max = [min(projections), max(projections)];
end

function result = overlap(a, b)
    if contains(a(1), b)
        result = true;
        return
    end
    if contains(a(2), b)
        result = true;
        return
    end
    if contains(b(1), a)
        result = true;
        return
    end
    if contains(b(2), a)
        result = true;
        return
    end

    result = false;
end

function result = contains(n, range)
    result = (n >= min(range)) && (n <= max(range));
end
