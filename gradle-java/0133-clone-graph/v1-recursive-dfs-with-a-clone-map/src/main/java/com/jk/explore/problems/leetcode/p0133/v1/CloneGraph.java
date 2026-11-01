package com.jk.explore.problems.leetcode.p0133.v1;

import java.util.*;

public class CloneGraph {

    /** Undirected graph node. */
    public static class Node {
        public int val;
        public List<Node> neighbors = new ArrayList<>();

        public Node(int val) { this.val = val; }
    }

    private final MyHashMap<Node, Node> copyOf = new MyHashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        Node existing = copyOf.get(node);
        if (existing != null) return existing;
        Node copy = new Node(node.val);
        copyOf.put(node, copy);
        for (Node nb : node.neighbors) copy.neighbors.add(cloneGraph(nb));
        return copy;
    }
}
