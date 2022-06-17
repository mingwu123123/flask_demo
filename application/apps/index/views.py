from . import index_blu
from .models import Student
from flask import render_template,request
from application import db
from flask import flash
from flask import Flask, jsonify
from application.settings import redis_client

app = Flask(__name__)


@index_blu.route("/data/", methods=["POST"])
def index():
    """學生列表"""
    data_type = request.args.get('type')
    timestamp = request.args.get('timestamp')  # 毫秒级
    redis_client.set(f"{data_type}-{int(timestamp)}", request.json, px=30 * 1000) # 保存datatype，方便分别处理，数据量大过期时间不能过长
    return jsonify({"message": "ok"})  # dict 类型数据需要转型


@index_blu.route("/add",methods=["POST","GET"])
def add_student():
    if request.method == "POST":
        # 接受數據
        name = request.form.get("username")
        age = int(request.form.get("age"))
        sex = True if request.form.get("sex") == '1' else False
        class_number = request.form.get("class_number")
        description = request.form.get("description")
        # 驗證數據
        if age < 0 or age > 120:
            # 閃現信息[用於返回錯誤信息給客戶端,只顯示一次]
            flash("非法的年齡數值")

        # 保存入庫
        student = Student(name=name,age=age,sex=sex,class_number=class_number,description=description)
        try:
            db.session.add(student)
            db.session.commit()
        except:
            # 事務回滾
            db.session.rollback()

    return render_template("add.html")