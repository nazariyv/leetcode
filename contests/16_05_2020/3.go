package main

import (
	"fmt"
	"sync"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
const MinUint = 0
const MaxUint = ^uint(MinUint)
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
const MinUint = 0
const MaxUint = ^uint(MinUint)
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

func goodNodes(root *TreeNode) int {
	var ans int
	var lst []int

	wg.Add(1)
	preorder(root, lst, &ans)

	ans++
	return ans
}

var mux sync.Mutex
var wg sync.WaitGroup

func maxTwo(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func max(lst *[]int) (maxInLst int) {
	maxInLst = MinInt
	if len(*lst) == 0 {
		return
	}
	for _, v := range *lst {
		maxInLst = maxTwo(maxInLst, v)
	}
	return
}

func preorder(t *TreeNode, lst []int, ans *int) {
	defer wg.Done()
	if t == nil {
		return
	}
	maxInLst := max(&lst)
	if len(lst) > 0 && t.Val >= maxInLst {
		// deadlock / race-condition otherwise
		mux.Lock()
		defer mux.Unlock()
		*ans++
	}
	lst = append(lst, t.Val)
	wg.Add(1)
	go preorder(t.Left, lst, ans)
	// preorder(t.Left, lst, ans)
	wg.Add(1)
	go preorder(t.Right, lst, ans)
	// preorder(t.Right, lst, ans)
}

func main() {
	t := TreeNode{
		Val: 2,
		Right: &TreeNode{
			Val: 4,
			Left: &TreeNode{
				Val: 10,
			},
			Right: &TreeNode{
				Val: 8,
				Left: &TreeNode{
					Val: 4,
				},
			},
		},
	}
	ans := goodNodes(&t)
	fmt.Println(ans)
}
