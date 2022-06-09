# SpanTreeWebapp

A Spanning Tree represents nodes in a network, like devices in LAN.
It consists of vertices conected via edges.
A vertex has a name and a ID, edges go from one vertex to another and have a weight/cost.

For any given Vertices and Edges (given some restrictions) the algorithm computes every vertexes least expensive path to root.
The root vertex is that vertex, that has the lowest ID.

## Restrictions:
* lowest ID of vertices can only be given once, other IDs can be same as other vertices IDs
* edge can not go from vertex to same vertex
* no edge can be defined twice


## Website
Under 'new project' anyone can create Edges and Vertices and send this data to be computed by the algorithm.
If the algorithm computes successfully one will be redirected to the results page.

### Users
In order to save Spanning Trees as 'projects' a user can create an account and must log in with this account.
After creating a Spanning Tree, it can be saved to a database and the user can load these Spanning Tree projects from 'My Projects'

## How to run:
* Start Frontend Server on localhost:8080
  * inside frontend/spanningtree-fe run `npm run serve`
* Start Backend Server on localhost:5000
  * inside the project folder set up a virtual environment: `python -m venv Venv`
  * after the virtual env called Venv is creeated activate it via `Venv\Scripts\activate` 
  * install required packages inside the venv
    * `pip install flask`
    * `pip install flask-login`
    * `pip install flask_cors`
    * `pip install flask-sqlalchemy`
  * Run the server using by running the main file `python main.py`
