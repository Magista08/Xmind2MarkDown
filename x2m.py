#!/usr/bin/python
# -*- coding:utf-8 -*-

# Packages
import xmindparser
import sys

# Universal Signal
CODE = False
CODE_TYPE = ["shell", "c++", "c", "python", "java", "javascript", "c#", "html", "css", "javascript", "php"]
CATALOG_LEVEL = 5
SERIAL_NUM_NEED = True


def GetData(_input_file, _output_path):
    xmindparser.config = {
        'showTopicId': True,
        'hideEmptyValue': False
    }
    content = xmindparser.xmind_to_dict(_input_file)
    content = content[0]['topic']  # 画布
    return content


def UpdateIndex(_quene, _max_layer_nodes, _output_file):
    # Redirect
    global CODE
    assert (len(_quene) != _max_layer_nodes)
    quene = _quene[:]
    max_layer_nodes = _max_layer_nodes[:]
    for i in range(len(_quene) - 1, -1, -1):
        quene[i] += 1
        if quene[i] >= max_layer_nodes[i]:
            quene.pop()
            max_layer_nodes.pop()
        else:
            break
    return quene, max_layer_nodes


def RedirectPtr(_root, _quene):
    global CODE
    ptr = _root
    for i in _quene[1:]:
        ptr = ptr['topics'][i]
    return ptr


def OutputText(_output_file, _text, _level, _quene):
    global CODE, SERIAL_NUM_NEED
    output_string = str()
    space_index = "  " * (_level - CATALOG_LEVEL)

    # Hyperlink
    if _text.get('link') is not None:
        output_string = space_index + "- "
        output_string += "[" + _text['title'] + "](" + _text['link'] + ")\n"
        _output_file.write(output_string)
        return

    # Images
    elif _text['title'] == "[Image]" and _text['note'] is not None:
        _output_file.write(space_index + _text['note'])
        _output_file.write("\n")
        return

    # Code Write
    elif CODE is True and _text.get('note') is not None and _text.get('title') is None:
        _output_file.write(space_index)
        _output_file.write(_text['note'].replace("\r\n", ("\n" + space_index)))
        _output_file.write("\n" + space_index + "```" + "\n\n")
        CODE = False
        return

    # Do the Normal Writing

    # Pages Title
    if _level == 2:
        output_string = "<center><h1>" + _text['title'].replace("\n", " ") + "</h1></center>"
        output_string += "\n[TOC]"  # Add the catalog
        output_string += '\n<div STYLE="page-break-after: always;"></div>'  # Paging break

    # Subtitle
    elif (_level > 2) and (_level <= CATALOG_LEVEL) and _text.get('topics') is not None:
        if SERIAL_NUM_NEED:
            serial_num = list()
            for i in range(1, _level - 1):
                serial_num.append(str(_quene[i] + 1))
            serial_text = ".".join(serial_num)
            output_string = "#" * (_level - 2) + " " + serial_text + " " + _text['title']
        else:
            output_string = "#" * (_level - 2) + " " + _text['title']

    # Text with non-sequence serial
    else:
        if _text.get('title') is None:
            output_string = "\n"
        else:
            output_string = "  " * (_level - CATALOG_LEVEL - 1) + "- " + _text['title']
    '''
    # Plain text
    else:
        if _text.get('title') is None:
            output_string = "\n"
        else:
            output_string = space_index + _text['title']
    '''

    # Code Detect
    if (_text.get('note') is not None) and (_text['note'].lower() in CODE_TYPE):
        output_string += "\n" + space_index + "```" + _text['note'].upper() + "\n"
        CODE = True

    # Note
    elif _text.get('note') is not None:
        output_string += "\n" + space_index + "```\n" + space_index \
                         + _text['note'].replace("\r\n", ("\n" + space_index)) + "\n" \
                         + space_index + "```"
    # Change the line
    if CODE is False:
        output_string += "\n\n"

    _output_file.write(output_string)


def WriteMarkDown(_dict_data, _output_path):
    # output file
    output_file = open(_output_path, 'w')

    # parameters
    # Depth First Search
    quene = [0]
    max_layer_nodes = [1]
    ptr = _dict_data

    # Get the data by DFS
    while len(quene) != 0:
        if (ptr.get("topics") is None) or (len(ptr["topics"]) == 0):
            OutputText(output_file, ptr, (len(quene) + 1), quene)  # Default as the plain text
            quene, max_layer_nodes = UpdateIndex(quene, max_layer_nodes, output_file)
            ptr = RedirectPtr(dict_data, quene)
        else:
            quene.append(0)
            max_layer_nodes.append(len(ptr["topics"]))
            OutputText(output_file, ptr, len(quene), quene)
            ptr = ptr["topics"][0]


if __name__ == '__main__':
    args = len(sys.argv)
    if args < 3:
        print("USAGE: python x2m.py <input_file> <output_path> { windows = 1 | linux = 0 }")
        exit(1)

    # Get the parameter
    input_file = sys.argv[1]
    output_path = sys.argv[2]
    OS = sys.argv[3]

    # Change the path if need
    if int(OS) == 1:
        file_name = input_file.split('\\')[-1][:-6]
        output_path += "\\" + file_name + ".md"
    else:
        file_name = input_file.split('/')[-1][:-6]
        if output_path[-1] == "/":
            output_path += file_name + ".md"
        else:
            output_path += "/" + file_name + ".md"

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

    # Read Data from the .xmind file
    print("=== Getting Data from {} ===".format(input_file))
    dict_data = GetData(input_file, output_path)
    print("=== Done ===")
    print()

    # Write the data to the .md file
    print("=== Writing the Data to {} ===".format(output_path))
    WriteMarkDown(dict_data, output_path)
    print("=== Done ===")
