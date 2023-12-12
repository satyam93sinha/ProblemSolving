func replaceElements(arr []int) []int {
    max_to_right := -1
    index := len(arr)-1
    for index > -1{
        arr[index], max_to_right = max_to_right, max(arr[index], max_to_right)
        index--
    }
    
    return arr
}

func max(first_num, second_num int) int{
    if first_num > second_num{
        return first_num
    }
    
    return second_num
}