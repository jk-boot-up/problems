package com.jk.explore.problems.leetcode.p1305.v1;

import java.util.*;

public class AllElementsTwoBST {

    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> a = inorder(root1), b = inorder(root2), out = new ArrayList<>(a.size() + b.size());
        int i = 0, j = 0;
        while (i < a.size() || j < b.size()) {
            if (j == b.size() || (i < a.size() && a.get(i) <= b.get(j))) out.add(a.get(i++));
            else out.add(b.get(j++));
        }
        return out;
    }

    private List<Integer> inorder(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        for (TreeNode cur = root; cur != null || !stack.isEmpty(); ) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            out.add(cur.val);
            cur = cur.right;
        }
        return out;
    }
}
