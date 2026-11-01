package com.jk.explore.problems.leetcode.p0138.v2;

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
        for (Node n = head; n != null; n = n.next.next) {
            Node copy = new Node(n.val);
            copy.next = n.next;
            n.next = copy;
        }
        for (Node n = head; n != null; n = n.next.next) {
            n.next.random = n.random == null ? null : n.random.next;
        }
        Node dummy = new Node(0), tail = dummy;
        for (Node n = head; n != null; n = n.next) {
            tail.next = n.next;
            tail = tail.next;
            n.next = tail.next;
        }
        return dummy.next;
    }
}
