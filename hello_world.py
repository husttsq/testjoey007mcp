#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World程序
这是一个简单的Python Hello World示例
作者: Joey007
创建时间: 2025-08-22
"""

def main():
    """主函数"""
    print("Hello, World!")
    print("欢迎使用GitHub MCP工具！")
    print("这是一个通过MCP工具创建的Python程序")
    
    # 显示一些基本信息
    import datetime
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"当前时间: {current_time}")
    
    # 简单的交互
    name = input("请输入您的姓名: ")
    print(f"你好, {name}! 很高兴认识您！")

if __name__ == "__main__":
    main()
