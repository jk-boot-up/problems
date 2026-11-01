package com.jk.explore.problems.leetcode.p0142.v1;

import java.util.*;

public class LinkedListCycleII {

    public ListNode detectCycle(ListNode head) {
        MyHashSet<ListNode> seen = new MyHashSet<>();
        for (ListNode n = head; n != null; n = n.next) {
            if (!seen.add(n)) return n;
        }
        return null;
    }
}
