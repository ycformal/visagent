Question: A person is holding up a leopard in the right image.

Reference Answer: False

Left image URL: http://namibianhuntingsafaris.com/wp-content/uploads/2014/12/hunting-namibia-077.jpg

Right image URL: http://www.namibiahuntingsafaris.com/wp-content/uploads/2012/03/cheetah-hunting.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='Is a person holding up a leopard?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is a person holding up a leopard?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

