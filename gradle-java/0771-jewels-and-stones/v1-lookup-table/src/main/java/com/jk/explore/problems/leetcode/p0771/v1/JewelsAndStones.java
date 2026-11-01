package com.jk.explore.problems.leetcode.p0771.v1;

import java.util.*;

public class JewelsAndStones {

    public int numJewelsInStones(String jewels, String stones) {
        boolean[] isJewel = new boolean[128];
        for (char c : jewels.toCharArray()) isJewel[c] = true;
        int count = 0;
        for (char c : stones.toCharArray()) if (isJewel[c]) count++;
        return count;
    }
}
