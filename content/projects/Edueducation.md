---
title: "Based on LLM to judge student learning state"
date: 2023-08-28T15:00:30.183Z
extra:
  link: https://github.com/BiorelaxA/EduExtension-HIT
description: 📊 A browser plug-in that can be used to monitor the user's learning status
taxonomies:
  tags:
    - LLM
    - Python
---

## 项目名称
> EduExtension-HIT

## 运行条件
> 目前还在开发中，这里列出当前配置  
* Vue3相关组件安装
* Django相关框架组件安装
* Python3.9以上
* LangChain,Spacy,Faiss,LTP相关组件安装

## 运行说明
> 当前只能以开发者模式运行
* 进入后端目录，运行`python manage.py runserver`
* 进入前端目录，运行`npm run serve`
* 浏览器访问`http://localhost:8080`
* 管理员账号：admin， 密码：0

## 技术架构
> Vue3 + BootStrap + Django + Langchain + Spacy + Faiss + Python>=3.9

>前端部分
>1. 任何页面的外观与ui设计
>2. 所有后端函数的前端调用
>3. sidepanel页面时间选取展示
>4. 历史记录页面完成
>5. PreInstall页面完成
>6. 前端加一个markdown显示器(important)
>7. 判题部分若干

>后端部分
>1. 动态获取取bilibili网站的cookie（或者在绕过SESSDATA的前提下获得字幕信息？）
>2. views.py相关函数的完成
>3. 爬虫相关
>4. 任何流程的实现逻辑设计


>接口部分
>1. api.js下相关接口的完成
>2. 模型与后端功能接口完成（可以使用工厂模式）
>3. 有关密钥部分（api-key）等隐私内容传输的适配
>4. csrf相关

>模型相关
>1. 星火大模型适配
>2. 活字大模型适配
>3. Prompt自强化
>4. 流式问答

>数据库部分
>1. neo4j图数据库
>2. Prompt数据库
>3. 数据库的分页和滚动加载

>测试
>1. 实际产品功能测试与反馈