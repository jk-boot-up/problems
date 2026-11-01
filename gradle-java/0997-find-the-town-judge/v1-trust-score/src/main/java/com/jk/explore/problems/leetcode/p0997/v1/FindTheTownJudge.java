package com.jk.explore.problems.leetcode.p0997.v1;

import java.util.*;

public class FindTheTownJudge {

    public int findJudge(int n, int[][] trust) {
        int[] score = new int[n + 1];
        for (int[] t : trust) {
            score[t[0]]--;
            score[t[1]]++;
        }
        for (int p = 1; p <= n; p++) {
            if (score[p] == n - 1) return p;
        }
        return -1;
    }
}
