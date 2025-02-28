Question: In the image to the right, you can see the person's fingers.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/Yq0EzVpgskg/maxresdefault.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/10/c6/1d/be/feeding-the-stingrays.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the person's fingers in the image?')
FINAL_ANSWER=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In the image to the right, you can see the person's fingers.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In the image to the right, you can see the person's fingers.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

