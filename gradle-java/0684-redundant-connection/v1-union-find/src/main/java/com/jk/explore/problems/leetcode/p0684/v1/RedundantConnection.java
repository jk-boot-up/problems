package com.jk.explore.problems.leetcode.p0684.v1;

import java.util.*;

public class RedundantConnection {

    private int[] parent, size;

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        parent = new int[n + 1];
        size = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        for (int[] e : edges) {
            int a = find(e[0]), b = find(e[1]);
            if (a == b) return e;
            if (size[a] < size[b]) { int t = a; a = b; b = t; }
            parent[b] = a;
            size[a] += size[b];
        }
        return new int[0];
    }
}
