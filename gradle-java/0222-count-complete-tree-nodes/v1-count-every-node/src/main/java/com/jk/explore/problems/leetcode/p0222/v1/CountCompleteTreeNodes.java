package com.jk.explore.problems.leetcode.p0222.v1;

import java.util.*;

public class CountCompleteTreeNodes {

    public int countNodes(TreeNode root) {
        return root == null ? 0 : 1 + countNodes(root.left) + countNodes(root.right);
    }
}
