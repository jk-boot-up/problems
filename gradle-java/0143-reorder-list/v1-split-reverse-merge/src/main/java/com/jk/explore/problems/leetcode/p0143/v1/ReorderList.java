package com.jk.explore.problems.leetcode.p0143.v1;

import java.util.*;

public class ReorderList {

    public void reorderList(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode second = null, cur = slow.next;
        slow.next = null;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = second;
            second = cur;
            cur = next;
        }
        for (ListNode first = head; second != null; ) {
            ListNode n1 = first.next, n2 = second.next;
            first.next = second;
            second.next = n1;
            first = n1;
            second = n2;
        }
    }
}
