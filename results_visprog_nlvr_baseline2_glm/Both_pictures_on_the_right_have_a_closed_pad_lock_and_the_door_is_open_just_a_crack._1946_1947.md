Question: Both pictures on the right have a closed pad lock and the door is open just a crack.

Reference Answer: False

Left image URL: http://paxtonlocksmithing.com/blog/wp-content/uploads/2012/01/electronic-access.jpeg

Right image URL: http://www.virosecurityclub.com/wp-content/uploads/sites/5/2015/03/lucchetto-doppia-asta-su-garage2-300x225-300x225.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Both pictures on the right have a closed pad lock and the door is open just a crack.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both pictures on the right have a closed pad lock and the door is open just a crack.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

