package com.jk.explore.problems.leetcode.p0138.v1;

import java.util.*;

public class CopyRandomList {

    /** List node with an extra random pointer. */
    public static class Node {
        public int val;
        public Node next;
        public Node random;

        public Node(int val) { this.val = val; }
    }

    public Node copyRandomList(Node head) {
        MyHashMap<Node, Node> copyOf = new MyHashMap<>();
        for (Node n = head; n != null; n = n.next) copyOf.put(n, new Node(n.val));
        for (Node n = head; n != null; n = n.next) {
            Node c = copyOf.get(n);
            c.next = copyOf.get(n.next);
            c.random = copyOf.get(n.random);
        }
        return copyOf.get(head);
    }
}
