package main

import (
	"fmt"
	"io"
	"os"
)

type movement struct {
	direction string
	distance  int
}

func main() {
	moves := make([]movement, 0)
	var direction string
	var distance int
	_, err := fmt.Fscanf(os.Stdin, "%s %d", &direction, &distance)
	for err != io.EOF {
		moves = append(moves, movement{direction: direction, distance: distance})
		_, err = fmt.Fscanf(os.Stdin, "%s %d", &direction, &distance)
	}
	horizontal := 0
	vertical := 0
	for _, m := range moves {
		switch m.direction {
		case "forward":
			horizontal += m.distance
		case "up":
			vertical -= m.distance
		case "down":
			vertical += m.distance
		}
	}
	fmt.Println(horizontal, vertical)
	fmt.Println(horizontal * vertical)
}
