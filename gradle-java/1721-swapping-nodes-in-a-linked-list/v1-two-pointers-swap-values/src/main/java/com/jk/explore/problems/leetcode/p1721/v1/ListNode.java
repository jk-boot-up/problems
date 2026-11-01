package com.jk.explore.problems.leetcode.p1721.v1;

import java.util.*;

/** Singly linked list node used by the LeetCode list problems. */
public class ListNode {
    public int val;
    public ListNode next;

    public ListNode(int val) { this.val = val; }

    public ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    /** Builds a list from the given values and returns its head (null when empty). */
    public static ListNode of(int... values) {
        ListNode dummy = new ListNode(0), tail = dummy;
        for (int v : values) { tail.next = new ListNode(v); tail = tail.next; }
        return dummy.next;
    }

    /** Converts the list starting at head to an int array. */
    public static int[] toArray(ListNode head) {
        List<Integer> out = new ArrayList<>();
        for (ListNode n = head; n != null; n = n.next) out.add(n.val);
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
}
