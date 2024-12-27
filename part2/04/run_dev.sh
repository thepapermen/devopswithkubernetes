#!/bin/bash
# Simple script to simultaneously run all three components of the system
# "the old way", i.e., natively, i.e. without Docker or Kubernetes.

cd todo-frontend
export HOST='127.0.0.1'
export PORT='3000'
export URL='/image'
export MEDIA_ROOT='../image-backend/'
export IMAGE_LIFE_MINUTES='0.1'
export IMAGE_SOURCE_URL='https://picsum.photos/1200'
../todo-backend/.venv/bin/python ../image-backend/serve_image.py &\
../todo-backend/.venv/bin/python ../todo-backend/todo/manage.py runserver &\
bun run dev
