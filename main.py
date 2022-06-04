"""Module description
   * this script runs the application

   author: 7056674
   date: 04.06.2022
   version: 0.0.1
   license: free
"""

from backend import create_app

app = create_app()


if __name__== '__main__':
    app.run(debug=True)