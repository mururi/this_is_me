from flask import render_template, redirect, url_for, abort, request
from . import main
from ..models import User, Post, Comment
from .forms import NewPost, UpdateProfile, NewComment
from .. import db, photos
from flask_login import login_required, current_user
from ..requests import get_quote
from sqlalchemy import desc

# Views
@main.route('/')
def index():
    title = 'This is Me'
    random_quote = get_quote()

    posts = Post.query.order_by(desc(Post.date_created)).all()

    return render_template('index.html', title = title, quote = random_quote, posts = posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    posts = user.posts
    return render_template("profile/profile.html", user = user, posts = posts)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/new-post', methods = ['GET', 'POST'])
@login_required
def new_post():
    form = NewPost()

    if form.validate_on_submit():
        content = form.content.data
        author = current_user.id
    
        post = Post(content=content, author=author)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('new_post.html', new_post_form = form)

@main.route('/new-post2', methods = ['GET', 'POST'])
@login_required
def new_post2():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        author = current_user.id

        # if 'image' in request.files:
        filename = photos.save(request.files['image'])
        path = f'img/uploads/{filename}'
        featured_img = path

        post = Post(title=title, featured_img=featured_img, content=content, author=author)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('new_post2.html')

@main.route('/post/<int:post_id>')
def view_post(post_id):
    '''
    View post function that returns the full post page
    '''
    comment_form = NewComment()

    post = Post.query.filter_by(id = post_id).first()
    comments = post.comments
    if post is None:
        abort(404)

    return render_template('view_post.html', post = post, comment_form = comment_form, comments = comments)

@main.route('/post/<int:post_id>/new-comment', methods = ['GET', 'POST'])
def new_comment(post_id):
    if request.method == "POST":
        author = request.form.get('author')
        content = request.form.get('content')
        post_id = post_id

        comment = Comment(author=author, content=content, post_id=post_id)

        db.session.add(comment)
        db.session.commit()

    return redirect(f'/post/{post_id}')

@main.route('/delete-post/<int:post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id = post_id).first()

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/delete-comment/<int:id>')
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id = id).first()
    post_id = comment.post_id

    db.session.delete(comment)
    db.session.commit()

    return redirect(f'/post/{post_id}')