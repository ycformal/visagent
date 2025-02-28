Question: A person is holding up a leopard in the right image.

Reference Answer: False

Left image URL: http://www.namibiahuntingsafaris.com/wp-content/uploads/2012/03/hunting-cheetah-033.jpg

Right image URL: http://africanhuntingsafaris.com/wp-content/uploads/2013/02/hunting-cheetah-025.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A person is holding up a leopard in the right image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A person is holding up a leopard in the right image.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

