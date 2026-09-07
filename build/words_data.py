# -*- coding: utf-8 -*-
"""
新概念英语第一册 · 单词数据（单一事实源）
功能：按课次收录生词，供 build_words.py 注入 words.html
约定：绝不手写 JS 对象字面量，一律 json.dumps(ensure_ascii=False) 注入

每个词的字段：
  w      单词/词组（造句时必须用上它，容许复数/过去式/ing 等变形）
  ipa    音标
  pos    词性
  zh     中文释义
  lesson 首次出现的课次（1..144）
  egs    3 个例句 —— 给孩子看的范例，每句 ≥5 个单词、必须用上该词、三句互不重复
         ⭐ 孩子没有判断能力，例句错了他会照着学，所以规则焊进 build_words.py 的 validate()

生词表依据：新概念第一册官方生词表（2026-09-07 已上网核对 Lesson 1-24）
不收录纯品牌专有名词（Volvo / Peugeot / Ford 等），那些对造句练习没有价值。
"""

UNITS = []

import words_u1, words_u2, words_u3, words_u4, words_u5, words_u6
for _m in (words_u1, words_u2, words_u3, words_u4, words_u5, words_u6):
    UNITS.append(_m.CHAPTER)

DATA = {"units": UNITS}
