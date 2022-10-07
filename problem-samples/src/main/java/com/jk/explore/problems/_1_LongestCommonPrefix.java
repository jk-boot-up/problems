package com.jk.explore.problems;

import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class _1_LongestCommonPrefix {

    public String lcp(String[] strings) {
        if (strings == null || strings.length == 0 || strings.length == 1) {
            return null;
        }
        for(String string : strings) {

        }

        return null;

    }

    public List<String> getAllPrefixStrings(String string) {
        if(string == null || string.length() == 0) {
            return Collections.emptyList();
        }
        return IntStream.range(0, string.length()).mapToObj(i->string.substring(0, i+1)).collect(Collectors.toList());
    }

}
