package com.jk.explore.problems.leetcode.p0141.v1;

import java.util.*;

public class LinkedListCycle {

    public boolean hasCycle(ListNode head) {
        MyHashSet<ListNode> seen = new MyHashSet<>();
        for (ListNode n = head; n != null; n = n.next) {
            if (!seen.add(n)) return true;
        }
        return false;
    }
}
