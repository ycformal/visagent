Question: Are these two people of the same gender?

Reference Answer: Yes, all the people are female.

Image path: ./sampled_GQA/2353344.jpg

Program:

```
 Are A and B of the same <attr>?
Program:
ANSWER0=VQA(image=IMAGE,question='Are these two people of the same gender?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are these two people of the same gender?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

