package com.jk.explore.problems.leetcode.p0023.v2;

import java.util.*;

public class MergeKSortedLists {

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        ListNode[] a = lists.clone();
        for (int step = 1; step < a.length; step *= 2) {
            for (int i = 0; i + step < a.length; i += 2 * step) {
                a[i] = merge(a[i], a[i + step]);
            }
        }
        return a[0];
    }

    private static ListNode merge(ListNode x, ListNode y) {
        ListNode dummy = new ListNode(0), tail = dummy;
        while (x != null && y != null) {
            if (x.val <= y.val) { tail.next = x; x = x.next; } else { tail.next = y; y = y.next; }
            tail = tail.next;
        }
        tail.next = x != null ? x : y;
        return dummy.next;
    }
}
