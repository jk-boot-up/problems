package com.jk.explore.problems.leetcode.p0234.v1;

import java.util.*;

public class PalindromeLinkedList {

    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null;
        while (slow != null) {
            ListNode next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }
        for (ListNode a = head, b = prev; b != null; a = a.next, b = b.next) {
            if (a.val != b.val) return false;
        }
        return true;
    }
}
