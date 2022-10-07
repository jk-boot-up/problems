import com.jk.explore.problems._1_LongestCommonPrefix;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

public class _1_LongestCommonPrefixTest {

    @Test
    public void getAllPrefixStrings() {
        _1_LongestCommonPrefix cut = new _1_LongestCommonPrefix();
        List<String> prefixes = cut.getAllPrefixStrings("abcd");
        List<String> expected = Arrays.asList("a", "ab", "abc", "abcd");
        Assertions.assertEquals(expected.size(), prefixes.size());
        Assertions.assertTrue(prefixes.containsAll(expected));
    }
}
