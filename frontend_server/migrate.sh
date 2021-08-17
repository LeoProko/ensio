source configure_environment.sh
PRIVATE_DIR="$PRIVATE_DIR" python3 manage.py makemigrations

source configure_environment.sh
PRIVATE_DIR="$PRIVATE_DIR" python3 manage.py migrate
