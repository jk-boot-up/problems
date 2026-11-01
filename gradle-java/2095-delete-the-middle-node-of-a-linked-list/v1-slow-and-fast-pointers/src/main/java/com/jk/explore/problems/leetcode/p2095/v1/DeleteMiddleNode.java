package com.jk.explore.problems.leetcode.p2095.v1;

import java.util.*;

public class DeleteMiddleNode {

    public ListNode deleteMiddle(ListNode head) {
        if (head.next == null) return null;
        ListNode slow = head, fast = head.next.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        slow.next = slow.next.next;
        return head;
    }
}
