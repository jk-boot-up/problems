package com.jk.explore.problems.leetcode.p1318.v1;

import java.util.*;

public class MinimumFlips {

    public int minFlips(int a, int b, int c) {
        int flips = 0;
        for (int i = 0; i < 31; i++) {
            int x = a >> i & 1, y = b >> i & 1, z = c >> i & 1;
            if (z == 1) flips += (x | y) == 0 ? 1 : 0;
            else flips += x + y;
        }
        return flips;
    }
}
