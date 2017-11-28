import os
import json
from flask import Flask, render_template, abort

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    path0 = 'home/shiyanlou/files'
    filename = os.listdir(path0)
    file1_path = os.path.join(path0, filename[0])
    file2_path = os.path.join(path0, filename[1])
    with open(file1_path, 'r') as papers1:
        file_content1 = json.loads(papers1.read())
    with open(files_path, 'r') as papers2:
        file_content2 = json.loads(papers2.read())
    title = {
            title1: file_content1['title']
            title2: file_content2['title']
            }

    return render_template('index.html', title=title)

@app.route('files/<filename>')
def file(filename):
    index_instance = index()
    if os.path.isfile(index_instance.file1_path) and os.path.isfile(index_instance.file2_path):
        file_content = {
                title1: index_instance.file_content1['title']
                title1: index_instance.file_content1['title']
                created_time1: index_instance.file_content1['created_time']
                created_time2: index_instance.file_content1['created_time']
                content1: index_instance.file_content1['content']
                content2: index_instance.file_content1['content']
                }
        return render_template('file.html', filename=filename)
    else:
        abort(404)
        return render_template('404.html', filename=filename)
    

if __name__ == '__main__':
    app.run()
