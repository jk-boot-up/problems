package com.jk.explore.problems.leetcode.p0299.v1;

import java.util.*;

public class BullsAndCows {

    public String getHint(String secret, String guess) {
        int bulls = 0, cows = 0;
        int[] tally = new int[10];
        for (int i = 0; i < secret.length(); i++) {
            int s = secret.charAt(i) - '0', g = guess.charAt(i) - '0';
            if (s == g) {
                bulls++;
                continue;
            }
            if (tally[s]++ < 0) cows++;
            if (tally[g]-- > 0) cows++;
        }
        return bulls + "A" + cows + "B";
    }
}
