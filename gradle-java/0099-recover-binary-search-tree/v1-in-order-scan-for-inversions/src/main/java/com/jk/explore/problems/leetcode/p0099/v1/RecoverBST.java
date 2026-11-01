package com.jk.explore.problems.leetcode.p0099.v1;

import java.util.*;

public class RecoverBST {

    public void recoverTree(TreeNode root) {
        TreeNode first = null, second = null, prev = null, cur = root;
        Deque<TreeNode> stack = new ArrayDeque<>();
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            if (prev != null && cur.val < prev.val) {
                if (first == null) first = prev;
                second = cur;
            }
            prev = cur;
            cur = cur.right;
        }
        int t = first.val;
        first.val = second.val;
        second.val = t;
    }
}
