func sortedSquares(nums []int) []int {
    result := make([] int, len(nums))
    
    left, right := 0, len(nums)-1
    end := len(nums)-1
    for left <= right{
        left_square := nums[left] * nums[left]
        right_square := nums[right] * nums[right]
        if left_square <= right_square{
            result[end] = right_square
            end -= 1
            right -= 1
        } else{
            result[end] = left_square
            end -= 1
            left += 1
        }
    }
    
    return result
    
}