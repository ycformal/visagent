Question: One of the dogs is posing kennel club show style.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/9b/db/23/9bdb238df3bfdf38077faafb68d26f68.jpg

Right image URL: http://www.davolvoreta.com/foto/schnauzer/mediano/sal-pimienta/yes-to-volvoreta/1200x900/yes-to-volvoreta-032.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One of the dogs is posing kennel club show style.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the dogs is posing kennel club show style.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

