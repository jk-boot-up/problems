package com.jk.explore.problems.leetcode.p0881.v1;

import java.util.*;

public class BoatsToSavePeople {

    public int numRescueBoats(int[] people, int limit) {
        int[] p = people.clone();
        Arrays.sort(p);
        int boats = 0;
        for (int l = 0, r = p.length - 1; l <= r; r--) {
            if (p[l] + p[r] <= limit) l++;
            boats++;
        }
        return boats;
    }
}
