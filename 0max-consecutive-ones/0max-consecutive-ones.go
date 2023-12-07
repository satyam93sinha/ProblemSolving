func findMaxConsecutiveOnes(nums []int) int {
    consecutive_ones := 0
    max_consecutive_ones := 0
    for _, num := range nums{
        if num == 1{
            consecutive_ones++
        } else{
            consecutive_ones = 0
        }
        max_consecutive_ones = max(consecutive_ones, max_consecutive_ones)
    }
    
    return max_consecutive_ones
}