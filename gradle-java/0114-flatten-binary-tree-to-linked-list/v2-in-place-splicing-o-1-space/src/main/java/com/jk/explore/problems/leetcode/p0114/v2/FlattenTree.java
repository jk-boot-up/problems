package com.jk.explore.problems.leetcode.p0114.v2;

import java.util.*;

public class FlattenTree {

    public void flatten(TreeNode root) {
        for (TreeNode cur = root; cur != null; cur = cur.right) {
            if (cur.left != null) {
                TreeNode rightmost = cur.left;
                while (rightmost.right != null) rightmost = rightmost.right;
                rightmost.right = cur.right;
                cur.right = cur.left;
                cur.left = null;
            }
        }
    }
}
