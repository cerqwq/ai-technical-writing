# ✍️ AI Technical Writing

AI技术写作工具，支持技术文档、API文档、教程生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 技术文档生成
- 📋 API参考文档
- 📚 教程生成
- 🚀 快速开始指南
- 🔧 故障排除指南
- 🔍 文档审查

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_technical_writing import create_tools

tools = create_tools()

# 技术文档
doc = tools.generate_technical_doc("认证系统", "开发者", "架构文档")

# API文档
api = tools.generate_api_reference(endpoints, "FastAPI")

# 教程
tutorial = tools.generate_tutorial("Python装饰器", "intermediate", "30分钟")

# 快速开始
getting_started = tools.generate_getting_started("Sans", ["Python", "FastAPI"])

# 故障排除
troubleshooting = tools.generate_troubleshooting(common_issues)

# 文档审查
review = tools.review_documentation(docs)
```

## 📁 项目结构

```
ai-technical-writing/
├── tools.py       # 技术写作工具核心
└── README.md
```

## 📄 许可证

MIT License
