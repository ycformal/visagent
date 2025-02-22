Question: Exactly one animal is standing on the grass.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/2047341/9004/i/950/depositphotos_90040876-stock-photo-hartebeest-in-etosha-national-park.jpg

Right image URL: https://st3.depositphotos.com/7571106/16106/i/1600/depositphotos_161067452-stock-photo-side-profile-of-a-red.jpg

Original program:

```
The program is designed to evaluate the given statement by asking questions about the images. It uses the VQA function to ask questions about the images and the EVAL function to evaluate expressions. The final answer is obtained by evaluating the expression {ANSWER0} == 1, which checks if there is exactly one animal standing on the grass. If the expression evaluates to True, the final answer is True, indicating that the statement is true.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

