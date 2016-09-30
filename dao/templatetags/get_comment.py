#!/usr/bin/env python
#_*_coding:utf-8_*_
# !/usr/bin/env python
# coding:utf-8
from django import template
from django.utils.safestring import mark_safe
# from django.template.base import  Node, TemplateSyntaxError

register = template.Library()


@register.simple_tag
def my_simple_time(v1, v2, v3):
    return v1 + v2 + v3


@register.simple_tag
def my_input(id, arg):
    result = "<input type='text' id='%s' class='%s' />" % (id, arg,)
    return mark_safe(result)


my_comment_html = """
<div class="list_li S_line1 clearfix">
                    <div class="WB_face W_fl">
                        <a href="">
                            <img style="width: 30px;height: 30px" src="" alt="">
                        </a>
                    </div>
                    <div class="list_con">
                        <div class="WB_text">
                            <a href="">大佐</a>
                            <a href="http://huodong.weibo.com/travel2016?ref=icon ">
                                <i class="W_icon icon_airball">☺</i>
                            </a>
                            ：笑的肚子疼
                            <img src="" alt="我是表情">
                        </div>
                        <div class="WB_func clearfix" style="display: block">
                            <div class="WB_handler">
                                <ul class="ul_ul" >
                                    <li><span class="line S_line1">
                                        <a class="S_txt1" href="">
                                        <span  class="line S_line1">
                                            <em class="glyphicon glyphicon-thumbs-up"></em>
                                            <em>10</em>
                                        </span>
                                        </a>
                                        </span>
                                    </li>
                                    <li><span class="line S_line1">
                                        <span onclick="Sun_Repeat(this)" class="S_txt1">回复</span>
                                        </span>
                                    </li>

                                    <li class="hide">举报</li>


                                </ul>
                            </div>
                            <div>今天 14:30</div>
                        </div>
                    </div>
                </div>
"""
@register.simple_tag
def get_comment_handler(info_comment):



    return 123
