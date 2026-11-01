package com.jk.explore.problems.leetcode.p0332.v1;

import java.util.*;

public class ReconstructItinerary {

    public List<String> findItinerary(List<List<String>> tickets) {
        MyHashMap<String, PriorityQueue<String>> graph = new MyHashMap<>();
        for (List<String> t : tickets) graph.computeIfAbsent(t.get(0), k -> new PriorityQueue<>()).add(t.get(1));
        LinkedList<String> route = new LinkedList<>();
        Deque<String> stack = new ArrayDeque<>(List.of("JFK"));
        while (!stack.isEmpty()) {
            PriorityQueue<String> next = graph.get(stack.peek());
            if (next != null && !next.isEmpty()) {
                stack.push(next.poll());
            } else {
                route.addFirst(stack.pop());
            }
        }
        return route;
    }
}
