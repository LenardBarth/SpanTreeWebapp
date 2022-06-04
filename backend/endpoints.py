from flask import Blueprint, request
from flask_login import login_required, current_user
from . import db
from .db_models import SpanningTree, User
from .evaluateSpanningTree import evaluateSpanningTree

endpoints = Blueprint('endpoints', __name__)


# -- Defining routes --
@endpoints.route('/computeTree', methods=["POST"])
def computeTree():
    response_object = {"status": "success"}
    if request.method == 'POST':
        post_data = request.get_json()
        
        vrtcs = post_data.get('vrtcs')
        edges = post_data.get('edges')

        print("vrtcs", vrtcs)
        print("edges", edges)

        evaluateSpanningTree(input_vertices=vrtcs, input_edges=edges)
        try:
            tree_result = evaluateSpanningTree(input_vertices=vrtcs, input_edges=edges)
            response_object['message'] = tree_result
        except:
            response_object = {"status": "error"}
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



# Routes for Vertices
# @endpoints.route('/getVertices', methods=["GET"])
# def getVertices():
#     response_object = {"status": "success"}
#     return response_object

# @endpoints.route('/newVertex', methods=["POST"])
# def newVertex():
#     response_object = {"status": "success"}
#     return response_object

# @endpoints.route('/updateVertex', methods=["PUT"])
# def updateVertex():
#     response_object = {"status": "success"}
#     return response_object

# @endpoints.route('/deleteVertex', methods=["REMOVE"])
# def deleteVertex():
#     response_object = {"status": "success"}
#     return response_object

# Routes for Edges
# @endpoints.route('/getEdges', methods=["GET"])
# def getEdges():
#     response_object = {"status": "success"}
#     return response_object

# @endpoints.route('/newEdge', methods=["POST"])
# def newEdge():
#     response_object = {"status": "success"}
#     return response_object

# @endpoints.route('/updateEdge', methods=["PUT"])
# def updateEdge():
#     response_object = {"status": "success"}
#     return response_object

# @endpoints.route('/deleteEdge', methods=["REMOVE"])
# def deleteEdge():
#     response_object = {"status": "success"}
#     return response_object