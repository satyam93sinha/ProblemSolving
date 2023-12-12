func sortArrayByParity(nums []int) []int {
    left, right := 0, len(nums)-1
    for left < right{
        // left num is odd
        if nums[left] % 2 == 1{
            // right is even
            if nums[right] % 2 == 0{
                nums[left], nums[right] = nums[right], nums[left]
                left++
                right--
            } else{
                right--
            }
        } else {  // left num is even
            left++
        }
    }
    return nums
}