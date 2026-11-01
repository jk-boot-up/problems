package com.jk.explore.problems.leetcode.p0133.v2;

import java.util.*;

public class CloneGraph {

    /** Undirected graph node. */
    public static class Node {
        public int val;
        public List<Node> neighbors = new ArrayList<>();

        public Node(int val) { this.val = val; }
    }

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        MyHashMap<Node, Node> copyOf = new MyHashMap<>();
        copyOf.put(node, new Node(node.val));
        Deque<Node> queue = new ArrayDeque<>(List.of(node));
        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            for (Node nb : cur.neighbors) {
                if (!copyOf.containsKey(nb)) {
                    copyOf.put(nb, new Node(nb.val));
                    queue.add(nb);
                }
                copyOf.get(cur).neighbors.add(copyOf.get(nb));
            }
        }
        return copyOf.get(node);
    }
}
