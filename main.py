#author Delika Pratiwi - Delikapratiwi@gmail.com

from app import db
from app import app
from app.models import News, Topic
from flask import jsonify, request

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'News': News, 'Topic': Topic}

# endpoint to show all news
@app.route("/news", methods=["GET"])
def get_news():
    news_data = News.query.all()
    dataList = []
    if news_data is not None:
        for item in news_data:
            dataTempObj = {
                'id': item.id,
                'title': item.title,
                'description': item.description,
                'status': item.status
            }
            dataList.append(dataTempObj)
        return jsonify(dataList)
    else:
        return jsonify(error_message='data kosong!')

# endpoint to create new user
@app.route("/news", methods=["POST"])
def add_news():
    title = request.json['title']
    description = request.json['description']
    status = 0

    new_news = News(title, description, status)

    db.session.add(new_news)
    db.session.commit()

    return jsonify(id=new_news.id, title=new_news.title, description=new_news.description)

# endpoint to get news detail by id
@app.route("/news/<id>", methods=["GET"])
def news_detail(id):
    news = News.query.get(id)
    if news is not None:
        return jsonify(id=news.id, title=news.title, description=news.description, status=news.status)
    else:
        return jsonify(error_message='data kosong!')

# endpoint to update news
@app.route("/news/<id>", methods=["PUT"])
def news_update(id):
    news = News.query.get(id)
    title = request.json['title']
    description = request.json['description']
    status = request.json['status']

    news.title = title
    news.description = description
    news.status = status
    if news is not None:
        db.session.commit()
        return jsonify(id=news.id, title=news.title, description=news.description, status = status)
    else:
        return jsonify(error_message='data kosong!')


# endpoint to delete news
@app.route("/news/<id>", methods=["DELETE"])
def news_delete(id):
    news = News.query.get(id)

    if news is not None:
        db.session.delete(news)
        db.session.commit()

        return jsonify(id=news.id, title=news.title, description=news.description)
    else:
        return jsonify(error_message='data kosong!')

# endpoint to show all topics
@app.route("/topic", methods=["GET"])
def get_topic():
    topic_data = Topic.query.all()
    dataList = []
    if topic_data is not None:
        for item in topic_data:
            dataTempObj = {
                'id': item.id,
                'name': item.name,
                'news_id': item.news_id
            }
            dataList.append(dataTempObj)
        return jsonify(dataList)
    else:
        return jsonify(error_message='data kosong!')

# endpoint to create new topic
@app.route("/topic", methods=["POST"])
def add_topic():
    name = request.json['name']
    news_id = request.json['news_id']

    new_topic = Topic(name, news_id)

    db.session.add(new_topic)
    db.session.commit()

    return jsonify(id=new_topic.id, name=new_topic.name, news_id = new_topic.news_id)

# endpoint to get topic detail by id
@app.route("/topic/<id>", methods=["GET"])
def topic_detail(id):
    topic = Topic.query.get(id)

    if topic is not None:
        return jsonify(id=topic.id, name=topic.name, news_id=topic.news_id)
    else:
        return jsonify(error_message='data kosong!')


# endpoint to update topic
@app.route("/topic/<id>", methods=["PUT"])
def topic_update(id):
    topic = Topic.query.get(id)
    name = request.json['name']
    news_id = request.json['news_id']

    topic.name = name
    topic.news_id = news_id

    if topic is not None:
        db.session.commit()
        return jsonify(id=topic.id, name=topic.name, news_id=topic.news_id)
    else:
        return jsonify(error_message='data kosong!')

# endpoint to delete topic
@app.route("/topic/<id>", methods=["DELETE"])
def topic_delete(id):
    topic = Topic.query.get(id)

    if topic is not None:

        db.session.delete(topic)
        db.session.commit()

        return jsonify(id=topic.id, name=topic.name, news_id=topic.news_id)
    else:
        return jsonify(error_message='data kosong!')

# endpoint to show all news by filter status (0 = publish, 1 = draft, 2 = delete)
@app.route("/news-filter-status/<status>", methods=["GET"])
def get_news_by_filter_status(status):
    news_data = News.query.filter_by(status=status).all()
    dataList = []
    if news_data is not None:
        for item in news_data:
            dataTempObj = {
                'id': item.id,
                'title': item.title,
                'description': item.description,
                'status': item.status
            }
            dataList.append(dataTempObj)
        return jsonify(dataList)
    else:
        return jsonify(error_message='data kosong!')


# endpoint to show all news by filter topic
@app.route("/news-filter-topic/<topic>", methods=["GET"])
def get_news_by_filter_topic(topic):
    news_data = News.query.join(Topic, News.id == Topic.news_id)\
        .add_columns(News.id, News.title,News.description, News.status, Topic.news_id, Topic.name)\
        .filter(News.id == Topic.news_id).filter(Topic.news_id == topic)

    dataList = []
    if news_data is not None:
        for item in news_data:
            dataTempObj = {
                'id': item.id,
                'title': item.title,
                'description': item.description,
                'topicName': item.name,
                'status':item.status
            }
            dataList.append(dataTempObj)
        return jsonify(dataList)
    else:
        return jsonify(error_message='data kosong!')


if __name__ == '__main__':
    app.run(debug=True)