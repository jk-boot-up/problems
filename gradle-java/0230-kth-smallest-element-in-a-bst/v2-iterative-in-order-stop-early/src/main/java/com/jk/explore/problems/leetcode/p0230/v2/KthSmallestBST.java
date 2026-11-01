package com.jk.explore.problems.leetcode.p0230.v2;

import java.util.*;

public class KthSmallestBST {

    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode n = root;
        while (true) {
            for (; n != null; n = n.left) stack.push(n);
            n = stack.pop();
            if (--k == 0) return n.val;
            n = n.right;
        }
    }
}
