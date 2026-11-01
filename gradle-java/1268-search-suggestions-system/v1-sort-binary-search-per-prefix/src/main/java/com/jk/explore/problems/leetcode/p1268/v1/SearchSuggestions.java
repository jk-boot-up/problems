package com.jk.explore.problems.leetcode.p1268.v1;

import java.util.*;

public class SearchSuggestions {

    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        String[] sorted = products.clone();
        Arrays.sort(sorted);
        List<List<String>> out = new ArrayList<>();
        for (int len = 1; len <= searchWord.length(); len++) {
            String prefix = searchWord.substring(0, len);
            int lo = 0, hi = sorted.length;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (sorted[mid].compareTo(prefix) < 0) lo = mid + 1; else hi = mid;
            }
            List<String> picks = new ArrayList<>();
            for (int i = lo; i < sorted.length && picks.size() < 3 && sorted[i].startsWith(prefix); i++) picks.add(sorted[i]);
            out.add(picks);
        }
        return out;
    }
}
