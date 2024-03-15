from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # 允许所有源的跨域请求

# 示例心理测试题目和答案
questions = [
    {"id": 1, "question": "你在社交场合通常是怎样的人？", "options": ["外向", "内向", "中立"]},
    {"id": 2, "question": "面对挑战，你的第一反应是？", "options": ["直面挑战", "规划策略", "避免冲突"]}
]

# 示例函数：计算性格类型
def calculate_personality(answers):
    # 这里只是一个简单的示例逻辑
    if answers["1"] == "外向" and answers["2"] == "直面挑战":
        return "冒险型"
    else:
        return "思考型"

@app.route("/get_personality_test", methods=['GET'])
def get_personality_test():
    return jsonify(questions)

@app.route("/submit_answers", methods=['POST'])
def submit_answers():
    answers = request.json.get('answers', {})
    personality_type = calculate_personality(answers)
    description = "你是一个{}的人。".format(personality_type)
    return jsonify({"personalityType": personality_type, "description": description})

# 为了提供更好的用户体验，确保处理请求不会超时
# 对于耗时较长的处理流程，可以考虑采用异步处理方式或返回一个初步响应，
# 然后让前端轮询或使用其他机制（如WebSocket）来获取最终结果。

@app.route('/')
def index():
    return '🌟 欢迎来到心灵探索之旅！ 🌈'

if __name__ == '__main__':
    app.run(debug=True, host='10.21.134.107', port=5000)
