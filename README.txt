hipchatpy
=========

hipchatpy is `HipChat`_ client library for specific logging.

Install
-------

.. code:: python

    pip install hipchatpy

Dependencies
------------

-  requests

Sample Code
-----------

.. code:: python

    import hipchatpy

    AUTH_TOKEN = 'hogehoge'
    ROOM_ID = 10000

    # Create a new instance.
    logging = hipchatpy.HipChatLogging(AUTH_TOKEN, ROOM_ID)

    # LogLevel: INFO
    logging.info(message='INFO Message')

    # LogLevel: WARN
    logging.warn(message='WARN Message')

    # LogLevel: ERROR
    logging.error(message='ERROR Message')

Correspondence table
~~~~~~~~~~~~~~~~~~~~

+-----------+---------------+----------+----------+
| Method    | LogLevel      | Notify   | Color    |
+===========+===============+==========+==========+
| info()    | INFO (1)      | False    | green    |
+-----------+---------------+----------+----------+
| warn()    | WARNING (2)   | True     | yellow   |
+-----------+---------------+----------+----------+
| error()   | ERROR (3)     | True     | red      |
+-----------+---------------+----------+----------+

Command line
------------

.. code:: sh

    export HIPCHAT_TOKEN=your_api_token

    # LogLevel: INFO
    hipchatpy -r 10000 -m 'INFO Message' -l 1

    # LogLevel: WARN
    hipchatpy -r 10000 -m 'WARN Message' -l 2

    # LogLevel: ERROR
    hipchatpy -r 10000 -m 'ERROR Message' -l 3

.. _HipChat: https://www.hipchat.com