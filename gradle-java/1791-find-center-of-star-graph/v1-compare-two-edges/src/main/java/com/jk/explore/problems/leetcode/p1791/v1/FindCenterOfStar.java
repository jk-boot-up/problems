package com.jk.explore.problems.leetcode.p1791.v1;

import java.util.*;

public class FindCenterOfStar {

    public int findCenter(int[][] edges) {
        int a = edges[0][0], b = edges[0][1];
        return a == edges[1][0] || a == edges[1][1] ? a : b;
    }
}
