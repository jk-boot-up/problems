package com.jk.explore.problems.leetcode.p0297.v1;

import java.util.*;

public class Codec {

    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode marker = new TreeNode(0); // stands for null on the stack
        stack.push(root == null ? marker : root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (!sb.isEmpty()) sb.append(',');
            if (n == marker) {
                sb.append('#');
                continue;
            }
            sb.append(n.val);
            stack.push(n.right == null ? marker : n.right);
            stack.push(n.left == null ? marker : n.left);
        }
        return sb.toString();
    }

    public TreeNode deserialize(String data) {
        Iterator<String> it = Arrays.asList(data.split(",")).iterator();
        return build(it);
    }

    private TreeNode build(Iterator<String> it) {
        String token = it.next();
        if (token.equals("#")) return null;
        TreeNode n = new TreeNode(Integer.parseInt(token));
        n.left = build(it);
        n.right = build(it);
        return n;
    }
}
