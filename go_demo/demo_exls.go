package main

import (
	"fmt"
	"github.com/360EntSecGroup-Skylar/excelize"
	"reflect"
)

func Export(name []string, list []map[string]int) {
	column := []string{
		"A",
		"B",
		"C",
		"D",
	}
	sheetName := "Sheet1"
	f := excelize.NewFile()
	index := f.NewSheet(sheetName)
	f.SetActiveSheet(index)
	n := len(name)
	for i := 0; i < n; i++ {
		f.SetCellValue(sheetName, column[i]+"1", name[i])
	}
	for k, v := range list {
		//for _, vv := range v {
		f.SetCellValue(sheetName, column[0]+fmt.Sprint(k+2), v["username"])
		f.SetCellValue(sheetName, column[1]+fmt.Sprint(k+2), v["age"])

	}
	if err := f.SaveAs("test.xlsx"); err != nil {
		fmt.Println(err)
	}
}

type person struct {
	name string
	city string
	age  string
}

func main() {
	name := []string{
		"ID",
		"用户名",
		"年龄",
	}
	data := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	//list := [][]person{}
	list := []map[string]int{}
	fmt.Println("v1 type:", reflect.TypeOf(list))
	//list = append(list, []person{{"1", "u1", "11"}})
	//list = append(list,  []person{{"2", "u2", "22"}})
	//list = append(list,  []person{{"3", "u3", "33"}})ist = append(list, [])
	//l
	for _, value := range data {
		list = append(list, map[string]int{
			"username": value,
			"age": value*10,
		})
	}

	//list = append(list, person{"4", "u4", "44"})
	fmt.Println(list)
	Export(name, list)
}
