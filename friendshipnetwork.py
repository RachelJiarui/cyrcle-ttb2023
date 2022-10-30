from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/getfriends")
def hello_world():
    g = Graph(7) # 1 user, 3 friends, each with 1 secondary friend
    # xx u0 f1 f2 f3 s4 s5 s6
    # u0  0  1  1  1  2  2  2
    # f1  1  x  x  x  1  0  0
    # f2  1  x  x  x  0  1  0
    # f3  1  x  x  x  0  0  1
    # s4  2  1  0  0  x  x  x
    # s5  2  0  1  0  x  x  x
    # s6  2  0  0  1  x  x  x

    g.add_immediate_friend(0, 1)
    g.add_immediate_friend(0, 2)
    g.add_immediate_friend(0, 3)
    g.add_immediate_friend(1, 4)
    g.add_immediate_friend(2, 5)
    g.add_immediate_friend(3, 6)

    g.add_secondary_friend(0, 4)
    g.add_secondary_friend(0, 5)
    g.add_secondary_friend(0, 6)

    #g.print_matrix()

    friend4 = {
        "id": 4,
        "name": "William",
        "location": "Boston, MA",
        "interests": ["soccer", "juice"],
        "mutual_id": 1
    }

    friend5 = {
        "id": 5,
        "name": "Josh",
        "location": "Boston, MA",
        "interests": ["laughing", "girls"],
        "mutual_id": 2
    }

    friend6 = {
        "id": 6,
        "name": "Babeliette",
        "location": "Syracuse, NY",
        "interests": ["Rachel", "Chester"],
        "mutual_id": 3
    }

    # returning this
    friend_dict = {
        "4": friend4,
        "5": friend5,
        "6": friend6
    }

    # results = g.matrix_to_string()

    return friend_dict 

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_immediate_friend(self, v1, v2):
        if v1 == v2:
            #print("Same vertex %d and %d" % (v1, v2))
            return False
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        return True
    
    def add_secondary_friend(self, v1, v2):
        if v1 == v2:
            #print("Same vertex %d and %d" % (v1, v2))
            return False
        self.adjMatrix[v1][v2] = 2
        self.adjMatrix[v2][v1] = 2
        return True

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            #print("No edge between %d and %d" % (v1, v2))
            return False
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        return True

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print

    def matrix_to_string(self):
        str_matrix = ""

        for row in self.adjMatrix:
            for val in row:
                str_matrix += str(val)
        
        return str_matrix


def main():
    g = Graph(7) # 1 user, 3 friends, each with 1 secondary friend
    # xx u0 f1 f2 f3 s4 s5 s6
    # u0  0  1  1  1  2  2  2
    # f1  1  x  x  x  1  0  0
    # f2  1  x  x  x  0  1  0
    # f3  1  x  x  x  0  0  1
    # s4  2  1  0  0  x  x  x
    # s5  2  0  1  0  x  x  x
    # s6  2  0  0  1  x  x  x

    g.add_immediate_friend(0, 1)
    g.add_immediate_friend(0, 2)
    g.add_immediate_friend(0, 3)
    g.add_immediate_friend(1, 4)
    g.add_immediate_friend(2, 5)
    g.add_immediate_friend(3, 6)

    g.add_secondary_friend(0, 4)
    g.add_secondary_friend(0, 5)
    g.add_secondary_friend(0, 6)

    g.print_matrix()

if __name__ == '__main__':
    main()