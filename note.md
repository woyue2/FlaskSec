# env
conda install flask-sqlalchemy

# db
>>> python3
>>> from app import db

flask shell
db.create_all()
或者
python3
from xx import app,db
app.app_context.push()
db.create_all()

    pip list
    pip freeze > requirements_20211206.txt        #导出当前环境所有的依赖包及其对应的版本号
    pip install -r requirements_20211206.txt      #在新的环境中安装导出的包
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  -r F:/File_Anaconda/CV2020_RealTimeImageAnimation/requirements.txt
     
     
     
     
    conda list
    conda list -e > requirements.txt              #导出当前环境所有的依赖包及其对应的版本号
    conda install --yes --file requirements.txt   #在新的环境中安装导出的包
