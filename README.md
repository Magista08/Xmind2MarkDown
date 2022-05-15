# README

## Description

This python file is to transfer the .xmind file to .md file. Unlike the usual tool written by someone else, the last node of the xmind will directly changed into the plain text instead of a title or a subtitle. 

## Usage

### Pre-request
Please make sure that python and package: `xmindparser` has installed in the system. 

```shell
pip3 install xmindparser
```

### Command

#### Linux

```shell
python3 x2m.py <xmind_file> <output_folder> 0
```

 #### Windows

```power
python x2m.py <xmind_file> <output_folder> 1
```

### Change the number of the subtitle

In the program, line 11, there is a variable named `CATALOG_LEVEL`. The subtitle number will be (`CATALOG_LEVEL` - 2). The default of the catalog level is 3 which means `x.x.x`, i.e. `1.1.1`. If you don't want so many subtitles, you can make this variable smaller.

### Insert Image

If you want to insert a image, please make sure you should insert the image with no words on the node and add the note in the correct format of how markdown can track the image. This is how you should put in your note.

```shell
note = ![<image_name>](<image_location>)
```

### Insert Code

The code mode is now available. If you are writing some code in the file. Please add the which language you want to show in the main node's note. Add a sub-node and make it content all clean and add the code in the note. Right now, this is what language it can recognize

```python
CODE_TYPE = ["shell", "c++", "c", "python", "java", "javascript", "c#", "html", "css", "javascript", "php"]
```

If you are using some programming language it cannot recognize, please add this programming language at line 10. The list named as `CODE_TYPE`



# 中文介绍

## 简介

本工具使用于如何把`.xmind`文件转换为`.md` 文件。网上有许多转换工具，但是他们都是按照子节点的个数直接转换为对应数量的标题。（我觉得有点蠢 lol）所以就自己建了一个自己的工具

## 使用方法

### 环境
确保运行的机器里面有python和`xmindparser`的安装包，可以通过以下命令安装安装包

```shell
pip3 install xmindparser -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

### 命令

#### Linux系统

```shell
python3 <源文件> <目标输出地址> 0
```

#### Windows 系统

```powershell
python <源文件> <目标输出地址> 1
```

### 改变子标题个数

在程序11行，有一个全局变量`CATALOG_LEVEL`. 这个全局变量控制着标题个数（无论标题有多少个，末尾子节点都不会转换为标题）如果你不需要这么多子标题，或者你需要更多的子标题，请对应减少或者增加这个变量的值

### 插入图片

如果你想插入图片，因为`xmindparser`库不能读取对应的图片，所以请按照一下格式，把对应的图片地址放在备注里面。该节点内容只能为图片或者文字 = "[Image]"

```
note = ![<图片名称>(<图片路劲>)
```

### 插入代码

如果想在某个节点放入代码，请在该节点的备注里面加入该代码的程序语言。并且清空子节点里面的内容，在对应的备注里面写上相应的代码。现在可识别出的程序语言有

```python
CODE_TYPE = ["shell", "c++", "c", "python", "java", "javascript", "c#", "html", "css", "javascript", "php"]
```

如果里面有其他语言，markdown可以识别，但是作者没有写进去的，请在代码第10行`CODE_TYPE` 的列表里面添加自己想用的语言。
