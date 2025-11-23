import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Consecutive{

    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 1, 1, 1, 1, 3, 4, 1, 2, 1, 1, 1, 2));
        System.out.println(maxConsecutiveOnes(nums));
    }
    
    public static int maxConsecutiveOnes(List<Integer> nums ) {
        int longest = 0, count = 0;
        for (Integer num : nums) {
            if (num != 1) {
                count = 0;
                continue;
            }
            count += 1;
            longest = Math.max(longest, count);
        }
        return longest;
    }
}