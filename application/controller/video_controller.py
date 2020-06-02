from application import app
from flask import render_template, request, current_app, jsonify
from application.model.dao.category_dao import categoryDao
from application.model.dao.video_dao import videoDao
from application.model.entity.comment import Comment

@app.route("/categories/<int:category_id>/videos/<int:video_id>")
def video(category_id, video_id):
    videos = current_app.config ['videos']
    categories = current_app.config ['categories']

    category = categories.search(category_id)
    videory = videos.get_video_by_id(video_id)
    videory.setViews(videory.getViews()+1)

    return render_template('comment.html', videory = videory, category = category)
    
