# coding=utf-8
from . import snp
from flask import render_template


@snp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@snp.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500