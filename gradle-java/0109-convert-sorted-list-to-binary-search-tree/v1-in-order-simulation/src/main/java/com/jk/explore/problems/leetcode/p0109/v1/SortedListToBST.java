package com.jk.explore.problems.leetcode.p0109.v1;

import java.util.*;

public class SortedListToBST {

    private ListNode cur;

    public TreeNode sortedListToBST(ListNode head) {
        int n = 0;
        for (ListNode p = head; p != null; p = p.next) n++;
        cur = head;
        return build(0, n - 1);
    }

    private TreeNode build(int lo, int hi) {
        if (lo > hi) return null;
        int mid = (lo + hi) >>> 1;
        TreeNode left = build(lo, mid - 1);
        TreeNode root = new TreeNode(cur.val);
        cur = cur.next;
        root.left = left;
        root.right = build(mid + 1, hi);
        return root;
    }
}
