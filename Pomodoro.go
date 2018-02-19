package main

import (
	"bufio"
	"fmt"
	"os"
	"time"
)

func main() {
	fmt.Printf("Welcome to the Pomodoro Timer!\n")
	reader := bufio.NewReader(os.Stdin)
	bufio.NewReader(os.Stdin)
	fmt.Print("Press Enter to start: ")
	//THIS READS BACK WHAT WAS RAW INPUTED
	text, _ := reader.ReadString('\n')
	fmt.Println(text)
	fmt.Println("Ok, ready to be productive? GO!")

	x := make([]int, 4)
	y := make([]int, 1500) //1500 secs = 25min
	z := make([]int, 900) //900 secs = 15min

	for c := range z {
		for a := range x {
			for b := range y {
				minutes := b / 60
				seconds := b % 60

				//timeformat := "%d:%2d" % minutes, seconds
				//fmt.Println(timeformat)
				fmt.Println(minutes, seconds)
				time.Sleep(time.Millisecond * 1000)

			}
			fmt.Println(a, "Take a 5 minute break!")
			time.Sleep(time.Second * 300) //300secs = 5min
		}
		fmt.Println(c, "15 minute break time! Go find taquitos!")
		time.Sleep(time.Second * 900)
	}
}
