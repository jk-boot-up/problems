package com.jk.explore.problems.leetcode.p1431.v1;

import java.util.*;

public class KidsWithCandies {

    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        for (int c : candies) max = Math.max(max, c);
        List<Boolean> out = new ArrayList<>();
        for (int c : candies) out.add(c + extraCandies >= max);
        return out;
    }
}
