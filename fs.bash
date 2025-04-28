#!/bin/bash

# Set the base directory name
BASE_DIR="prompt_assistant_backend"

# Create the main project directory
mkdir -p $BASE_DIR

# Define subdirectories to create
SUBDIRS=(
  "$BASE_DIR/app/api"
  "$BASE_DIR/app/services"
  "$BASE_DIR/app/models"
  "$BASE_DIR/app/core"
  "$BASE_DIR/app/utils"
)

# Create subdirectories
for DIR in "${SUBDIRS[@]}"; do
  mkdir -p $DIR
done

# Define files to create with sample content
FILES=(
  "$BASE_DIR/app/api/prompt_routes.py"
  "$BASE_DIR/app/api/healthcheck.py"
  "$BASE_DIR/app/services/prompt_classifier.py"
  "$BASE_DIR/app/services/question_generator.py"
  "$BASE_DIR/app/services/prompt_builder.py"
  "$BASE_DIR/app/models/prompt_request.py"
  "$BASE_DIR/app/models/session_data.py"
  "$BASE_DIR/app/core/config.py"
  "$BASE_DIR/app/core/redis.py"
  "$BASE_DIR/app/core/llm_client.py"
  "$BASE_DIR/app/core/exceptions.py"
  "$BASE_DIR/app/utils/text_cleaner.py"
  "$BASE_DIR/app/utils/session_utils.py"
  "$BASE_DIR/main.py"
  "$BASE_DIR/requirements.txt"
  "$BASE_DIR/README.md"
)

# Create files and add placeholder content
for FILE in "${FILES[@]}"; do
  echo "# Placeholder content for $FILE" > $FILE
done

echo "Project structure created successfully!"
