Question: In one image, one person with her head turned rightward is standing behind a non-curved glass display with tiered shelves of baked goods.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/0e/05/d2/83/carlo-s-bake-shop-goodies.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/fc/3b/cb/fc3bcb76f9898d336eccdd3b485a768f.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In one image, one person with her head turned rightward is standing behind a non-curved glass display with tiered shelves of baked goods.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAoAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDn08Y+JLe4kZNavRbsvywRvsCueSc47nPHvWCtvcS20RKSPKJAzDbncQ2QfTp2rp9A03TohI66Bq99I0almaNZFRgP4cnjBzzmr8vh3Vrm63aZomoW1sQUaKVcOTjqPTHXFZU5OOiOmUr62SOWW7nvbiVrd7hgolQ/KAI9zA/IvReh4HFTWUV7aaYFttV1eCVp2Zo4pSIyh6MMfxH61sXnhvVdK0y9WLTXRZI+ZZAwOMYJPPWpPC00EujQW8mhalM0eU32yZVue1OpJtWsOlp79032Zy114mltZmgi1PUGWNiA0hYux9SfU13Xhaa/1/R9RgsrpvtAijihdyGAfq3DDjgYOe9crc+Gb03810mnlUeU4tZYTkL2LN64wa6rSZ7vw1ZtPaaaWnWQExkAIzMQoyQScc1lyWdy51ueKWmnoQz6d4ktLh7e41uRJUOCqW8Z549B70+HSvEbAA65cKW+6DBGpPOOhWtOWPxHqN8bwppdq8hOUZ2kByAvTHv/ADoj0vxCyr/xM9OA3Bx+6Y88EH/x5a0bZSaM7+xvED70k1m6YZ5Bhj/vbe6/3hilh0nX5smLXLpsO0ZAijyGXkj7tbB0/wARYLHXLPHJP7gn1b+maYuka5b+Zt121jy7O222xk/Nn/0E0rsfNEyJNN8RRr5ja5cBAQuWgjPJGcfd64q3/wAI94qOnR6h/bKG3bABMMRIJOP7tWZtG1iQ4l1y1bZz/wAe54wCM9fRTWqp1iPTBp327TfIXnH2d88Enru/2T+VNNkykuhzLad4iU/NrEIz0zax8/pRW7LZagW/e3+nKecBopOOTn+L1z+tFXci6I/DGgaffaRb3SvNukByIbXcv4ccV0jWVzEirEdVZMFjutMnjsOa4jTvE8mn6bDbwTXRdR8zPKyZP4A5q2fHl2kYjlkdImJDMbggnjscA1jCEehE5vqxviOfU9OsIGeK/aa5TMqzLtRSTz7ngjpS+BbydtFtZbWG2RCoiZJWXrxyfl4Bx+tY2s63BqVuULoW/vtOxK8dfrWLoF3b2VjDBdQWczMFBM8jJjjpwPfFU4pLQzvrqexXGnzXlqJDBpiSMdhfKhlbsM7en+Nc54gtNQjsitxBYIUZNwUAO5DDGMDj61gjUNIWBN9jp0rY6m4bj25FS3Gu+H5NOt7QaVbrqTyqsE8dxu2YYdieTjPSnHzF10ZlzSarbeI4ZZ72TypYHIiEh2K4I6Z+orppJzJpHli58liUVewQnGCCOTyOmewrJ8QvaQXllPdSiKJI5cuyF+69hXNQ67I6vDaXS3m6QNExg2bTu/hGPTjnNc86cpPnWxs5JS5TVuBcXtvAq3s/7tbgyMLh18wKFAyM8D5iPzqjqN0mkBkW8uZ5pY5EcvK7qnQhgSeW5b8z61mzagI9SW7uIfLV3If5TgjA7fUCtkzQtdwfNDIxjl2nyw2PlBHXknjvSVN2Wouezd1sYkY32Vzdy3l9ERtELfaj94nkkE8gDJ45qzBp1mdHurybV7uWWGdRhbhlV1JGflznoT09TUOpanBe2g01bSJpjcI4kjG2Qkg/ID0GeKp2twbZv30TIHfhSN2duR0x1ySK6IUmo3bMXVTehfurCxvXWZLm6dSuAXuXJ4JHc9KKitLiVYmR8nY5CliRx17j3oppSSsNyRxw8ZasP44f+/Qpkni3VJseYYGx0zEKKKvkj2J5mMPii/P8Ft/35FNPiS+OPlg4/wCmQoop8qC7Gt4ivmGMxY9oxWn4Wv7rUPFmlxOUI88HhcdOT/KiiiyBN3PaNT0W11mJI7oybVyBtcr1IP8AQVQsvB2lafKz2kN01weAS7Giis2tLG27uLc+HmuJ0kaCVSmTl03E/maiOlLBNbyrErSRbgN5VcgjHY0UU0ktkRK7LDWlmITI1pbpKuGyjgnjmorC502yjC3aAyBiQ3lk9ST/AFoorRP3WjFpc6djQGvaGRkqSfXygaKKKk107H//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image, one person with her head turned rightward is standing behind a non-curved glass display with tiered shelves of baked goods.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

