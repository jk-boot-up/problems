package com.jk.explore.problems.samples.kmp;

import java.util.Arrays;

public class KMPPatternSearcher {
    void KMPSearch(String pat, String txt)
    {
        int M = pat.length();
        int N = txt.length();

        // create lps[] that will hold the longest
        // prefix suffix values for pattern
        int lps[] = new int[M];
        int j = 0; // index for pat[]

        // Preprocess the pattern (calculate lps[]
        // array)
        computeLPSArray(pat, M, lps);

        int i = 0; // index for txt[]
        while (i < N) {
            if (pat.charAt(j) == txt.charAt(i)) {
                j++;
                i++;
            }
            if (j == M) {
                System.out.println("Found pattern "
                        + "at index " + (i - j));
                j = lps[j - 1];
            }

            // mismatch after j matches
            else if (i < N && pat.charAt(j) != txt.charAt(i)) {
                // Do not match lps[0..lps[j-1]] characters,
                // they will match anyway
                if (j != 0)
                    j = lps[j - 1];
                else
                    i = i + 1;
            }
        }
    }

    void computeLPSArray(String pat, int M, int lps[])
    {
        // length of the previous longest prefix suffix
        int len = 0;
        int i = 1;
        lps[0] = 0; // lps[0] is always 0

        // the loop calculates lps[i] for i = 1 to M-1
        while (i < M) {
            if (pat.charAt(i) == pat.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            }
            else // (pat[i] != pat[len])
            {
                // This is tricky. Consider the example.
                // AAACAAAA and i = 7. The idea is similar
                // to search step.
                if (len != 0) {
                    len = lps[len - 1];

                    // Also, note that we do not increment
                    // i here
                }
                else // if (len == 0)
                {
                    lps[i] = len;
                    i++;
                }
            }
        }
    }

    public static void main(String args[])
    {
        String txt = "ABABDABACDABABCABAB";
        String pat = "ABABCABAB";
        new KMPPatternSearcher().KMPSearch(pat, txt);
    }

    public int[] findLPSArray(String pattern, int m) {
        if(pattern == null) {
            return null;
        }
        int[] lps = new int[m];
        lps[0] = 0;
        int len = 0;
        int i = 1;
        while(i < m) {
            if(pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if(len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = len;
                    i++;
                }
            }
        }
        return lps;
    }

    public int[] findPatterns(String text, String pattern) {
        if(text == null || pattern == null || text.length() == 0 || pattern.length() == 0) {
            return null;
        }
        int n = text.length();
        int m = pattern.length();
        int[] lps = findLPSArray(pattern, m);
        int i = 0;
        int j = 0;
        int[] results = new int[n];
        int count = 0;
        while(i < n) {
            if(text.charAt(i) == pattern.charAt(j)) {
                i++;
                j++;
            }
            if(j == m) {
                System.out.println("Match found at index: "+(i-j));
                results[count++] = i - j;
                j = lps[j -1];
            } else if(i < n && text.charAt(i) != pattern.charAt(j)) {
                if(j != 0) {
                    j = lps[j-1];
                } else {
                    i ++;
                }
            }
        }
        results = Arrays.stream(results, 0, count).toArray();
        return results;
    }


}
