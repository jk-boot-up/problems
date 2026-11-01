package com.jk.explore.problems.leetcode.p0863.v1;

import java.util.*;

public class DistanceK {

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        MyHashMap<TreeNode, TreeNode> parent = new MyHashMap<>();
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            for (TreeNode c : new TreeNode[]{n.left, n.right})
                if (c != null) {
                    parent.put(c, n);
                    stack.push(c);
                }
        }
        MyHashSet<TreeNode> seen = new MyHashSet<>();
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(target));
        seen.add(target);
        for (int d = 0; d < k && !queue.isEmpty(); d++) {
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                for (TreeNode m : new TreeNode[]{n.left, n.right, parent.get(n)})
                    if (m != null && seen.add(m)) queue.add(m);
            }
        }
        List<Integer> out = new ArrayList<>();
        for (TreeNode n : queue) out.add(n.val);
        return out;
    }
}
