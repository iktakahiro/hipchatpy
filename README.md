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
auth_token = 'hogehoge'

room_id = 10000
message_from = 'hipchatpy'
message = 'Test Message'

# Send a message.
client = HipChatClient(auth_token)
client.send_message(room_id, message_from, message)

# Get list rooms for your group.
client = HipChatClient(auth_token)
client.get_room_list()
```

