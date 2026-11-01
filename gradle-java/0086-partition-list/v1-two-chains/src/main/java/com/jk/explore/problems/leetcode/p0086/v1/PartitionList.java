package com.jk.explore.problems.leetcode.p0086.v1;

import java.util.*;

public class PartitionList {

    public ListNode partition(ListNode head, int x) {
        ListNode lessHead = new ListNode(0), restHead = new ListNode(0), less = lessHead, rest = restHead;
        for (ListNode n = head; n != null; n = n.next) {
            if (n.val < x) {
                less.next = n;
                less = n;
            } else {
                rest.next = n;
                rest = n;
            }
        }
        rest.next = null;
        less.next = restHead.next;
        return lessHead.next;
    }
}
