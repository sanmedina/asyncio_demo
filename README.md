asyncio Demo
=====

A small demo to compare the behavior of a synchronous application with an
asynchrounous one.

# Basic Concepts

The `basics/` directory has some scripts to show an overview on how to work
with asynchronism in Python.

# Web App Demo

There are four components:

- `blocking_resource`: Represents a blocking resource. It is a FastAPI
  resource that has service called `/blocking-resource`. That service 
  takes 5 seconds to respond.
- `sync_flask`: The synchronous application. It is a simple Flask
  application that consumes `/blocking-resource`.
- `async_fastapi`: The asynchronous application. It is a FastAPI
  application that also consume the single service of `blocking_resource`.
- `run_clients.py`: A script the simulates an N number of clients that
  consumes one of the applications. By default, it runs four clients.

They way to run each components is as the following (everything is done with
the virtual environment activated):

First, run the `blocking_resource` by running the `run.sh` script inside
its directory.

```console
(venv) /blocking_resource$ ./run.sh  # will run on port 8000
```

Then run both applications in separate terminals. Each application also
have a `run.sh` script. Note that the Flask application by default runs
four workers. If you want a different the number, pass the desire number
of workers to the run script.

```console
# Flask app
(venv) /sync_flask$ ./run.sh  # will run on port 8001; runs 4 workers by default
(venv) /sync_flask$ ./run.sh 10  # if you want to run 10 workers
# FastAPI app
(venv) /async_fastapi$ ./run.sh  # will run on port 8002
```

Finally, run `run_clients.py` against the desire application.

```console
(venv) $ ./run_clients.py 8001  # consume Flask app
(venv) $ ./run_clients.py 8002  # consume FastAPI app
# if you want different number of clients than 4, use the -n flag
(venv) $ ./run_clients.py 8001 -n 10
```

# References

- [Official docs](https://docs.python.org/3/library/asyncio.html)
- [asyncio playlist](https://www.youtube.com/playlist?list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB)
- [Node.js success case](https://hackernoon.com/how-netflix-and-paypal-did-product-transformation-using-node-js-22074e13caad)
- [FastAPI – The Good, the Bad and the Ugly](https://www.infolytx.com/fast-api-gbu/)
