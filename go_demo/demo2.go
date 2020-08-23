/// 方法调用

package main

import "fmt"

type Integer int
func (a Integer) Less(b Integer) bool{  //表示a这个对象定义了Less这个方法，a可以为任意类型
	return a<b
}
//类型基于值传递，如果要修改值需要传递指针
func (a *Integer) Add(b Integer){
	*a+=b    //通过指针传递来改变值
}

func main() {
	c := Integer(5)
	fmt.Println(c.Less(90))
	b := Integer(5)
	b.Add(20)
	fmt.Println(b)


}
