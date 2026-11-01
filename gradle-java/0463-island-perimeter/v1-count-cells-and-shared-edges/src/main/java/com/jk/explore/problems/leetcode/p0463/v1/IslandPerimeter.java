package com.jk.explore.problems.leetcode.p0463.v1;

import java.util.*;

public class IslandPerimeter {

    public int islandPerimeter(int[][] grid) {
        int land = 0, shared = 0;
        for (int r = 0; r < grid.length; r++)
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] != 1) continue;
                land++;
                if (r > 0 && grid[r - 1][c] == 1) shared++;
                if (c > 0 && grid[r][c - 1] == 1) shared++;
            }
        return 4 * land - 2 * shared;
    }
}
