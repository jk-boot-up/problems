package com.jk.explore.problems.leetcode.p2130.v1;

import java.util.*;

public class MaximumTwinSum {

    public int pairSum(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null;
        while (slow != null) {
            ListNode next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }
        int best = 0;
        for (ListNode a = head, b = prev; b != null; a = a.next, b = b.next) best = Math.max(best, a.val + b.val);
        return best;
    }
}
