package com.jk.explore.problems.leetcode.p0547.v1;

import java.util.*;

public class NumberOfProvinces {

    private int[] parent;

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length, provinces = n;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    int a = find(i), b = find(j);
                    if (a != b) {
                        parent[a] = b;
                        provinces--;
                    }
                }
            }
        }
        return provinces;
    }
}
