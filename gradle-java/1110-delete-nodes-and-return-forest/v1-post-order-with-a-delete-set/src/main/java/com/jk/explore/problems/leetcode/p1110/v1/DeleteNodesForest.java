package com.jk.explore.problems.leetcode.p1110.v1;

import java.util.*;

public class DeleteNodesForest {

    public List<TreeNode> delNodes(TreeNode root, int[] toDelete) {
        MyHashSet<Integer> del = new MyHashSet<>();
        for (int v : toDelete) del.add(v);
        List<TreeNode> roots = new ArrayList<>();
        walk(root, true, del, roots);
        return roots;
    }

    private TreeNode walk(TreeNode node, boolean parentGone, MyHashSet<Integer> del, List<TreeNode> roots) {
        if (node == null) return null;
        boolean gone = del.contains(node.val);
        if (parentGone && !gone) roots.add(node);
        node.left = walk(node.left, gone, del, roots);
        node.right = walk(node.right, gone, del, roots);
        return gone ? null : node;
    }
}
