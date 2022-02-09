from flask import Blueprint, request
from app.models import db, Comment


comment_routes = Blueprint('comments', __name__)


@comment_routes.route('/new', methods=['POST'])
def create_comment():
    data = request.json

    comment = Comment(userId=data['userId'],
                      projectId=data['projectId'],
                      comment=data['comment'])

    db.session.add(comment)
    db.session.commit()

    return {'message': 'success'}


@comment_routes.route('/<int:id>', methods=['DELETE'])
def delete_comment(id):

    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()

    return {'message': 'success'}


@comment_routes.route('/<int:id>', methods=['PUT'])
def edit_comment(id):
    data = request.json

    comment = Comment.query.get(id)
    comment.comment = data['comment']
    db.session.commit()

    return {'message': 'success'}