#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt 
@file: gen_readme.py 
@time: 2022-10-25
@contact: danerlt001.gmail.com
@des: 生成README
"""

import os
import sys
import traceback

current_path = os.path.dirname(os.path.abspath(__file__))
readme_path = os.path.join(current_path, "README.md")
python3_path = os.path.join(current_path, "Python3")


def get_tags_by_python_file(file_path):
    """从文件中获取标签

    :param file_path: 文件路径
    :return: 标签 多个标签用逗号分隔
    """
    try:
        not_tags = ["#", "Related", "Topics", "👍", "👎"]

        tags = []
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line and "Related Topics" in line:
                    # 示例: #  Related Topics 栈 树 深度优先搜索 二叉树 👍 925 👎 0
                    arr = line.split(" ")
                    for item in arr:
                        item = item.strip()
                        if item and item not in not_tags:
                            try:
                                int_tem = int(item)
                                # 说明是数字
                            except Exception:
                                # 说明不是数字 是标签
                                tags.append(item)

        if tags:
            return ",".join(tags)
        else:
            return ""
    except Exception:
        return ""


def gen_content():
    """生成表格"""
    table_head = "| 题目 | 算法实现  |  标签| \n|------|-------------|------|"

    tables = {}
    for py_file in os.listdir(python3_path):
        py_file_path = os.path.join(python3_path, py_file)
        if os.path.isfile(py_file_path):
            # py_file s.g. 100.相同的树.py
            try:
                topic_num, py_file_name, _ = py_file.split(".")
            except Exception as e:
                print(f"gen_content split 失败, py_file: {py_file}")
                raise
            tags = get_tags_by_python_file(py_file_path)
            row = f"| {topic_num}.{py_file_name} | [{py_file}](./Python3/{py_file}) | {tags}"
            topic_num = int(topic_num)  # 将题目号转成int类型
            tables[topic_num] = row

    tables_list = []
    for key in sorted(tables.keys()):
        row = tables[key]
        tables_list.append(row)
    tables_str = "\n".join(tables_list)

    content = f"{table_head}\n{tables_str}"
    print("生成内容成功")
    return content


def gen_title():
    """
    生成标题
    :return:
    """
    title = "# leetcode 题解\n\n## Python3实现"
    print("生成标题成功")
    return title


def write_data(data):
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(data)
    print("写入数据成功")


def gen_readme():
    title = gen_title()
    content = gen_content()
    data = title + "\n\n" + content
    write_data(data)
    print("生成README文件成功")


def main():
    try:
        gen_readme()
    except Exception as e:
        t, v, tb = sys.exc_info()
        traceback.print_tb(tb)


def t_tags():
    tags = get_tags_by_python_file(os.path.join(python3_path, "392.判断子序列.py"))
    print(tags)


if __name__ == '__main__':
    main()
