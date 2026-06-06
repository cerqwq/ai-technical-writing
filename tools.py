"""
AI Technical Writing - AI技术写作工具
支持技术文档、API文档、教程生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AITechnicalWritingTools:
    """
    AI技术写作工具
    支持：文档、API、教程
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_technical_doc(self, topic: str, audience: str, doc_type: str) -> str:
        """生成技术文档"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{topic}的{doc_type}文档：

目标读者：{audience}

要求：
1. 结构清晰
2. 内容准确
3. 示例丰富
4. 易于理解"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_api_reference(self, endpoints: List[Dict], framework: str) -> str:
        """生成API参考文档"""
        if not self.client:
            return "LLM客户端未配置"

        endpoints_text = json.dumps(endpoints, ensure_ascii=False)

        prompt = f"""请为{framework} API生成参考文档：

端点：{endpoints_text}

要求：
1. 端点说明
2. 参数说明
3. 返回值说明
4. 使用示例
5. 错误码说明"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_tutorial(self, topic: str, level: str, duration: str) -> str:
        """生成教程"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{level}级别的{topic}教程：

时长：{duration}

要求：
1. 循序渐进
2. 代码示例
3. 练习题
4. 常见问题"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_getting_started(self, project: str, tech_stack: List[str]) -> str:
        """生成快速开始指南"""
        if not self.client:
            return "LLM客户端未配置"

        tech_text = ", ".join(tech_stack)

        prompt = f"""请为{project}生成快速开始指南：

技术栈：{tech_text}

要求：
1. 安装步骤
2. 配置说明
3. 第一个示例
4. 下一步指引"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_troubleshooting(self, common_issues: List[Dict]) -> str:
        """生成故障排除指南"""
        if not self.client:
            return "LLM客户端未配置"

        issues_text = json.dumps(common_issues, ensure_ascii=False)

        prompt = f"""请生成故障排除指南：

常见问题：{issues_text}

要求：
1. 问题描述
2. 可能原因
3. 解决步骤
4. 预防措施"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def review_documentation(self, docs: str) -> Dict:
        """审查文档"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请审查以下文档：

{docs[:2000]}

请返回JSON格式：
{{
    "score": 1-100,
    "completeness": "完整性",
    "clarity": "清晰度",
    "accuracy": "准确性",
    "issues": ["问题"],
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"review": content}


def create_tools(**kwargs) -> AITechnicalWritingTools:
    """创建技术写作工具"""
    return AITechnicalWritingTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Technical Writing Tools")
    print()

    # 测试
    tutorial = tools.generate_tutorial("Python装饰器", "intermediate", "30分钟")
    print(tutorial[:300] + "...")
