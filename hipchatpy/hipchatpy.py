#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Takahiro Ikeuchi'

import requests
from copy import deepcopy

BASE_URI = "https://api.hipchat.com/v1/"
AUTH_TOKEN = ''


class HipChatClient:

    def __init__(self, base_uri=BASE_URI, auth_token=AUTH_TOKEN, response_format='json'):

        self.base_uri = base_uri
        self.auth_token = auth_token
        self.response_format = response_format

        self.base_params = {
            "auth_token": self.auth_token,
            "format": self.response_format
        }

    def post(self, params, endpoint):

        __params = deepcopy(params)
        __params.update(self.base_params)

        uri = self.base_uri + endpoint

        http = requests.session()
        response = http.post(uri, params=__params)
        http.close()

        return response

    def get(self, params, endpoint):

        __params = deepcopy(params)
        __params.update(self.base_params)

        uri = self.base_uri + endpoint

        http = requests.session()
        response = http.get(uri, params=__params)
        http.close()

        return response

    def create_room(self, name, owner_user_id, privacy='private', guest_access=0):
        """Creates a new room.

        Args:
            name:
            owner_user_id:
            privacy:
            guest_access:

        Returns:
            response:

        Raises:
            TODO:

        """

        params = {
            "name": name,
            "owner_user_id": owner_user_id,
            "privacy": privacy,
            "guest_access": guest_access
        }

        response = self.post(params, 'rooms/create')

        return response

    def delete_room(self, room_id):
        """Deletes a room and kicks the current participants.

        Args:
            room_id:

        Returns:
            response:

        Raises:
            TODO:

        """

        params = {
            "room_id": room_id
        }

        response = self.post(params, 'rooms/delete')

        return response

    def get_room_history(self, room_id, date='recent', timezone='Asia/Tokyo'):
        """Fetch chat history for this room.

        Args:
            room_id:
            date:
            timezone:

        Returns:
            response:

        Raises:
            TODO:

        """

        params = {
            "room_id": room_id,
            "date": date,
            "timezone": timezone
        }

        response = self.get(params, 'rooms/history')

        return response

    def get_room_list(self):
        """List rooms for this group.

        Args:
            Nothing

        Returns:
            response:

        Raises:
            TODO:

        """

        params = {}

        response = self.get(params, 'rooms/list')

        return response

    def send_message(self, room_id, message_from, message, message_format='html', notify=0, color='yellow'):
        """Send a message to a room.

        Args:
            room_id: ID or name of the room.
            from: Name the message will appear be sent from.
            message: The message body. 10,000 characters max.
            message_format: Determines how the message is treated by our server and rendered inside HipChat applications.
            notify: Whether or not this message should trigger a notification for people in the room.
            color: Background color for message.
                   One of "yellow", "red", "green", "purple", "gray", or "random". (default: yellow)

        Returns:
            response:

        Raises:
            TODO:

        """

        params = {
            "room_id": room_id,
            "from": message_from,
            "message": message,
            "message_format": message_format,
            "notify": notify,
            "color": color
        }

        response = self.post(params, 'rooms/message')

        return response

    def set_topic(self, room_id, topic, topic_from='API'):
        """Set a room's topic.

        Args:
            room_id: ID or name of the room.
            topic: The topic body. 250 characters max
            from: Name of the service changing the topic.


        Returns:
            response:

        Raises:
            TODO:

        """

        params = {
            "room_id": room_id,
            "topic": topic,
            "from": topic_from,
        }

        response = self.post(params, 'rooms/topic')

        return response

    def get_room_details(self, room_id):
        """Get room details.

        Args:
            room_id: ID or name of the room.

        Returns:
            response:

        Raises:
            TODO:

        """

        params = {"room_id": room_id}

        response = self.get(params, 'rooms/show')

        return response
