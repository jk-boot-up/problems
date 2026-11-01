package com.jk.explore.problems.leetcode.p0237.v1;

import java.util.*;

public class DeleteNode {

    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
