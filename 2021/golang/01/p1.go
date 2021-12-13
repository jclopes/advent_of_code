package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	numbers := make([]int, 0)
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		n, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Fprintf(os.Stderr, "Fail to convert to integer:", err)
			os.Exit(1)
		}
		numbers = append(numbers, n)
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "Fail reading standard input:", err)
	}
	count := 0
	for i := 0; i < len(numbers)-1; i++ {
		if numbers[i] < numbers[i+1] {
			count++
		}
	}
	fmt.Println(count)
}
