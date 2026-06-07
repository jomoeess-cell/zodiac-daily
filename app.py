#!/usr/bin/env python3
"""測試代碼 - 故意包含各種問題"""

# ❌ 問題 1: 硬編碼密碼
API_KEY = "sk-1234567890abcdef"
PASSWORD = "supersecret123"

# ❌ 問題 2: 危險函數
user_input = input("Enter code: ")
result = eval(user_input)

# ❌ 問題 3: 格式問題
import os,sys,math
from flask import Flask, request,jsonify


def hello( name,age ):
    return {'name':name,'age':age}

# ✅ 正確代碼
def greet(name: str) -> str:
    """正確的函數"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Test"))