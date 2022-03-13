from flask import render_template, redirect, url_for, abort
from . import main
from ..models import User, Post
from .forms import NewPost, UpdateProfile
from .. import db
from flask_login import login_required, current_user
from ..requests import get_quote

# Views
@main.route('/')
def index():
    title = 'This is Me'
    random_quote = get_quote()

    return render_template('index.html', title = title, quote = random_quote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    
    return render_template("profile/profile.html", user = user)

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