package com.jk.explore.problems.leetcode.p0382.v2;

import java.util.*;

public class LinkedListRandomNode {

    private final ListNode head;
    private final Random rnd;

    public LinkedListRandomNode(ListNode head) {
        this(head, new Random());
    }

    LinkedListRandomNode(ListNode head, Random rnd) {
        this.head = head;
        this.rnd = rnd;
    }

    public int getRandom() {
        int pick = head.val, i = 1;
        for (ListNode n = head.next; n != null; n = n.next) {
            i++;
            if (rnd.nextInt(i) == 0) pick = n.val;
        }
        return pick;
    }
}
