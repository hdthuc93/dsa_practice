// https://leetcode.com/problems/binary-tree-inorder-traversal/description/
// inorder traversal: left - root - right

package main

import (
	"container/list"
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	result := []int{} // or var result []int
	stack := list.New()
	stack.PushBack(root)

	for stack.Len() > 0 {
		node := stack.Back().Value.(*TreeNode)
		stack.Remove(stack.Back())

		if node.Left != nil {
			newNode := &TreeNode{
				node.Val,
				nil,
				node.Right,
			}
			stack.PushBack(newNode)
			stack.PushBack(node.Left)
			continue
		}

		result = append(result, node.Val)

		if node.Right != nil {
			stack.PushBack(node.Right)
		}
	}

	return result
}

func buildTree(arr []any) *TreeNode {
	root := &TreeNode{
		arr[0].(int),
		nil,
		nil,
	}
	queue := list.New()
	queue.PushBack(root)

	for i := 1; i < len(arr); i += 2 {
		node := queue.Front().Value.(*TreeNode)
		queue.Remove(queue.Front())

		var leftNode, rightNode *TreeNode
		if arr[i] != nil {
			leftNode = &TreeNode{
				arr[i].(int),
				nil,
				nil,
			}
			queue.PushBack(leftNode)
		}
		if i+1 < len(arr) && arr[i+1] != nil {
			rightNode = &TreeNode{
				arr[i+1].(int),
				nil,
				nil,
			}
			queue.PushBack(rightNode)
		}

		node.Left = leftNode
		node.Right = rightNode
	}

	return root
}

func main() {
	arr := []any{1, 2, 3, 4, 5, nil, 8, nil, nil, 6, 7, 9}
	root := buildTree(arr)

	fmt.Println(inorderTraversal(root))
}
