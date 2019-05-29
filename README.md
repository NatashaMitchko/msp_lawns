# Madison Square Park Lawns

Which lawns are open today? Here's an endpoint to find out

`/` - returns nothing right now (it will render what's in in `templates/index.html`)

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