package com.jk.explore.problems.leetcode.p0142.v2;

import java.util.*;

public class LinkedListCycleII {

    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                for (ListNode p = head; ; p = p.next, slow = slow.next) {
                    if (p == slow) return p;
                }
            }
        }
        return null;
    }
}
