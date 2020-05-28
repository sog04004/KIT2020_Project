from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

import json

champion_dict = {
    1:{'name':"애쉬", 'skill':["마법의 수정화살", "점멸 (사용불가)"]},
    2:{'name':"이즈리얼", 'skill':["정조준 일격", "점멸 (사용불가)"]},
    3:{'name':"미스포츈", 'skill':["쌍권총 난사", "점멸 (사용불가)"]}}

@app.route('/hello/')
def hello():
    return 'Hello. World!'

@app.route('/hello/<name>')
def hellovar(name):
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
    return render_template('gamestart.html', data=character)

@app.route('/gamecreate')
def gamecreate():
    return render_template('gamecreate.html')

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        return "{0}님 반갑습니다. (HP {1}으로 게임을 시작 합니다.".format(character["name"], character["hp"])

@app.route('/create/<int:num>')
def create_num(num):
    if num == 1: 
        return champion_dict[1]['name']
    elif num == 2:
        return champion_dict[2]['name']
    elif num == 3:
        return champion_dict[3]['name']
    else:
        return "알 수 없는 행동"

@app.route('/action/<int:num>')
def action_num(num):
    if num == 1: #싸운다
        return "싸운다"
    elif num == 2: #도망간다
        return "당신은 뒤도 안돌아보고 도망 쳤습니다."
    else:
        return "알 수 없는 행동"

if __name__ == '__main__':
    app.run(debug=True)