Question: Are the people of the same gender?

Reference Answer: Yes, all the people are female.

Image path: ./sampled_GQA/2380680.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Are the people of the same gender?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the people of the same gender?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
