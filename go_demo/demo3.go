package main

import "fmt"

func main() {
	//创建切片
	slice1 := make([]int, 5)       //元素初始值为0，初始个数为5
	slice2 := make([]int, 5, 10)   //元素初始值为0，初始个数为5，预留个数为10
	slice3 := []int{1, 2, 3, 4, 5} //初始化赋值
	fmt.Println(slice1, slice2, slice3, "\n")
	//map
	//创建
	//map1=make(map[键类型] 值类型)
	//map1=make(map[键类型] 值类型 存储空间)
	//赋值
	//map1[key]=value
	// 直接创建
	m2 := make(map[string]string)
	m2["a"] = "aa"
	m2["b"] = "bb"
	m2["c"] = "cc"
	fmt.Println(m2, "\n")
	// 初始化 + 赋值一体化
	m3 := map[string]string{
		"a": "aa",
		"b": "bb",
	}
	fmt.Println(m3)
	value, ok := m3["a"] // map取值 找到 了返回元素，没有返回false
	fmt.Println(value, ok)
}
