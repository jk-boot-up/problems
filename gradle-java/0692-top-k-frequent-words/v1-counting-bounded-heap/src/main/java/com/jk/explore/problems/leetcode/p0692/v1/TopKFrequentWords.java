package com.jk.explore.problems.leetcode.p0692.v1;

import java.util.*;

public class TopKFrequentWords {

    public List<String> topKFrequent(String[] words, int k) {
        MyHashMap<String, Integer> count = new MyHashMap<>();
        for (String w : words) count.merge(w, 1, Integer::sum);
        PriorityQueue<String> heap = new PriorityQueue<>((a, b) -> {
            int ca = count.get(a), cb = count.get(b);
            return ca != cb ? Integer.compare(ca, cb) : b.compareTo(a);
        });
        for (String w : count.keys()) {
            heap.add(w);
            if (heap.size() > k) heap.poll();
        }
        LinkedList<String> out = new LinkedList<>();
        while (!heap.isEmpty()) out.addFirst(heap.poll());
        return out;
    }
}
