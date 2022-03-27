#!/usr/bin/python
# -*- coding:utf-8 -*-

# Packages
import xmindparser
import sys

# Universal Signal
CODE = False
CODE_TYPE = ["shell", "c++", "c", "python", "java", "javascript", "c#"]


def GetData(_input_file, _output_path):
    xmindparser.config = {
        'showTopicId': True,
        'hideEmptyValue': False
    }
    content = xmindparser.xmind_to_dict(_input_file)
    content = content[0]['topic']
    return content


def UpdateIndex(_quene, _max_layer_nodes, _output_file):
    global CODE
    assert (len(_quene) != _max_layer_nodes)
    quene = _quene[:]
    max_layer_nodes = _max_layer_nodes[:]
    for i in range(len(_quene) - 1, -1, -1):
        quene[i] += 1
        if quene[i] >= max_layer_nodes[i]:
            quene.pop()
            max_layer_nodes.pop()
            if CODE is True:
                _output_file.write("```\n")
                CODE = False
            CODE = False
        else:
            break
    return quene, max_layer_nodes


def RedirectPtr(_root, _quene):
    global CODE
    ptr = _root
    for i in _quene[1:]:
        ptr = ptr['topics'][i]
    return ptr


def OutputText(_output_file, _text, _level):
    global CODE
    output_string = str()
    # Check the link
    if _text.get('link') is not None:
        output_string = "[" + _text['title'] + "](" + _text['link'] + ")\n"
        _output_file.write(output_string)
        return

    # Check the note
    elif _text['title'] == "[Image]" and _text['note'] is not None:
        _output_file.write(_text['note'])
        _output_file.write("\n")
        return

    # Do the Normal Writing
    if _level == 2:
        output_string = "<center><h1>" + _text['title'] + "</h1></center>\n"
    elif (_level > 2) and (_level <= 4):
        output_string = "#" * _level + " " + _text['title'] + "\n"
    elif (_level == -1) or (_text['title'] == "示例"):
        output_string = _text['title'] + "\n"
    else:
        output_string = "\t" * (_level - 5) + "- " + _text['title'] + "\n"

    # Check if the next sentences are all code
    if (_text.get('note') is not None) and (_text['note'] in CODE_TYPE):
        output_string += "```" + _text['note'] + "\n"
        CODE = True

    _output_file.write(output_string)


def WriteMarkDown(_dict_data, _output_path):
    # output file
    output_file = open(_output_path, 'w')

    # parameters
    quene = [0]
    max_layer_nodes = [1]
    ptr = _dict_data

    # Get the data by DFS
    while len(quene) != 0:
        if (ptr.get("topics") is None) or (len(ptr["topics"]) == 0):
            OutputText(output_file, ptr, -1)  # Default as the plain text
            quene, max_layer_nodes = UpdateIndex(quene, max_layer_nodes, output_file)
            ptr = RedirectPtr(dict_data, quene)
        else:
            quene.append(0)
            max_layer_nodes.append(len(ptr["topics"]))
            OutputText(output_file, ptr, len(quene))
            ptr = ptr["topics"][0]


if __name__ == '__main__':
    args = len(sys.argv)
    if args < 3:
        print("USAGE: $0 <input_file> <output_path> { windows = 1 | linux = 0 }")
        exit(1)

    # Get the parameter
    input_file = sys.argv[1]
    output_path = sys.argv[2]
    OS = sys.argv[3]

    # Change the path if need
    if int(OS) == 1:
        file_name = input_file.split('\\')[-1][:-6]
        output_path += "\\" + file_name + ".md"
    # Check the existence of the .xmind file
    try:
        open_signal = open(input_file)
        open_signal.close()
    except FileNotFoundError:
        print("File is not found.")
        exit(1)
    except PermissionError:
        print("You don't have permission to access this file.")
        exit(-1)
    if input_file[-6:] != ".xmind":
        print("Please Get an .xmind file!!! Can't you f**king see what this tool is?")
        exit(1)
    print(output_path)
    dict_data = GetData(input_file, output_path)
    WriteMarkDown(dict_data, output_path)