Question: The bookshelf in the image on the right is angled into a triangular shape.

Reference Answer: True

Left image URL: http://www.urlag.mn/Admin/uploaded/tumblr_m4puzlsc4V1rw7sa3o1_5005717161962015-03-24-13-49[www.urlag.mn].jpg

Right image URL: https://cdn.makespace.com/blog/wp-content/uploads/2016/02/09143843/staircase-book-storage-hack-for-small-apartments.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the bookshelf angled into a triangular shape?')
FINAL_ANSWER=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the bookshelf angled into a triangular shape?')
FINAL_ANSWER=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the bookshelf angled into a triangular shape?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

