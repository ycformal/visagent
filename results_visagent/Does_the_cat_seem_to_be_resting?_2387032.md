Question: Does the cat seem to be resting?

Reference Answer: Yes, the cat is resting.

Image path: ./sampled_GQA/2387032.jpg

Program:

```
Does A seem to be <action>?
Program:
BOX0=LOC(image=IMAGE,object='cat')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Does the cat seem to be resting?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='cat')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAEsAZAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APPbh0WSJZFcIc73Udvb15xTBr8UVoEUxm4QgqnzFXA65xj+dR3s0c9tBt+WRsOoY4IBrEj066lu9kYGNzAZPUGsaceaCT6EJXR0I1dNTlhSeCzttoIMiBhuz65J/T1rGuV2XbxrhgTwVOcmtnStNfS7qa4u7u1ikhjP7p5lDOpBBCnBG7pj657VnarcvqviK61PyxGHkVii9FB4HTj/APXXbKhRVP2nN7z6XXe22/Z3No1J25baIuaajyXvlOvJibG4cdKmsY91nfh9wKAYJ7ip7zzY9Sa4hVGjgt/MlZlJVV4UkgdeSKyjqVzpkEkkloJILxmWOUA7ZFBxlD9e1UsNyxWutm7dbfdb8RuXO9Xa9u5a2AaFLIQwO88VDqMQihtRtGTHngc9e9JBqcB0mS0ubee2QvzJIp259N2OD7YpNUnguY4ZreZZFAK5HQe1ckpWjZo3jRTblGadtev6pGcwHofyqFxkdD+VI7N6j86daQy3l7BbJIFeVwoLHgfWpREmdHpHh65geR7lFBYDaAQferEumqqn5cH0I6V1kcRRQspV3CjJAwDWTqh8qCZxhfLjPJrojoYM4SdFa4lI4G4gfhRUTk5Hrjn60VXOSad1HLDasrKzxxEMhUD5VBwR7cEdawEQIOUk2t94bRn8K2ILa7yspuGQPGUKYzwfXPFSR6XJgHzETnIYZ9fTpWNOmktRbGZCssz/AGeLcsBcEgqMgnjNMnl2zyRqcMDgsPYf4iulnkgjgcI6F1QvtB/Ksy2toJdTtI9VjktomuAtxKExhOBn8+p7e5zTcVcuOzZveD/Fkmmyy3H2QXEzxrEdzAAKH3NwQRyOPatfWNRufFGp2122n2lvDaqRFGZCV+8COAQMjHbFYWt6bolld2baJ9ue1ldxcbt22MgZAV2A3cAnpUmnRz3FuWWSQDdgDrj8cV0qvK3Lyq9rX12++34BdKz3Oi8Q6tq2vaNNYan9mkiZlYMigMpBzkY6muAvLeC0gWGEMRvLMfcgf4V0VxbTpbSOZXO1ckYrGt4Ypy4uHlCO+3ZGck+g96wjQ503KVku/wB3RG8a61UYJX7X/VmfBpN7eqGtrKeVTnDKPl4689KsNp954fvbK7urQOAwfaG3Dg9CRwD3ruNN0pdPsbcwXN2gS7hk8p2G35mCnjHXmr3jfZF4evniUBnwrMOCcsB/j+dU6EYwUlK97/h6+pjKTvaxi23i7SpxiVpLV267xkfmKyta1+yukltbWYzPJwXUfKB9a5F+y5zkdcdKsrp8lmkU0kkTefFvQRvuIBOOcdD7VCbIbEZssT6mijaaKYHQ2ljPdahfW89wkUNpH5xYwl3Ke2COa6TSvDFvqEYji1CbdLEWUSWw54/3qzNY0W7uLiKezQmRoyjANgHBDDJ9DyKsSQeJbqMxCySAHjdHLtI+h3Vl7Kc72nb7irpdDH0wM2ozWckaTw+TJ5YSPZkjAPQE+vr7U2PR9dllt4JLW7msI3OwH5cL25OCPXmut07QpbAaQzoPNieXzsHOA6+v1AFdE7pEhdiOOQoPJ9qpuzKjexwn/CJagYG86Qzzu7TZXJBPbcxPzEZOPr9Kmjt77TbdYsSQA9iCMmuiXUZFuXMyIvACxkk7vy/w5qzHqSsi+ZAuOhRjkkH0zUqqkN0mzlpLm5aPbJOxQjBBzgisWOeKynBZSDHcFl2jkDAr1CCyjvGlVvKFsSDHCBtPHUsOvX+VcXrOkPdeILzy4nfEjM7LzhVCZOBycA9q3jJulP0X5oIxSkjYlfztMgnjYMjywEEDj/WLVzUbGLULZ7a5XzUfqCfyrGt7W8t7JIUKfZUmh3IyncCZRjBxz0/ya6mSEGTcV5IxnFK/+zx9X+URNe8zzW98IQxXXyXMnlA4KEDI49fSsO+VI7kwRRiNIf3YAz26k59zXqeoQxAFpUyqDf8AN7c15K0hknd2/jYt+ZzUIhoUAY6UU7FFUI759XtrmLY0c6jIPySbc/iDmr58Q2lvDveKUKg6DB/rXF295Hnlv0q1dCa+tAlqNyBsuSwHSsb9zaMW3qdQvjTTT/yxufxQH+tQ21/bapqi28CSqJWO0snI7nPNctDo9+VDLblwehVgf611PgzSp11rzboPCiQttbcByTjg/nRJRZ08sYxbR0Vxp1nptu09y0joiFmAYLwBngd/pWbF4s0uCV4rbRbySWNdzrGiMVHqSGNdJqsFtDouo+WgMhtZct95vuHv1rxbQ7m70HX4LiNSJoJNrx5xuHRl/EZropwpwpczim2+t/Ls0ckpybtc9cs9fa9itbgaZIsFxIsUc7OjAMxwAcHI9+KZpxW38U+fJBHKy38y4LkdYo8/5NULXUNIubuOPSFnjJv7eSSB12pndjIHY/Supn0OyupnnudNs5pX5ZmjBJ+pIya25qSp3a5ebtrs0+r/AFFrcx9dtxDHNKtr5JlvLc+WJg3lgSLgD9T9TVyWeJFJcSK3oUPP0xUv/CP6dFKkkemWSOpDKViwQfUGnyW7ls/dUdeck1jUnDkUIX0beum9vN9gSd7s5DxXqCw+HbkqrxvIojUOuCdxxx+Ga8q43D0Nej/EdJorCzTYoiaUlmUY5A4B/M15u3Ss1sTLcmBIFFRq4KjJ570UxEEd4Rjmuh0+/VIlTcOeTXFqTnrVuGaQdHNZuNzVVGeiWN5DAuyMBVJyQO5rcg1e6srC4vLG2W5kVkVozn7nJOMd+leYQXE2R+8Ndn4cuJfsTHecmQ/0qIws7jc7qx3Q1201fwpfz2wwDayqylcFW2HI9/rXL3vh17vxkIbX929/AJY3IBUNtw4Oeg4PI6Eir80rjRrxAcKLdwABgfdNcHJ4m1eWa1le8y9ucxN5aZXjHpXv5dlNbMaLVJpcr636ryT7GFSooPU9E0rSLzSLsw32Dtv7NFfaPUkgH0wRXoW5NvHSvDfDniDVbzWtPs7i8eWB71ZWVgCS2c5zjP617CkjZxntWOaZfUwHJRqNN6vT/hkOnNTu0XpMGPAxiqEzbSckD3qR3bBG41QumPBz1ryTUzfEGnx63pFxZnHmkboz6MOn+H414dMrRSPGwIZSQQfWvex8seR1Dda8e8axpF4rvBGoUFgxA9SAT/OqT0JkjnmK5oqJ/vmimQf/2Q==">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIACkAZAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APHtM/10aOQCg5z3U8/zrtGWN9KiA5Kt1AwB/LpiuOsRsvo8gbkyp5613DqraMkLKVI4G05x9c1pDVCej0OU8zGojawXk/hmupv7NU06O4Q8SjcCq9SvUE1yvku+qIsSnzPNAVQea1wlzq9jcWVzfPZNbk+TagYZyect04/SiDsmipK9jFJVb8I4AAk5z2rs1a1fSmKTxZAJA8znIrzWCVbbUo1vIGeOOQebDnBOOopL+eGe9kljtlhRmyEB6Cog+ROw5y5rGzqR8m+lUsD0OQOvFdboEK+SS+M7Rj+leaGfYRs5A7Hmup0TxklmwW5tkC4xkZI/LrTg0m2xSd0l2DxEjKVAUg7tuT3xWrYD9wmMl0Q/dPtVS6SPU18/eNhYsoXnjr/jWhZ+WY3YcEKcjPp/OtFvchvSxzOpHfdnOTknvVNtueA35VZvBvunI3YHr1qoyN/eP51zTfvM6qa91aBx2zRTNj9icUVIy88lp/bjNbJNFbOfkEpBbpzkjA65rqElMtotusqoF+Yruzk+hFcFc3M1wEkllZyo2jJ6D0rd0vUvPAjckOo2jnt9e9bU3ZWMKlnK6dztPB2jw3HilJXG8QRl1wMAEnHI9s1S1/4deKz4gvb2wjWZTMWicThW2k8cMe1df8OdPSz0y8125ICsjAMeyL1J/EV1HhjXLrWdOe6nSGOONygYHOcdevStHbZknEaT8PvJ8L6hJ4iW3hvr4o4l4keJUBJxjABzyeeleRaxawLdzPYl3slk8uN26nA6n69fxr33xN4i8LapZXNheT3HzAqxtgwBOPUYzj06V43p0GlwwMl6Jpt1yrlEXaCigjqemSf0qXJSA2PD/wAK7zXvDcOq2uoWxeb7sPPHOME+vtWxafBO5h3Pf36yDYfkgUjDe5PUVf0bxyul25trDToobVR+7jDdD6mtaP4jz3c8UN1DBaxNkPMGPy++MUKUewWPEdX0698P6xPp7yOjxHqGxkHkGqqajeROCLmUgHOC5wa7jx5JY6xrsctk7TKIgjybcbmyfzx61zUejQEfNuPvmpau9BEMV4bkM7cP3prSfWnGzFvMyowwQCOaRoie61jJe8dUJPlRH5lFL5Df3loosguyvjdGw9KZBI0c0bq2CD1o/wCev+5UcX3k/wB4Vp0Od7nead4p1IaI+lpcbLN2LSRYHU84zjOCecVNHf3FvA0MbSpHIwLqpODzxkd656w+8foa15PuRf8AXEf+hVUXdXCa5XYutCHfah3Z7Z6VYXQoZSSzKV3YCggHrUMH+vH+9/QVo2//ACz/AN5v61oQV/8AhHlZpGWUdMjJ4PXjH4daYmgguoaRcj7xx/h6Vox/8svqP5VI/wDrv+AN/ShgjBm04WzrIQGXk9OnpzWdIqeSxBAO8ZGP881u6j0k/wB0Vz83+tb8alsDKvBzuA46ZqmDnPzVdvf+PVP941QWsqiszopvQCeepopworJyLP/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the cat seem to be resting?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if True else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
