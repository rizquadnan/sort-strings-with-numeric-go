package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

func selectionSort(arr []string) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		minIdx := i
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIdx] {
				minIdx = j
			}
		}
		if minIdx != i {
			arr[i], arr[minIdx] = arr[minIdx], arr[i]
		}
	}
}

func main() {
	file, err := os.Open("./dataset/100k.txt")

	if err != nil {
		fmt.Println("Error opening the file:", err)
		return
	}
	defer file.Close()

	var words []string

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		word := strings.Split(line, "\n")[0] // Assuming words are separated by "@@@"

		words = append(words, word)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading the file:", err)
		return
	}

	fmt.Println(words[0])
	fmt.Println(words[len(words)-1])

	// Print the words
	// fmt.Println("Words in the array:")
	// fmt.Println(words)
	startTime := time.Now()
	selectionSort(words)
	fmt.Println(words)
	endTime := time.Now()
	elapsedTime := endTime.Sub(startTime)

	fmt.Printf("Code execution time: %s\n", elapsedTime)

}
