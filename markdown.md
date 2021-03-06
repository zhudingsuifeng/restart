## Markdown

[Markdown简介](#Markdown简介)

[Markdown标题](#Markdown标题)

[Markdown段落格式](#Markdown段落格式)

[Markdown列表](#Markdown列表)

[Markdown区块(引用)](#Markdown区块(引用))

[Markdown代码](#Markdown代码)

[Markdown链接](#Markdown链接)

[Markdown图片](#Markdown图片)

[Markdown表格](#Markdown表格)

[Markdown页内跳转](#Markdown业内跳转)

[Markdown高级技巧](#Markdown高级技巧)

### Markdown简介

Markdown是一种轻量级的「标记语言」，它的优点是语法简洁，纯文本兼容性好。  

Markdown有段落的概念，如果没有另起一段，不管文本内容是否换行，结果还是显示在一行中。
在行尾添加两个空格与回车，或者直接增加单独一个空行都能实现分段。

Typora将输入窗口与预览窗口合二为一，实现了真正的实时预览，并且同时支持windows和linux。

## Markdown标题

Markdown中，在文本前面添加#即可设置标题，#越多标题越深，最多支持六级标题，数字越大，标题越小。

注意#符号与文本之间有空格，用于区分语法符号与文本内容。

# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

## Markdown段落格式

### 段落

Markdown段落的换行是使用两个以上的空格加上回车，也可以在段落后面使用一个空行来表示重新开始一个段落。

### 字体

*斜体文本*

_斜体文本_

**粗体文本**

__粗体文本__

***粗斜体文本***

___粗斜体文本___

### 分割线

可以在一行中用三个以上的星号、减号、底线来建立一个分割线，符号之间可以用空格，但是要独占一行。

***
*****
---
___
_____
_ _ _

### 删除线

如果段落上的文字要添加删除线，需要在文字的两端加上两个波浪线~~。

~~baidu.com~~

### 下划线

下划线可以通过HTML的<u>标签来实现。

<u>带下划线文本</u>

### 脚注

> 创建脚注格式类似这样[^脚注]，gitee暂时不支持脚注，会直接跳转到404，github会将脚注内容显示在文末。

[^脚注]: Markdown脚注添加，gitee暂时不支持脚注，会直接跳转到404

## Markdown列表

### 无序列表

无序列表使用星号、加号或者是减号作为列表标记：

* Red
* Green
* Blue

等同于：

+ Red
+ Green
+ Blue

也等同于：

- Red
- Green
- Blue

### 有序列表

有序列表则使用数字接着一个英文句点：

1. bee
2. ant
3. bird

### 列表嵌套

列表嵌套只需要在子列表中的选项前面添加四个空格即可，有序列表与无序列表都可以嵌套，还可以混合嵌套。

结束列表需要在列表内容下面添加空行。

1. animal
    - bee
    - ant
2. plant

## Markdown区块(引用)

Markdown区块引用实在段落开头使用>符号，然后后面紧跟一个空格符号，区块和列表可以交叉嵌套使用。

> 区块引用

> 区块嵌套
> > 区块下一层
> > > 更深一层区块

> 区块中使用列表
> 1. 第一项

* 列表中使用区块
    > 区块

## Markdown代码

### 单行代码

单行代码可以使用反引号包起来(\`)

`print("hello world")`

### 多行代码

多行代码可以使用\`\`\`包裹，并指定编程语言(也可以不指定):
```python3
if __name__ == "__main__":
    print("hello world")
```

## Markdown链接

Markdown支持行内式和参考式两种链接语法。

行内式的链接文字用[方括号]标记，方括号后面紧接着圆括号并插入网址链接。

这是一个[百度](http://www.baidu.com) 的链接。

参考式的链接是在链接文字的括号后面再接上另一个方括号，而在第二个方括号里面要填入用以辨识链接的标记。

类似于文章中的参考文献。注意空行分段。

这是一个[参考式链接][1]

[1]: http://www.baidu.com/

参考式链接重点不在于它比较好写，而是相较于行内式，更易于阅读。

## Markdown图片

Markdown图片语法，开头一个感叹号!，接着一个方括号包裹代替文字，接着一个圆括号包裹着图片地址。

![gitee](https://portrait.gitee.com/uploads/avatars/user/306/920508_zhudingsuifeng_1644377386.png!avatar60 "可选标题")

## Markdown表格

Markdown制作表格使用|来分割不同的单元格，使用-来分隔表头和其他行。
|表头|表头|
|----|----|
|表格|表格|
|表格|表格|

-: 右对齐，:- 左对齐，:-: 居中对齐。
|左对齐|居中对齐|右对齐|
|:-----|:------:|-----:|
|单元格|单元格|单元格|
|单元格|单元格|单元格|

## Markdown页内跳转

Markdown业内跳转可以通过markdown语法和html语法两种形式实现。

gitee默认左侧对markdown文件都做了类似目录的链接，不在单独支持页内跳转，github能正常显示。

### Markdown语法

[Markdown简介](#Markdown简介)

### Html语法

[跳至文末](#down)

除了\<a\>标签，还有\<div\>、\<h2\>等标签同样能达到锚点的效果。

想要在Typora中达到页内跳转的效果，需要**按住ctrl**点击。

## Markdown高级技巧

Markdown支持HTML元素、公式、流程图等高级技巧，但是这与Markdown简洁的特性相违背，使用较少。

### 特殊字符转义

Markdown使用反斜杠转义特殊字符：

```
\\    反斜线
\`    反引号
\*    星号
\_    下划线
\{\}  花括号
\[\]  方括号
\(\)  小括号
\#    井号
\+    加号
\-    减号
\.    英文句点
\!    感叹号
```

<a id = "down">结尾</a>
