# -*- coding: utf-8 -*-

import redis


class Redis:
    def __init__(self, host, port, password, db, pool_size, decode_response=True, socket_connect_timeout=10,
                 socket_keepalive=60, ssl=True):
        self.__host = host
        self.__port = port
        self.__password = password
        self.__db = db
        self.__max_connections = pool_size
        self.__decode_responses = decode_response
        self.__socket_connect_timeout = socket_connect_timeout
        self.__socket_keepalive = socket_keepalive
        self.__ssl = ssl


    @property
    def conn(self):
        return redis.Redis(host=self.__host, port=self.__port, password=self.__password, db=self.__db,
                           socket_connect_timeout=self.__socket_connect_timeout,
                           socket_keepalive=self.__socket_keepalive,
                           max_connections=self.__max_connections,
                           decode_responses=self.__decode_responses,
                           ssl=self.__ssl,
                           # ssl_ca_certs="ca.crt",
                           )
