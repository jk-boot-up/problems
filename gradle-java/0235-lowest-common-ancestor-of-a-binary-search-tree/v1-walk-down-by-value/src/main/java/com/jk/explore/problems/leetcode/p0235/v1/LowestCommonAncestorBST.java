package com.jk.explore.problems.leetcode.p0235.v1;

import java.util.*;

public class LowestCommonAncestorBST {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode n = root;
        while (true) {
            if (p.val < n.val && q.val < n.val) n = n.left;
            else if (p.val > n.val && q.val > n.val) n = n.right;
            else return n;
        }
    }
}
