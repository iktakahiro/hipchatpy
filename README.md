# hipchatpy

Simple [HipChat](https://www.hipchat.com) client library.

## Install

```python
pip install hipchatpy
```

## Dependencies

- requests

## Sample

```python
import hipchatpy

AUTH_TOKEN = 'hogehoge'

# Create a new instance.
client = hipchatpy.HipChatClient(AUTH_TOKEN)

# Create a room.
client.create_room(name='Test_ROOM', owner_user_id=10000):

# Send a message.
client.send_message(room_id=10000, message_from='hipchatpy', message='Test Message')

# Send a message (Back ground Color = Red).
client.send_message(room_id=10000, message_from='hipchatpy', message='Alert', color='red')

# Get list rooms for your group.
client.get_room_list()
```

