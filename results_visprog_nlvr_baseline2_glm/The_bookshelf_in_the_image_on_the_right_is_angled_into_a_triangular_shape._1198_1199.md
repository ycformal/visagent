Question: The bookshelf in the image on the right is angled into a triangular shape.

Reference Answer: False

Left image URL: http://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2015/4/20/0/CI-Tamara-H-Design_Bunkbed-Staircase-Bookcase.jpg.rend.hgtvcom.966.1208.suffix/1429568578522.jpeg

Right image URL: https://cdn.makespace.com/blog/wp-content/uploads/2016/02/09131121/bookshelf-room-divider-book-storage-hack.jpg

Original program:

```
The bookshelf in the image on the right is angled into a triangular shape.
Program:
ANSWER0=VQA(image=RIGHT,question='Is the bookshelf angled into a triangular shape?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

