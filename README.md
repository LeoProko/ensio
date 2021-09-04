# Proko Engine

## Start up the server
- Run ``make_private_dir.sh`` to create the `ensio_private` directory, where the database and the secret key will be located
```bash
./make_private_dir.sh
```

- Add to `ensio_private/secret_key` your django secret key. To generate a random secret key, run the following code
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

- Install all necessary extensions
```bash
./install_requirements.sh
```

- Go to the `frontend_server` directory and add the necessary hosts to your machine. This is needed to run subdomains like docs.leoproko.io, shop.leoproko.io, etc,
```bash
cd frontend_server
./add_hosts.sh
```

- Start up the server
```bash
./run_server.sh
```

## Shop
Required photo size for homepage - **vertical 4x5**
