
# CTeeth backend

This project implements the API for CTeeth.

## Getting started with development

1. Install git (and Git Bash if on Windows)
2. Install VSCode
3. Set up your Github SSH keys
4. Clone the repo and start VSCode:

       $ git clone git@github:cteeth-uw/backend
       $ cd backend
       $ code .

5. Install the miniconda Python environment manager according to the [installation docs](https://www.anaconda.com/docs/getting-started/miniconda/install)
6. Create a new conda environment for this project, and install the dependencies:

       $ conda create -n cteeth python=3.12
       $ conda activate cteeth
       $ pip install poetry
       $ poetry install

7. In VSCode, set the Python Interpreter setting to point to the new environment: press `Ctrl+Shift+P`, type
   `Python: Select Interpreter` and press Enter, then choose the new `cteeth` conda environment.
8. The `poetry install` command should have installed the `cteeth-api` package and a command line
   script `cteeth-api`. In a terminal in which you've already done a `conda activate cteeth`, start the server:

       $ cteeth-api

   Hopefully you'll see some messages related to the server starting up and listening for requests.
9. If `curl` is not installed on your system, install it with scoop:

       $ scoop install curl

10. Use curl to send a request to the API:

       $ curl http://127.0.0.1:8000/scans

   You should get a (fake) list of scans available from the server.
