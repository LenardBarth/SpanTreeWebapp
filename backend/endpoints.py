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
# API for Spanning Tree Algorithm
@endpoints.route('/computeTree', methods=["POST"])
def computeTree():
    if request.method == 'POST':
        response_object = {"status": "success"}
        post_data = request.get_json()
        
        vrtcs = post_data.get('vrtcs')
        edges = post_data.get('edges')

        # make sure there is data to run algorithm with
        if vrtcs == []:
            response_object = {"status": "warning"}
            response_object['message'] = "Please create vertices first."
        elif edges == []:
            response_object = {"status": "warning"}
            response_object['message'] = "Please create edges."
        else:
            try:
                # let algorithm compute on given spanning tree and return results to frontend
                tree_result = evaluateSpanningTree(input_vertices=vrtcs, input_edges=edges)
                response_object['result'] = tree_result
                response_object['message'] = "Algorithm cpmleted successfully"
            except:
                response_object = {"status": "danger"}
                response_object['message'] = "Could not compute ideal Spanning Tree"

    return response_object

# Protected route for Users requesting all of his saved Spanning Tree projects
@endpoints.route('/getUserTrees/<userID>', methods=["GET"])
# @login_required   # throws inexplicable error so don't use this decorator
def getUserTrees(userID):
    if request.method == 'GET':
        response_object = {"status": "success"}
        user = User.query.filter_by(id=userID).first()
        # make sure user with given ID exists
        if user:
            # get all trees associated with this user
            trees = SpanningTree.query.filter_by(user_id=user.id).all()
            # make sure there are already existing projects
            if trees:
                # turn list of DB objects into list of JSON objects so frontend can handle them
                projects = []
                for tree in trees:
                    projects.append({"id": tree.id, "name": tree.name, "vertices": tree.vertices, "edges": tree.edges, "result": tree.result, "user_id": tree.user_id})
                response_object['projects'] = projects

    return response_object

# Protected route for Users saving a Spanning Tree project
@endpoints.route('/save', methods=["POST"])
# @login_required
def save_spanTree():
    if request.method == 'POST':
        response_object = {"status": "success"}
        post_data = request.get_json()

        treeID = post_data.get('tree_id')
        userID = post_data.get('user_id')
        nameStr = post_data.get('name')
        vrtcsStr = post_data.get('vrtcs')
        edgesStr = post_data.get('edges')
        resultStr = post_data.get('result')

        # ensure that there is data being sent
        if vrtcsStr == "":
            response_object = {"status": "warning"}
            response_object['message'] = "Please create vertices first."
        elif edgesStr == "":
            response_object = {"status": "warning"}
            response_object['message'] = "Please create edges."
        else:
            try:
                # check if treeID is taken, if so update existing tree with new data
                tree = SpanningTree.query.filter_by(id=treeID).first()
                if tree:
                    tree.vrtcs=vrtcsStr
                    tree.edges=edgesStr
                    tree.result=resultStr
                    response_object['message'] = "Updated!"
                    response_object['tree_id'] = tree.id
                # if treeID does not exist, create new tree
                else:
                    user = User.query.filter_by(id=userID).first()
                    newTree = SpanningTree(user_id=user.id, name=nameStr, vertices=vrtcsStr, edges=edgesStr, result=resultStr)
                    db.session.add(newTree)
                    response_object['message'] = "Saved new Spanning Tree project!"
                    response_object['tree_id'] = newTree.id
                db.session.commit()
            except:
                response_object = {"status": "danger"}
                response_object['message'] = "Could not save Spanning Tree"

    return response_object