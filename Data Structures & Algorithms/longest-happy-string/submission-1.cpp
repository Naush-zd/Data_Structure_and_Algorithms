class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        string res;
        priority_queue<pair<int, char>> maxHeap;
        
        if (a > 0) maxHeap.push({a, 'a'});
        if (b > 0) maxHeap.push({b, 'b'});
        if (c > 0) maxHeap.push({c, 'c'});
        
        while (!maxHeap.empty()) {
            auto [count, ch] = maxHeap.top();
            maxHeap.pop();
            
            // Check if adding 'ch' would create three consecutive identical characters
            if (res.size() > 1 && res[res.size() - 1] == ch && res[res.size() - 2] == ch) {
                if (maxHeap.empty()) break; // No other character available to break the streak
                
                auto [cnt, ch2] = maxHeap.top();
                maxHeap.pop();
                
                res += ch2;
                cnt--; // Fix 1: Decrement cnt, not ch2
                
                if (cnt > 0) maxHeap.push({cnt, ch2});
                maxHeap.push({count, ch}); // Push the original character back unchanged
            } else { // Fix 2: Belongs to the outer 'if'
                res += ch;
                count--;
                if (count > 0) maxHeap.push({count, ch}); // Fix 3: Check count > 0, not ch > 0
            }
        }
        
        return res;
    }
};
