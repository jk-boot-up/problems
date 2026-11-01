package com.jk.explore.problems.leetcode.p1396.v1;

import java.util.*;

public class UndergroundSystem {

    private record Trip(String station, int time) {}

    private final MyHashMap<Integer, Trip> open = new MyHashMap<>();
    private final MyHashMap<String, long[]> stats = new MyHashMap<>();

    public void checkIn(int id, String stationName, int t) {
        open.put(id, new Trip(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        Trip trip = open.remove(id);
        long[] s = stats.computeIfAbsent(trip.station() + "," + stationName, k -> new long[2]);
        s[0] += t - trip.time();
        s[1]++;
    }

    public double getAverageTime(String startStation, String endStation) {
        long[] s = stats.get(startStation + "," + endStation);
        return (double) s[0] / s[1];
    }
}
