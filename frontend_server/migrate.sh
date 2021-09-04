#source configure_environment.sh
#PRIVATE_DIR="$PRIVATE_DIR" python3 manage.py makemigrations
#PRIVATE_DIR="$PRIVATE_DIR" python3 manage.py migrate

python3 manage.py makemigrations
python3 manage.py migrate
