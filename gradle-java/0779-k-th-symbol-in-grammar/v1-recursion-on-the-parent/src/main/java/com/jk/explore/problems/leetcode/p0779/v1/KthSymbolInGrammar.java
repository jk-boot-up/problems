package com.jk.explore.problems.leetcode.p0779.v1;

import java.util.*;

public class KthSymbolInGrammar {

    public int kthGrammar(int n, int k) {
        if (n == 1) return 0;
        int parent = kthGrammar(n - 1, (k + 1) / 2);
        return k % 2 == 1 ? parent : 1 - parent;
    }
}
