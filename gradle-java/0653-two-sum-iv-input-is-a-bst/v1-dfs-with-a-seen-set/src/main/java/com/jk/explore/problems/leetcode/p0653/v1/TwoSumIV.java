package com.jk.explore.problems.leetcode.p0653.v1;

import java.util.*;

public class TwoSumIV {

    public boolean findTarget(TreeNode root, int k) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (seen.contains(k - n.val)) return true;
            seen.add(n.val);
            if (n.left != null) stack.push(n.left);
            if (n.right != null) stack.push(n.right);
        }
        return false;
    }
}
