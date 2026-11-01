package com.jk.explore.problems.leetcode.p0455.v1;

import java.util.*;

public class AssignCookies {

    public int findContentChildren(int[] g, int[] s) {
        int[] greed = g.clone(), size = s.clone();
        Arrays.sort(greed);
        Arrays.sort(size);
        int child = 0;
        for (int j = 0; j < size.length && child < greed.length; j++) if (size[j] >= greed[child]) child++;
        return child;
    }
}
