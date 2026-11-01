package com.jk.explore.problems.leetcode.p0148.v2;

import java.util.*;

public class SortList {

    public ListNode sortList(ListNode head) {
        int length = 0;
        for (ListNode p = head; p != null; p = p.next) length++;
        ListNode dummy = new ListNode(0, head);
        for (int size = 1; size < length; size <<= 1) {
            ListNode tail = dummy, cur = dummy.next;
            while (cur != null) {
                ListNode left = cur;
                ListNode right = split(left, size);
                cur = split(right, size);
                tail = merge(left, right, tail);
            }
        }
        return dummy.next;
    }

    /** Cuts the list after size nodes and returns the head of the rest. */
    private static ListNode split(ListNode head, int size) {
        for (int i = 1; head != null && i < size; i++) head = head.next;
        if (head == null) return null;
        ListNode rest = head.next;
        head.next = null;
        return rest;
    }

    /** Merges a and b after tail and returns the new tail. */
    private static ListNode merge(ListNode a, ListNode b, ListNode tail) {
        while (a != null && b != null) {
            if (a.val <= b.val) { tail.next = a; a = a.next; } else { tail.next = b; b = b.next; }
            tail = tail.next;
        }
        tail.next = a != null ? a : b;
        while (tail.next != null) tail = tail.next;
        return tail;
    }
}
