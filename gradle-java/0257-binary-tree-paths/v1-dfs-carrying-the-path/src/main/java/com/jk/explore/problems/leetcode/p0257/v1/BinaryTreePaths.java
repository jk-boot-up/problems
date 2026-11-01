package com.jk.explore.problems.leetcode.p0257.v1;

import java.util.*;

public class BinaryTreePaths {

    public List<String> binaryTreePaths(TreeNode root) {
        List<String> out = new ArrayList<>();
        dfs(root, new StringBuilder(), out);
        return out;
    }

    private void dfs(TreeNode node, StringBuilder path, List<String> out) {
        if (node == null) return;
        int mark = path.length();
        if (mark > 0) path.append("->");
        path.append(node.val);
        if (node.left == null && node.right == null) out.add(path.toString());
        else {
            dfs(node.left, path, out);
            dfs(node.right, path, out);
        }
        path.setLength(mark);
    }
}
