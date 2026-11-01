package com.jk.explore.problems.leetcode.p0735.v1;

import java.util.*;

public class AsteroidCollision {

    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (int a : asteroids) {
            boolean alive = true;
            while (alive && a < 0 && !stack.isEmpty() && stack.peek() > 0) {
                int top = stack.peek();
                if (top < -a) stack.pop();
                else {
                    alive = false;
                    if (top == -a) stack.pop();
                }
            }
            if (alive) stack.push(a);
        }
        int[] out = new int[stack.size()];
        for (int i = out.length - 1; i >= 0; i--) out[i] = stack.pop();
        return out;
    }
}
