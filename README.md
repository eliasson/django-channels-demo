# Django Channels Demo

A tiny Django setup with
[Django Rest Framework](http://www.django-rest-framework.org/) and
[Django Channels](http://channels.readthedocs.org/en/latest/).

This Django project was used as a small demonstration at the Geek Beer Tuesday
meetup. It is not meant to be practical or even to make sense, it is just to
combine the the features in DRF and Django Channels


## Getting started

Make sure you got Python3 installed in your
[virtualenv](https://docs.python.org/3/library/venv.html) and then run:

    # Install the needed third-parties
    $ make init

    # Add a super user to login with
    $ python manage.py createsuperuser

    # Add some nonsense Foos and Bars
    $ python manage.py test_data

    # Run the server
    $ make run

Now you should have a server running on port http://localhost:8000


### Available resources

#### Standard server-side templates

The root page at http://localhost:8000/ is just a list of the existing Foo's
in the database (those created with `python manage.py test_data` command).


#### Django Admin

The standard Django Admin is available at http://localhost:8000/admin
(login using the account created with `python manage.py createsuperuser`).

Here you can browse the available models.


#### Django REST framework

The browsable API generated form Django REST framework is available under
http://localhost:8000/api (in order to create or update objects you need to be
logged in).

The actual JSON API is available under the same URL (using content negotiation)
by running the `http` tool:

    $ http http://localhost:8000/api/foo/


#### Django channels

You can access the Django Channels from the root URL http://localhost:8000.

1. You need up open the Browser Developer console

2. Inject these two lines of JavaScript to initiate a WebSocket connection:

        var ws = new WebSocket("ws://localhost:8000/ws");
        ws.onmessage = function (event) { console.log(event.data); }

3. Optionally, do step 1-2 in another browser window

4. Send some messages using

        ws.send("Hello, World!");

5. You sound now se the message popping up in all browser windows. As well as
   be visible in Django Admin at http://localhost:8000/admin/demo/chatmessage/
   and via the REST API at http://localhost:8000/api/chat/

That's it!


### Implementation

The files of most interests are:

| File             | Description                                         |
| -----------------|-----------------------------------------------------|
| demo/models.py   | Implements all database models                      |
| demo/rest.py     | Implements the DRF serializers and view             |
| demo/channels.py | Implements the Channel consumers and setups routing |
| acme/settings.py | Adds and configures DRF and Channels apps           |


## License

Released under MIT, see LICENSE for details
