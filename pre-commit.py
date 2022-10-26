#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt 
@file: pre-commit.py
@time: 2022-10-25
@contact: danerlt001.gmail.com
@des: 生成README 这个文件要放在.git/hooks目录下 然后将文件名改成pre-commit
"""
import os
import sys
import traceback
from functools import cmp_to_key

from pathlib import Path

# 当前文件路径 .git/hooks/pre-commit 或者 leetcode/pre-commit
p = Path(__file__)

if ".git/hooks" in p.as_posix():
    # 说明是在.git hooks目录下
    root_path = p.parent.parent  # 项目根路径
else:
    # 说明是在项目目录下执行
    root_path = p.parent  # 项目根路径
readme_path = root_path.joinpath("README.md")
python3_path = root_path.joinpath("Python3")


def get_tags_by_python_file(file_path):
    """从文件中获取标签

    :param file_path: 文件路径
    :return: 标签 多个标签用逗号分隔
    """
    try:
        not_tags = ["#", "Related", "Topics", "👍", "👎"]
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        tags = []
        for line in lines:
            if line.strip() and "Related Topics" in line:
                # 示例: #  Related Topics 栈 树 深度优先搜索 二叉树 👍 925 👎 0
                arr = line.split(" ")
                for item in arr:
                    item = item.strip()
                    if item and item not in not_tags:
                        try:
                            int_tem = int(item)
                            # 没抛错 说明是数字
                        except Exception:
                            # 抛错了 说明不是数字 是标签
                            tags.append(item)

        if tags:
            return ",".join(tags)
        else:
            return ""
    except Exception:
        return ""


def compare_tpoic_num(x, y):
    try:
        x = int(x)
        y = int(y)
        return x - y
    except Exception:
        pass

    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1


def gen_python_content(path: Path = python3_path, suffix: str = ".py"):
    """生成python3内容
    :param path: 文件路径
    :param suffix: 文件后缀 .py文件
    """
    table_head = "| 题目 | 算法实现  |  标签| \n|------|-------------|------|"

    tables = {}
    for file in path.iterdir():
        if file.is_file() and file.suffix == suffix:
            filename = file.name  # 文件名
            # fix 文件名中有空格导致markdown显示错误的问题
            if " " in filename:
                new_filename = filename.replace(" ", "")
                new_file_path = file.parent.joinpath(new_filename)
                file.rename(new_file_path)
                filename = file.name

            # s.g. 100.相同的树
            filestem = file.stem  # 文件去除后缀之后的内容
            try:
                # 题目号 和 题目名称
                topic_num, topic_name = filestem.split(".")
            except Exception as e:
                print(f"gen_python_content split 失败, filestem: {filestem}")
                raise
            tags = get_tags_by_python_file(file)
            rela_path = file.relative_to(root_path).as_posix()  # 文件相对根路径的路径
            row = f"| {topic_num}.{topic_name} | [{filename}]({rela_path}) | {tags} |"
            tables[topic_num] = row

    tables_list = []
    for key in sorted(tables.keys(), key=cmp_to_key(compare_tpoic_num)):
        row = tables[key]
        tables_list.append(row)
    tables_str = "\n".join(tables_list)

    content = f"{table_head}\n{tables_str}"
    print("生成内容成功")
    return content


def write_data(data):
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(data)
    print("写入数据成功")


def gen_readme():
    title = "# leetcode 题解"
    python3_title = "## Python3实现"
    python3_content = gen_python_content(path=python3_path, suffix=".py")
    data = f"{title}\n\n{python3_title}\n\n{python3_content}\n\n"
    write_data(data)
    print("生成README文件成功")


def main():
    try:
        gen_readme()
        os.system("git add *.py")
        os.system("git add README.md")
    except Exception as e:
        t, v, tb = sys.exc_info()
        traceback.print_tb(tb)


if __name__ == '__main__':
    main()
