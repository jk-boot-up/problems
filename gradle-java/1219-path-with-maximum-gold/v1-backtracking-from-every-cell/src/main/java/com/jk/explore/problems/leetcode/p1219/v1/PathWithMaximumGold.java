package com.jk.explore.problems.leetcode.p1219.v1;

import java.util.*;

public class PathWithMaximumGold {

    public int getMaximumGold(int[][] grid) {
        int best = 0;
        for (int r = 0; r < grid.length; r++)
            for (int c = 0; c < grid[0].length; c++)
                if (grid[r][c] > 0) best = Math.max(best, dfs(grid, r, c));
        return best;
    }

    private int dfs(int[][] g, int r, int c) {
        if (r < 0 || c < 0 || r >= g.length || c >= g[0].length || g[r][c] == 0) return 0;
        int gold = g[r][c];
        g[r][c] = 0;
        int more = Math.max(Math.max(dfs(g, r + 1, c), dfs(g, r - 1, c)), Math.max(dfs(g, r, c + 1), dfs(g, r, c - 1)));
        g[r][c] = gold;
        return gold + more;
    }
}
