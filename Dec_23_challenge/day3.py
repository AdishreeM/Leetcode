# https://leetcode.com/problems/minimum-time-visiting-all-points/
# 1266. Minimum Time Visiting All Points
# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

# You can move according to these rules:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# You have to visit the points in the same order as they appear in the array.
# You are allowed to pass through points that appear later in the order, but these do not count as visits.

# Optimal way of covering dist = Move diagonally as far as possible which is equal to min(x_dist, y_dist) then cover the remaining. => Total dist = max(x_dist, y_dist)

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x_now, y_now = 'inf', 'inf'
        ans = 0
        for point in points:
            if x_now == 'inf':
                x_now, y_now = point
            else:
                ans += max(abs(point[0]-x_now), abs(point[1]-y_now))
                x_now, y_now = point
        return ans