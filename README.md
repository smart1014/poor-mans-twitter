# poor-mans-twitter
Poor Man's Twitter using Django and VUE

### Technical Stacks
* **`Django 3.2`**
* **`DRF 3.14`**
* **`Vue3`**

### Configuring and Running Site on Local

##### 1. First, Create virtualenv

```bash
virtualenv venv
```

##### 2. Activate virtualenv

```bash
source venv/bin/activate
```

##### 3. Install python packages

```bash
pip install -r requirements.txt
```

##### 4. Run Database Migration
```bash
python manage.py migrate
```

##### 5. Launch Site locally
```bash
python manage.py runserver
```

### Static web page built by Vue3
You can see it in **`static/index.html`**