package com.jk.explore.problems.leetcode.p0146.v1;

import java.util.*;

public class LRUCache {

    private static final class Node {
        int key, value;
        Node prev, next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final int capacity;
    private final MyHashMap<Integer, Node> nodes = new MyHashMap<>();
    private final Node head = new Node(0, 0), tail = new Node(0, 0); // sentinels

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node n = nodes.get(key);
        if (n == null) return -1;
        unlink(n);
        addFront(n);
        return n.value;
    }

    public void put(int key, int value) {
        Node n = nodes.get(key);
        if (n != null) {
            n.value = value;
            unlink(n);
            addFront(n);
            return;
        }
        n = new Node(key, value);
        nodes.put(key, n);
        addFront(n);
        if (nodes.size() > capacity) {
            Node lru = tail.prev;
            unlink(lru);
            nodes.remove(lru.key);
        }
    }

    private void unlink(Node n) {
        n.prev.next = n.next;
        n.next.prev = n.prev;
    }

    private void addFront(Node n) {
        n.next = head.next;
        n.prev = head;
        head.next.prev = n;
        head.next = n;
    }
}
