package com.jk.explore.problems.leetcode.p0147.v1;

import java.util.*;

public class InsertionSortList {

    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(0), prev = dummy;
        for (ListNode cur = head; cur != null; ) {
            ListNode next = cur.next;
            if (prev.val >= cur.val || prev == dummy) prev = dummy;
            while (prev.next != null && prev.next.val < cur.val) prev = prev.next;
            cur.next = prev.next;
            prev.next = cur;
            cur = next;
        }
        return dummy.next;
    }
}
