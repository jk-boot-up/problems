package com.jk.explore.problems.leetcode.p0092.v1;

import java.util.*;

public class ReverseLinkedListII {

    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0, head), prev = dummy;
        for (int i = 1; i < left; i++) prev = prev.next;
        ListNode cur = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode move = cur.next;
            cur.next = move.next;
            move.next = prev.next;
            prev.next = move;
        }
        return dummy.next;
    }
}
