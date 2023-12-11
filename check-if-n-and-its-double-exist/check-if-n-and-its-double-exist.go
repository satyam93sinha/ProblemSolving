func checkIfExist(arr []int) bool {
    hashmap := make(map[int] bool)
    for _, num := range arr{
        if num % 2 == 0 && hashmap[num / 2] || hashmap[num * 2]{
            return true
        }
        hashmap[num] = true
    }
    
    return false
    
}