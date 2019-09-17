from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response
from app.extensions import db
from flask_login import current_user
from app.forms import CommentForm, AdminCommentForm
from . import web
from app.models import Post,Category,Comment

