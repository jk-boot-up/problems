package com.jk.explore.problems.leetcode.p0061.v1;

import java.util.*;

public class RotateList {

    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;
        int n = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            n++;
        }
        tail.next = head;
        ListNode newTail = head;
        for (int i = 0; i < n - k % n - 1; i++) newTail = newTail.next;
        ListNode newHead = newTail.next;
        newTail.next = null;
        return newHead;
    }
}
