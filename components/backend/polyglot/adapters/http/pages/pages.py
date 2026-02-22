from flask import Blueprint, jsonify, render_template, request


def create_app_pages(bp_pages: Blueprint, ):

    @bp_pages.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    return bp_pages
