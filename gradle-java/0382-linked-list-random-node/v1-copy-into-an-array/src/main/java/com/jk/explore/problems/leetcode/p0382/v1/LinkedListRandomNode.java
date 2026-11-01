package com.jk.explore.problems.leetcode.p0382.v1;

import java.util.*;

public class LinkedListRandomNode {

    private final List<Integer> values = new ArrayList<>();
    private final Random rnd;

    public LinkedListRandomNode(ListNode head) {
        this(head, new Random());
    }

    LinkedListRandomNode(ListNode head, Random rnd) {
        for (ListNode n = head; n != null; n = n.next) values.add(n.val);
        this.rnd = rnd;
    }

    public int getRandom() {
        return values.get(rnd.nextInt(values.size()));
    }
}
