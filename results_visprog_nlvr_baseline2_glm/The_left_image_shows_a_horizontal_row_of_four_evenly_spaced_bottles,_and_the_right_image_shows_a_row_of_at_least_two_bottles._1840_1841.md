Question: The left image shows a horizontal row of four evenly spaced bottles, and the right image shows a row of at least two bottles.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-v5ndbycE5mE/TdtxfMNjI-I/AAAAAAAAGYE/lGRGJFDXcBI/s640/Mika-x-Coca-Cola-Bottle.jpg

Right image URL: https://i.pinimg.com/736x/a1/7e/49/a17e49b3b1edf6915bb5ea26306f2417--corporate-identity-packaging-design.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left image shows a horizontal row of four evenly spaced bottles, and the right image shows a row of at least two bottles.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA1AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigArB8YTXkHhueSwujbXG+MLKMcAuAevtW9XKfEO+Wy8KTnaru5AVWz2Oc8enFRU+FmlF2qRbV9Tmfhx4n1fXPEt5b314ZYYbbIQMCNwYLk+h+leo14R8Odfig8fwwXTOtzdwNbszxhQxHzJgADH3SOc5r3epo/Dvc1xdSFSq5QjyrsFFFFanMFFFRXVwlpaTXMufLiRpGx1wBk/yoGk27I5/SP7FXxFePaXNu1/MX8xFky/Dc5GfWulr5+8FeIinxDt7qZMR3czxkDkr5hOP1IzX0DWVGr7RXPQzLASwVRQbvdX/AK9AooorU84KKKKACvOviPqAhvLK3eKWaPKkxRgfMSevPXHpXoteV/FoMkltIs5jfaNihSTIcngY796wxEeek49y6btK6PO9e1S3XX9OvIbZ4ZbaeNhIwKkMrjHJ7cHvz7Yr6YHSvk14zd3drGskikTrEzO3GS390jqDmvrFRhQPSssHSVKHInoiqsWtX1FooorsMgqjrIJ0PUAuNxtpMZGf4TV6qeqjOkXo/wCmEn/oJoGtzwuwght/FNmYwN5mtgW+yKqkhhnae3U9AOlfQFfOOm6ml34h0rPnG4+0wmRmYbSdw+6BX0dWVKSadjvzCjOlKKkmtOoUUUVqeeFFFFABXn/xI3Mbc21y1veQxtKkiYDJzjOccda9Aryv4kTSW/im1d5ZY7ZrRdxSISHcrllIB4yGwaiorxsJ1fZe+jzaxJXxBpbTwOQ15E7uVAVh5gG7GMDoa+na+cm1Wa7vIbZLq/mSSeJEhntUXCg/3kGep4/HPavo0dBU04qKsjatiXiJuQUUUVqZHzb8b/FniHRviB9l0zW9Qs7f7HE/lQXDIuSWycA9a83/AOFheMf+ho1f/wADH/xrsP2gv+Slj/rxh/m1eVUAb6+N/FCPvTX9QV/7yzsD+dTf8LC8Zf8AQ0av/wCBj/41zVFAXudL/wALC8Zf9DRq/wD4GP8A40VzVFAH3/RRRQAVVuYI5ZMuobAHUUUUmOO5D9kgXG2JVPqBWhRRQhyYUUUUyT5V/aC/5KWP+vGH+bV5VRRQAUUUUAFFFFAH/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image shows a horizontal row of four evenly spaced bottles, and the right image shows a row of at least two bottles.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

