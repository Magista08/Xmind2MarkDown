# README

## Description

This python file is to transfer the .xmind file to .md file. Unlike the usual tool written by someone else, the last node of the xmind will directly changed into the plain text instead of a title or a subtitle. 

## Usage

### Command

#### Linux

```shell
python3 x2m.py <xmind_file> <output_folder>
```

 #### Windows

```power
python x2m.py <xmind_file> <output_folder>
```

### Insert Image

If you want to insert a image, please make sure you should insert the image with no words on the node and add the correct note in the format of how markdown can track the image

```shell
note = ![<image_name>](<image_location>)
```

### Insert Code

HIGHLY NOT RECOMMEND TO USE THE CODE MODE OF THE MARKDOWN!!! It may have some problems about the showing the code part in the markdown if two code are too close. However, if you insist to add it, please do it in the following format

Add all your code as the sub-nodes on the original nodes, and a note of which programming language. Right now, this is what language it can recognize

```python
CODE_TYPE = ["shell", "c++", "c", "python", "java", "javascript", "c#"]
```

If you are using some programming language, it cannot recognize. Please add this programming language at line 10. The list named as `CODE_TYPE`. If you add your name (whatever it needs capitalize or uppercase), the code will recognize it.
