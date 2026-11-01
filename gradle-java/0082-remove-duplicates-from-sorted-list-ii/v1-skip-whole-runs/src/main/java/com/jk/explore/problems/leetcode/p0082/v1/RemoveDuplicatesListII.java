package com.jk.explore.problems.leetcode.p0082.v1;

import java.util.*;

public class RemoveDuplicatesListII {

    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0, head), prev = dummy, cur = head;
        while (cur != null) {
            if (cur.next != null && cur.next.val == cur.val) {
                int dup = cur.val;
                while (cur != null && cur.val == dup) cur = cur.next;
                prev.next = cur;
            } else {
                prev = cur;
                cur = cur.next;
            }
        }
        return dummy.next;
    }
}
