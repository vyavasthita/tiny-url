#!/bin/sh

NAME=fastapi-template
WORKERS=1
WORKER_CLASS=uvicorn.workers.UvicornWorker
LOG_LEVEL=error

gunicorn main:app --workers $WORKERS --worker-class $WORKER_CLASS --bind 0.0.0.0:5001
