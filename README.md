# Madison Square Park Lawns

Which lawns are open today? Here's an endpoint to find out

`/` - returns nothing right now (it will render what's in in `templates/index.html`) *Want to build a front-end? scroll to the bottom*

`/lawn-status` - returns a map `<lawn name>: <bool>`, bool is `True` if lawn is open


### Status Endpoint
```
http://127.0.0.1:5000/lawn-status
```

### Response
```
{
    "cherry":false,
    "farragut":false,
    "magnolia":true,
    "oval":false,
    "redbud":true,
    "sol_lewitt":true,
    "sparrow":true,
    "veterans":false
}
```

## Run this at home

Things you need:
- Python 3.7.3
- pip 19.1.1
- virtualenv 16.6.0

1. Clone the repo
```
git clone https://github.com/NatashaMitchko/msp_lawns.git
```

2. Setup and start your `virtualenv`
```
virtualenv --clear env
source env/bin/activate
```

3. Install requirements
```
pip install -r requirements.txt
```

4. Run it
```
python server.py
```

## Build a Front-End for this Project

There are three blank files:
- `templates/index.html`
- `static/main.css`
- `static/main.js`
where you can put your front end code.