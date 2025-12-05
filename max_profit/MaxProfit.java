package max_profit;

public class MaxProfit {
    public static void main(String[] args) {
        int[] prices = {7,6,4,3,1};
        System.out.println("Maximum Profit: " + getMaxProfit(prices));
    }
    
    public static int getMaxProfit(int[] prices) {
        int minPrice = prices[0];
        int max_profit = 0;

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] <= minPrice) {
                minPrice = prices[i];
                continue;
            }
            int profit = prices[i] - minPrice;
            max_profit = Math.max(max_profit, profit);
        }
        return max_profit;
    }
}
