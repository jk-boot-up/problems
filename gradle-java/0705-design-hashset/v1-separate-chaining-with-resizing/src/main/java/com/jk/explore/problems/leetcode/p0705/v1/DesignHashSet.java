package com.jk.explore.problems.leetcode.p0705.v1;

import java.util.*;

public class DesignHashSet {

    private static final class Node {
        final int key;
        Node next;

        Node(int key, Node next) {
            this.key = key;
            this.next = next;
        }
    }

    private Node[] buckets = new Node[16];
    private int size;

    private int index(int key, int capacity) {
        int h = Integer.hashCode(key);
        return (h ^ (h >>> 16)) & (capacity - 1);
    }

    public void add(int key) {
        if (contains(key)) return;
        int i = index(key, buckets.length);
        buckets[i] = new Node(key, buckets[i]);
        if (++size > buckets.length * 3 / 4) resize();
    }

    public boolean contains(int key) {
        for (Node n = buckets[index(key, buckets.length)]; n != null; n = n.next) {
            if (n.key == key) return true;
        }
        return false;
    }

    public void remove(int key) {
        int i = index(key, buckets.length);
        for (Node prev = null, n = buckets[i]; n != null; prev = n, n = n.next) {
            if (n.key == key) {
                if (prev == null) buckets[i] = n.next; else prev.next = n.next;
                size--;
                return;
            }
        }
    }

    private void resize() {
        Node[] old = buckets;
        buckets = new Node[old.length * 2];
        for (Node head : old) {
            for (Node n = head; n != null; ) {
                Node next = n.next;
                int i = index(n.key, buckets.length);
                n.next = buckets[i];
                buckets[i] = n;
                n = next;
            }
        }
    }
}
