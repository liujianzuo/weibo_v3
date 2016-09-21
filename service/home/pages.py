#!/usr/bin/env python
#_*_coding:utf-8_*_
from dao import models
from django.core.paginator import  Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from decimal import Decimal

from dao.ormdjango import get_all_article

def Pager(request):
    after_range_num = 5
    before_range_num = 4
    page = int(request.GET.get('page', '1'))  # 获取页码
    if page < 1:
        page = 1

    ret = get_all_article()
    book_list = list(ret)
    print(book_list)

    paginator = Paginator(book_list, 4)  # 把数据和每页显示多少条 传入
    try:
        p = paginator.page(page)  # 获取当前页的对象
    except (EmptyPage, InvalidPage, PageNotAnInteger):  # 空页  页面无效多取超出范围  不是整数时 取第一页
        p = paginator.page(1)
    if page >= after_range_num:  # 页面最少显示5页
        # 如果page超出5页  就应该取 page的前4页到后4页 加上page 一共是9页
        page_range = paginator.page_range[page - 5:page + 4]

    else:
        # 如果没超过第5页，就取第一页 到 当前页加4   因为索引从0开始，而页码是从1开始的
        page_range = paginator.page_range[0:int(page) + before_range_num]

    li = []
    li.append(p)
    li.append(page_range)
    li.append(book_list)
    return li