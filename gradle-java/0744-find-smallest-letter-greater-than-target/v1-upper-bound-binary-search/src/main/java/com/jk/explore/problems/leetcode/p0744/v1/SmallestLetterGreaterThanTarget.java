package com.jk.explore.problems.leetcode.p0744.v1;

import java.util.*;

public class SmallestLetterGreaterThanTarget {

    public char nextGreatestLetter(char[] letters, char target) {
        int lo = 0, hi = letters.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (letters[mid] <= target) lo = mid + 1; else hi = mid;
        }
        return letters[lo % letters.length];
    }
}
