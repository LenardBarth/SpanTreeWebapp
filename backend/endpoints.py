from flask import Blueprint, request
from flask_login import login_required, current_user
from . import db
from .db_models import SpanningTree, User
from .evaluateSpanningTree import evaluateSpanningTree


"""Module description
   * this script sets up routes for all APIs concerning the Spanning Tree workflow
   * flask, flask_login are installed in venv
   * other imports are from within directory

   author: 7056674
   date: 04.06.2022
   version: 0.0.1
   license: free
"""


endpoints = Blueprint('endpoints', __name__)


# -- Defining routes --
@endpoints.route('/computeTree', methods=["POST"])
def computeTree():
    response_object = {"status": "success"}
    if request.method == 'POST':
        post_data = request.get_json()
        
        vrtcs = post_data.get('vrtcs')
        edges = post_data.get('edges')

        try:
            tree_result = evaluateSpanningTree(input_vertices=vrtcs, input_edges=edges)
            response_object['result'] = tree_result
        except:
            response_object = {"status": "danger"}
            response_object['message'] = "Could not compute ideal Spanning Tree"


    return response_object

# Protected routes for Users that save Spanning Tree to database
@endpoints.route('/getUserTrees/<user_id>', methods=["GET"])
@login_required
def getUserTrees(user_id):
    response_object = {"status": "success"}
    if request.method == 'GET':
        user = User.query.filter_by(id=user_id).first()
        if user:
            trees = SpanningTree.query.filter(user_id=current_user.id).all()
            if trees:
                print(trees)
    return response_object

@endpoints.route('/getSpanningTree/<tree_id>', methods=["GET"])
@login_required
def getSpanningTree(tree_id):
    response_object = {"status": "success"}
    if request.method == 'GET':
        tree = SpanningTree.query.filter_by(id=tree_id).first()
        if tree:
            print(tree)
    return response_object

@endpoints.route('/save', methods=["POST"])
@login_required
def save_spanTree():
    response_object = {"status": "success"}
    if request.method == 'POST':
        post_data = request.get_json()

        treeID = post_data.get('tree_id')
        vrtcsStr = post_data.get('vrtcs')
        edgesStr = post_data.get('edges')
        resultStr = post_data.get('result')

        try:
            tree = SpanningTree.query.filter_by(id=treeID).first()
            if tree:
                tree.vrtcs=vrtcsStr
                tree.edges=edgesStr
                tree.result=resultStr
            else:
                newTree = SpanningTree(user_id=current_user, vrtcs=vrtcsStr, edges=edgesStr, result=resultStr)
                db.session.add(newTree)
            db.session.commit()
            response_object['message'] = "Saved!"
        except:
            response_object = {"status": "warning"}
            response_object['message'] = "Could not save Spanning Tree"

    return response_object