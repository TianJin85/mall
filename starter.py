"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""
from flask_debugtoolbar import DebugToolbarExtension

from app.app import create_app

app = create_app(environment='development')

app.config['SECRET_KEY'] = '<replace with a secret key>'

toolbar = DebugToolbarExtension(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def lin_slogan():
    return """<html><body>
        <style type="text/css">*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} a{color:#2E5CD5;cursor: 
    pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: 
    "Century Gothic","Microsoft yahei"; color: #333;font-size:18px;} h1{ font-size: 100px; font-weight: normal; 
    margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }</style><div style="padding: 24px 48px;"><p> 
    Lin <br/><span style="font-size:30px">心上无垢，林间有风。</span></p></div> 
    </body></html>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

"""
    1.配置后台视图函数增加商品增删改查
    2.撰写后台接口文档
"""