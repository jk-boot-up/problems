package com.jk.explore.problems.leetcode.p0779.v2;

import java.util.*;

public class KthSymbolInGrammar {

    public int kthGrammar(int n, int k) {
        return Integer.bitCount(k - 1) & 1;
    }
}
