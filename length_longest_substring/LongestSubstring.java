import java.util.*;

public class LongestSubstring {
    
    public static int lenghtOfLongestSubstring(String s) {
        int n = s.length();

        int longest = 0, left = 0;
        Set<Character> set = new HashSet<>();

        for(int right = 0; right < n; right++){
            // shrink the window from the left until we remove the duplicate character
            while(set.contains(s.charAt(right))){
                set.remove(s.charAt(left));
                left += 1 ;
            }

            set.add(s.charAt(right));
            longest = Math.max(longest, right - left + 1);
        }
        return longest;
    }
}
