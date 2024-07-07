class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int min = INT_MAX;
        int maxprofit = 0;
        int profit = 0;
        for(int i = 0; i < n; i++) {
            if(min > prices[i]) {
                min = prices[i];
            }
            profit = prices[i] - min;
            if(profit > maxprofit) {
                maxprofit = profit;
            }
        }
        return maxprofit;
    }
};