Question: IN at least one image there is a home with at least two windows and a white paintbase with blue line trim and only one chimen.

Reference Answer: False

Left image URL: http://thatchinginfo.com/wp-content/uploads/2016/10/107j.jpg

Right image URL: http://thatchinginfo.com/wp-content/uploads/2016/10/107k.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'IN at least one image there is a home with at least two windows and a white paintbase with blue line trim and only one chimen.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'IN at least one image there is a home with at least two windows and a white paintbase with blue line trim and only one chimen.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

