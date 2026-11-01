package com.jk.explore.problems.leetcode.p0019.v1;

import java.util.*;

public class RemoveNthFromEnd {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 0;
        for (ListNode p = head; p != null; p = p.next) length++;
        ListNode dummy = new ListNode(0, head), prev = dummy;
        for (int i = 0; i < length - n; i++) prev = prev.next;
        prev.next = prev.next.next;
        return dummy.next;
    }
}
