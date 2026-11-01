package com.jk.explore.problems.leetcode.p0206.v2;

import java.util.*;

public class ReverseLinkedList {

    public ListNode reverseList(ListNode head) {
        ListNode prev = null, cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
}
