# How to run the solution

Run this command in the terminal

`python app.py `

# How to start the ngrock server

### Download the ngrock framework 

[Download NGROCK for windows](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip)

### Launch the flask app 

```
flask run --host=0.0.0.0 --port=5000
```

### Launch the ngrock app after unzip the file

Copy the url of the flask app 

And launch the following command : 

`ngrok http --domain=ostrich-driven-duly.ngrok-free.app http://192.168.1.44:5000`

you can replace with the url actually use : `http://192.168.1.44:5000`
