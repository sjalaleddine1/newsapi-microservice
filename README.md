**newsAPI**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**how to REQUEST data** 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To request Data, you must first run the server.py file locally on your computer. Then using ZMQ for Javascript, you can make a request using sockets and sending a json
of the country and news outlet. 

**how to RECEIVE data**
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The data can be recieved in a JSON object when the socket that is connected to the server.py receives the message. The data will be received as a JSON containing
the title, description, and url of the article

**UML sequence diagram**
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91445581/199154229-1564b469-9016-4991-b89e-7264d82d5ffc.png)
