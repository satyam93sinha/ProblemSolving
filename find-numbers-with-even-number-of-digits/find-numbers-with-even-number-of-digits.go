func findNumbers(nums []int) int {
    even_no_digits := 0
    for _, num := range nums{
        count_digits := 0
        
        for num != 0{
            num /= 10
            count_digits++
        }
        
        if count_digits % 2 == 0{
            even_no_digits++
        }
    }
    
    return even_no_digits
}