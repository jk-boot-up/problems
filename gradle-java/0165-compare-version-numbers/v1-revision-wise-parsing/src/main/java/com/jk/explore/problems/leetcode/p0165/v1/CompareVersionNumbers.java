package com.jk.explore.problems.leetcode.p0165.v1;

import java.util.*;

public class CompareVersionNumbers {

    public int compareVersion(String version1, String version2) {
        int i = 0, j = 0;
        while (i < version1.length() || j < version2.length()) {
            int a = 0, b = 0;
            while (i < version1.length() && version1.charAt(i) != '.') a = a * 10 + (version1.charAt(i++) - '0');
            while (j < version2.length() && version2.charAt(j) != '.') b = b * 10 + (version2.charAt(j++) - '0');
            if (a != b) return a < b ? -1 : 1;
            i++;
            j++;
        }
        return 0;
    }
}
