package com.jk.explore.problems.leetcode.p0093.v1;

import java.util.*;

public class RestoreIPAddresses {

    public List<String> restoreIpAddresses(String s) {
        List<String> out = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(String s, int i, List<String> parts, List<String> out) {
        if (parts.size() == 4) {
            if (i == s.length()) out.add(String.join(".", parts));
            return;
        }
        for (int len = 1; len <= 3 && i + len <= s.length(); len++) {
            String part = s.substring(i, i + len);
            if ((part.length() > 1 && part.charAt(0) == '0') || Integer.parseInt(part) > 255) break;
            parts.add(part);
            backtrack(s, i + len, parts, out);
            parts.removeLast();
        }
    }
}
