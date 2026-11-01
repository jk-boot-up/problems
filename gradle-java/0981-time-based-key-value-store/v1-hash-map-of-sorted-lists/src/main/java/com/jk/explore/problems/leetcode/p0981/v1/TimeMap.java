package com.jk.explore.problems.leetcode.p0981.v1;

import java.util.*;

public class TimeMap {

    private record Entry(int time, String value) { }

    private final MyHashMap<String, List<Entry>> map = new MyHashMap<>();

    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(new Entry(timestamp, value));
    }

    public String get(String key, int timestamp) {
        List<Entry> list = map.get(key);
        if (list == null) return "";
        int lo = 0, hi = list.size() - 1, found = -1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid).time() <= timestamp) {
                found = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return found < 0 ? "" : list.get(found).value();
    }
}
