Question: At least one panda is lying on its back.

Reference Answer: True

Left image URL: http://www.sichuanfun.com/wp-content/uploads/2016/07/panda-facts-4.jpg

Right image URL: https://i1.wp.com/www.kickassfacts.com/wp-content/uploads/2016/11/panda-bear.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one panda is lying on its back.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one panda is lying on its back.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

