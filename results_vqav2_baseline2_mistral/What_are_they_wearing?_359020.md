Question: What are they wearing?

Reference Answer: shorts and t shirts

Image path: ./sampled_GQA/359020.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What are they wearing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What are they wearing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What are they wearing?')=<b><span style='color: green;'>clothes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>clothes</span></b></div><hr>

Answer: clothes

