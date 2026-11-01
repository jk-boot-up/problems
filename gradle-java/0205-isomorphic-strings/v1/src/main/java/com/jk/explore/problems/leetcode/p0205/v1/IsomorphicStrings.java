package com.jk.explore.problems.leetcode.p0205.v1;

import java.util.*;

public class IsomorphicStrings {

    public boolean isIsomorphic(String s, String t) {
        int[] sToT = new int[256], tToS = new int[256];
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i), b = t.charAt(i);
            if (sToT[a] == 0 && tToS[b] == 0) {
                sToT[a] = b;
                tToS[b] = a;
            } else if (sToT[a] != b || tToS[b] != a) {
                return false;
            }
        }
        return true;
    }
}
