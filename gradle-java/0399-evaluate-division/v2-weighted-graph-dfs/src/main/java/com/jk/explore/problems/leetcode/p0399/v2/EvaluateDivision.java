package com.jk.explore.problems.leetcode.p0399.v2;

import java.util.*;

public class EvaluateDivision {

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        MyHashMap<String, MyHashMap<String, Double>> graph = new MyHashMap<>();
        for (int i = 0; i < values.length; i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            graph.computeIfAbsent(a, k -> new MyHashMap<>()).put(b, values[i]);
            graph.computeIfAbsent(b, k -> new MyHashMap<>()).put(a, 1.0 / values[i]);
        }
        double[] out = new double[queries.size()];
        for (int i = 0; i < out.length; i++) {
            String c = queries.get(i).get(0), d = queries.get(i).get(1);
            out[i] = graph.containsKey(c) && graph.containsKey(d) ? dfs(graph, c, d, new MyHashSet<>()) : -1.0;
        }
        return out;
    }

    private double dfs(MyHashMap<String, MyHashMap<String, Double>> graph, String cur, String target, MyHashSet<String> seen) {
        if (cur.equals(target)) return 1.0;
        seen.add(cur);
        for (MyHashMap.Entry<String, Double> e : graph.get(cur).entries()) {
            if (seen.contains(e.getKey())) continue;
            double rest = dfs(graph, e.getKey(), target, seen);
            if (rest >= 0) return e.getValue() * rest;
        }
        return -1.0;
    }
}
