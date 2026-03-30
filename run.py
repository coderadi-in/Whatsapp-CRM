'''coderadi &bull; Run file for the project in dev server.'''

# ? IMPORTS
from main import server

# ! RUN
if (__name__ == "__main__"):
    server.run(debug=True, host='0.0.0.0')