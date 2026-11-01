package com.jk.explore.problems.leetcode.p1971.v1;

import java.util.*;

public class FindIfPathExists {

    private int[] parent, size;

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        for (int[] e : edges) union(e[0], e[1]);
        return find(source) == find(destination);
    }

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return;
        if (size[ra] < size[rb]) {
            int t = ra;
            ra = rb;
            rb = t;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
    }
}
