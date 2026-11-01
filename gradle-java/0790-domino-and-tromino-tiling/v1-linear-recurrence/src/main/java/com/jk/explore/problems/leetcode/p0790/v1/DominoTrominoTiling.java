package com.jk.explore.problems.leetcode.p0790.v1;

import java.util.*;

public class DominoTrominoTiling {

    public int numTilings(int n) {
        final long MOD = 1_000_000_007L;
        long[] f = new long[Math.max(3, n + 1)];
        f[0] = 1;
        f[1] = 1;
        f[2] = 2;
        for (int i = 3; i <= n; i++) f[i] = (2 * f[i - 1] + f[i - 3]) % MOD;
        return (int) f[n];
    }
}
