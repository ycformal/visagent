Question: Is extensive construction taking place?

Reference Answer: no

Image path: ./sampled_GQA/410988.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is extensive construction taking place?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAEsAZAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/ADxraD/hJ5pJTshadxuHJPzHoO9dL8LLu1tdSubVpWEkyfIrIRnn2yBXLePJY5fEk7xurKXblTwea6X4TXUMF5eLLIqbk4yevIqupJ69XEa5x4wg94yP0Fdh9stz0lX86878c3bR6i89rMVkS2Yq6dVPFJaAzVu1HlnivLvE2iahqGr7rWymkUJjcFwo+Y9zxXpfw5vYbnQJJL+5WW6+0ON0zZbbgY6/jT9bniEzBCD9OlTNcyNKbszxseCdQIzcSwQD0zvP6cfrWZNPHpV3LaMDJ5eArAYLcc/SvTrphICc15T4gH/E+uPZz/IVg4pG7YyXVpQxaCCMHtvYmqE+p6o/8SIP9jFONRSnCmkkiW2X9Nnd7IGZy0m5sknNTswNZ+msGtcdwxq2alysy0tBDjNFBFFLmCx1njGE2/iq/Qk481iM/Wu0+ES/6fdP32EfyrlviGuzxbdnBG5iea6b4RyY1C4X1U/yFdi3OToewVw3j+1Rre4nI+YWcmD+VdxmuQ8ec6XPz1tJv/QaYMyvhW4j0C9Y/wDP1/7KKoa7dBr+4x3c/wA60PhLtfQb4MAR9pHX/dFc/wCIrqFNbu4jIit5rAKTg9e1S9io7lOWXK4zXmutHdr116bz/KvQHbivPdVOdYuT6uaxkbJ3KZqCY/KalY1XlPFJAyXTW2KPRiR+taZFcxI0kbZR2Uexpo1O9WTaLhiMdDg0Spt6oI1ElZnRkAnPX1orCGqXWOShPrsFFT7Nh7RHq/xGuYLjxNJJBIrhhk7Wzjir/wANNWttM1V3upkiRlwC5wM4rzxSDySScdzT8qQvGa6r63Oe2lj6SbxtoMSHzdTtV9NrZrkvFvjXRdTt/s1ldec5hlQkLgcocV46No/hH5UqygSAAgGjmDlO+8GeN7PwzYXFtcwXEjSyCQGIgDGMc0mq6pFqkz3DQgxzEuFcA4B5rgJbqOFh5kioCP4jiujjlD2luykEGNSCO/FTfQpLUkZIEB8maa2PpG2V/wC+TkVxt/n+0JtzbzuPzYx+ldRK/JrlLw5v5j7mspGqKzmq0lTO1VZHoQMikAIIqgRidh6AVbd6qPMkbsXzyccVaM2SgEjiimrPAV++PxNFMDZ+0Xp7hfotH+lt1mk/A4rWWFSM9acIV7VXKSY/2eZ+rufqxpVsmDAjr6+la2wDtQIx1FKwzLNiSckkn1JzXb2y7dOtF9IV/lXOFQPf8K6aL/jytv8Arkv8qARBL1NcpeH/AEqY+5/nXVSn5jXK3f8ArZT/AJ6ms5GqMqe7jUnMi/nVKS+j7Et9BVyTRXe3SaHncMlCf5GoILuSyJhlgDKvUbdrj/GnpbQnrqVTJPJ9yFsepqvPDOBl0yOvy81oXF8rqSJcA8jYuCPYioBqm2IAwhpP7x4/QVSb7EtLuZtFTPdO7Fisef8AcFFVqSd0j46GphKB3qkOlPycU7iLQlDdF/SgyHGBx9arqT60j9j7VI7kxOe9dLGf9Dtz/wBMl/lXJoxFdZCP9Btf+uS/ypoLlaQnca5W6PzSn/PeuudRuPFchddJazkaRZesji3iB6bRTrzTre7TEijPY9CPoaSz/wBTH/uj+VWs7XwOmKzW5b2ORv8ARJ7bLKDLGO6j5h9R3rHaPAOMEeor0T77SK3IU8e1c1r1vEkYmRAshbBYcZrWMrmUlY5vbRUwUEZI5oqyT//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is extensive construction taking place?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

