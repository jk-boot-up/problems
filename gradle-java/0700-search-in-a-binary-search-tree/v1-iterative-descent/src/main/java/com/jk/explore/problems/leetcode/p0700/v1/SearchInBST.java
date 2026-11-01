package com.jk.explore.problems.leetcode.p0700.v1;

import java.util.*;

public class SearchInBST {

    public TreeNode searchBST(TreeNode root, int val) {
        TreeNode n = root;
        while (n != null && n.val != val) n = val < n.val ? n.left : n.right;
        return n;
    }
}
