package com.jk.explore.problems.leetcode.p1009.v1;

import java.util.*;

public class ComplementOfBase10 {

    public int bitwiseComplement(int n) {
        int mask = 1;
        while (mask < n) mask = (mask << 1) | 1;
        return n ^ mask;
    }
}
