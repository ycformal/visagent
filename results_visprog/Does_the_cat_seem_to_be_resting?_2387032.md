Question: Does the cat seem to be resting?

Reference Answer: Yes, the cat is resting.

Image path: ./sampled_GQA/2387032.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Does the cat seem to be resting?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAEsAZAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APPbh0WSJZFcIc73Udvb15xTBr8UVoEUxm4QgqnzFXA65xj+dR3s0c9tBt+WRsOoY4IBrEj066lu9kYGNzAZPUGsaceaCT6EJXR0ceqf2xPDFJbWsDKCN8avls4xnk/p61jXsEltfyQOhVsg4Iwea6Lw3Zro9zfS6jf29qwt9oUsrO3OcIegb5QB9c9qzPEN8db8Tz6mm4p+7HK7SB0GQOPxrRwipX6s3jOXLboh+mo8l75TryYmxuHHSprGPdZ34fcCgGCe4q3OGi1T7WsYkt7e33zE8BV4BJx7kViSahfabbSSG1V4Lxysc2wlJFBxlDn17VooqNl2FKbld9y5sA0KWQhgd54qHUYhFDajaMmPPA5696bb6lEdCksrqGa3Yyf690OzPpnHX2pmqXUN00LW8yyKseCR2NKVlAIu8yiwHofyqFxkdD+VI7N6j86daQy3l7BbJIFeVwoLHgfWskayZ0ekeHrmB5HuUUFgNoBB96sS6aqqflwfQjpXWRxFFCylXcKMkDANZOqHyoJnGF8uM8muiOhgzhJ0VriUjgbiB+FFROTkeuOfrRVc5Jp3UcsNqysrPHEQyFQPlUHBHtwR1rARAg5STa33htGfwrYgtrvKym4ZA8ZQpjPB9c8VJHpcmAfMROchhn19OlY06aS1FsZkKyzP9ni3LAXBIKjIJ4zTJ5ds8kanDA4LD2H+IrpZ5II4HCOhdUL7QfyrMtraCXU7SPVY5LaJrgLcShMYTgZ/Pqe3uc03FXLjs2dP4L8Wx2EM8ksLy3TlI+QCnlg5fg9zwK0ddvpvE2pW14lnaxR2oIiiLttAyCDjIGRjsBXP63puiWV3Zton257WV3Fxu3bYyBkBXYDdwCelSadHPcW5ZZJAN2AOuPxxVK97MTtbQ6HxDq+sa9o0thqYtZImZWDIAGUg5yMdTXnl1ZQ2h/dKcHhjnvXT3FtOltI5lc7VyRismCGGVSLgybJGxtQ5YnPA96me2pVPV3MyDSb69UNbWU8qnOGUfLx156VYbT7zw/e2V3dWgcBg+0NuHB6EjgHvXpPhvSre3so7dBKAswnAkJypxg0zxuUi8O3zxKAz7VZhwTlgP8fzpRimrjm3fQxbbxdpU4xK0lq7dd4yPzFZWta/ZXSS2trMZnk4LqPlA+tci/Zc5yOuOlWV0+SzSKaSSJvPi3oI33EAnHOOh9qpNmbYjNlifU0UbTRTA6G0sZ7rUL63nuEihtI/OLGEu5T2wRzXSaV4Yt9QjEcWoTbpYiyiS2HPH+9WZrGi3dxcRT2aEyNGUYBsA4IYZPoeRViSDxLdRmIWSQA8bo5dpH0O6svZTne07fcVdLoY+mBm1GazkjSeHyZPLCR7MkYB6An19famx6PrsstvBJa3c1hG52A/Lhe3JwR6811unaFLYDSGdB5sTy+dg5wHX1+oArondIkLsRxyFB5PtVN2ZUb2OE/4RLUDA3nSGed3abK5IJ7bmJ+YjJx9fpU0dvfabbrFiSAHsQRk10S6jIty5mRF4AWMknd+X+HNWY9SVkXzIFx0KMckg+malVUhuk2ctJc3LR7ZJ2KEYIOcEVkmaOxkgLIRskLptHOD3/SvTILKO8aVW8oWxIMcIG08dSw69f5VzXivRWuNZhMUTyZt98hHOFVsE7RycA9qU5yaHCKTNfTnMsMdxE4KugIKjim6jYxahatbXK+Yj9Rn8qqaDa3sGIYvLNqgyyOpDDJPIOOen9OtbbwgyBivJGM4oi9BSWp5re+EIYrr5LmTygcFCBkcevpWHfKkdyYIoxGkP7sAZ7dSc+5r1PUIYgC0qZVBv+b25ryVpDJO7t/Gxb8zmtEZtCgDHSinYoqhHfPq9tcxbGjnUZB+STbn8Qc1fPiG0t4d7xShUHQYP9a4u3vI88t+lWroTX1oEtRuQNlyWA6VjfubRi29TqF8aaaf+WNz+KA/1qG2v7bVNUW3gSVRKx2lk5Hc55rlodHvyoZbcuD0KsD/AFrqfBmlTrrXm3QeFEhba24DknHB/OiSizp5Yxi2jpv7ItbZk8+R2DccsFx+HU/QVSfxHo1jdyW1pYz3MsQzJ5EO7aPUnOa6Oa0h+zTxW423EkTIsg+ZgSCAc9a8P0ae88PeIopkUie2lKSR5xuA4Zfx5pRijmlNnt1lcLqNpFd2/wBnkjcZRwTn6dOD6imSD7P4g0m4kt45mVpFxuI4I57foaoeHNR0m5vruPR0njJ/eSwONqA5xuAPQ/Suk2z4O4Kc/wAKngfpTEZb2pgu7qVbJojK+fKEobywOw/U/U1DLPEikuJFb0KHn6YrUkikJz8o9gTVOS3ctn7qjrzkmncDkPFeoLD4duSqvG8iiNQ64J3HHH4ZryrjcPQ16P8AEdJorCzTYoiaUlmUY5A4B/M15u3SrWxnLcmBIFFRq4KjJ570UxEEd4Rjmuh0+/VIlTcOeTXFqTnrVuGaQdHNZuNzVVGeiWN5DAuyMBVJyQO5rcg1e6srC4vLG2W5kVkVozn7nJOMd+leYQXE2R+8Ndn4cuJfsTHecmQ/0qIws7jc7qx6RomvWmq2S3FsNo6MpXBVscj3+tcdqvh17zx3JFa/u3v0MsbkAruxhwc9BweRyCRWrYyuqbVOFHQAYAqHUnZtb0Ik5P2huce1aEs1/B+kXmkX+ow3+DtWNFfaPTOAfTGK64sm3jpXH+G5ZDYSFpHYmZySzEknce5rfSRtxGaQIvSYMeBjFUJm2k5IHvUju2CNxqhdMeDnrQMzfEGnx63pFxZnHmkboz6MOn+H414dMrRSPGwIZSQQfWvex8seR1Dda8e8axpF4rvBGoUFgxA9SAT/ADqk9CZI55iuaKif75opkH//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the cat seem to be resting?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
