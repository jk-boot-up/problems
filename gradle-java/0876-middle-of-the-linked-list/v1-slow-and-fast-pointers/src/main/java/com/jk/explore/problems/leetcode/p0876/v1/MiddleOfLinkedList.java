package com.jk.explore.problems.leetcode.p0876.v1;

import java.util.*;

public class MiddleOfLinkedList {

    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
