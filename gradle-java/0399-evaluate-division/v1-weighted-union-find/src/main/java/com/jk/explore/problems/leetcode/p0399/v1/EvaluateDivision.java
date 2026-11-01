package com.jk.explore.problems.leetcode.p0399.v1;

import java.util.*;

public class EvaluateDivision {

    private final MyHashMap<String, String> parent = new MyHashMap<>();
    private final MyHashMap<String, Double> weight = new MyHashMap<>(); // x / parent(x)

    private String find(String x) {
        String p = parent.get(x);
        if (!p.equals(x)) {
            String root = find(p);
            weight.put(x, weight.get(x) * weight.get(p));
            parent.put(x, root);
        }
        return parent.get(x);
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        for (int i = 0; i < values.length; i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            for (String v : List.of(a, b)) {
                if (!parent.containsKey(v)) { parent.put(v, v); weight.put(v, 1.0); }
            }
            String ra = find(a), rb = find(b);
            if (!ra.equals(rb)) {
                parent.put(ra, rb);
                weight.put(ra, values[i] * weight.get(b) / weight.get(a));
            }
        }
        double[] out = new double[queries.size()];
        for (int i = 0; i < out.length; i++) {
            String c = queries.get(i).get(0), d = queries.get(i).get(1);
            if (!parent.containsKey(c) || !parent.containsKey(d) || !find(c).equals(find(d))) out[i] = -1.0;
            else out[i] = weight.get(c) / weight.get(d);
        }
        return out;
    }
}
