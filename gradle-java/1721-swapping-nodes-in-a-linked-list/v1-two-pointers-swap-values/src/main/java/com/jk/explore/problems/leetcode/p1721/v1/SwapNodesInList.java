package com.jk.explore.problems.leetcode.p1721.v1;

import java.util.*;

public class SwapNodesInList {

    public ListNode swapNodes(ListNode head, int k) {
        ListNode fast = head;
        for (int i = 1; i < k; i++) fast = fast.next;
        ListNode first = fast, slow = head;
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        int t = first.val;
        first.val = slow.val;
        slow.val = t;
        return head;
    }
}
