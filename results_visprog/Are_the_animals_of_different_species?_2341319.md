Question: Are the animals of different species?

Reference Answer: No, all the animals are cats.

Image path: ./sampled_GQA/2341319.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Are the animals of different species?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the animals of different species?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
