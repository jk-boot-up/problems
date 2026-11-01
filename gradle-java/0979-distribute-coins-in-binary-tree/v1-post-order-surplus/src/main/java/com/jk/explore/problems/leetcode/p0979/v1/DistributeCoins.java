package com.jk.explore.problems.leetcode.p0979.v1;

import java.util.*;

public class DistributeCoins {

    private int moves;

    public int distributeCoins(TreeNode root) {
        moves = 0;
        surplus(root);
        return moves;
    }

    private int surplus(TreeNode node) {
        if (node == null) return 0;
        int l = surplus(node.left), r = surplus(node.right);
        moves += Math.abs(l) + Math.abs(r);
        return node.val - 1 + l + r;
    }
}
