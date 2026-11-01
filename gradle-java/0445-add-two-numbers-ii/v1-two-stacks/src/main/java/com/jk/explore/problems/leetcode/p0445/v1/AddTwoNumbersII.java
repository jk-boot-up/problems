package com.jk.explore.problems.leetcode.p0445.v1;

import java.util.*;

public class AddTwoNumbersII {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Deque<Integer> a = new ArrayDeque<>(), b = new ArrayDeque<>();
        for (ListNode n = l1; n != null; n = n.next) a.push(n.val);
        for (ListNode n = l2; n != null; n = n.next) b.push(n.val);
        ListNode head = null;
        int carry = 0;
        while (!a.isEmpty() || !b.isEmpty() || carry > 0) {
            int sum = carry + (a.isEmpty() ? 0 : a.pop()) + (b.isEmpty() ? 0 : b.pop());
            head = new ListNode(sum % 10, head);
            carry = sum / 10;
        }
        return head;
    }
}
