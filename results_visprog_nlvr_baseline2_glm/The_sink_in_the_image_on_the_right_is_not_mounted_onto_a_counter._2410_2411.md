Question: The sink in the image on the right is not mounted onto a counter.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/05/30/24/f0/piece-hostel-kyoto.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/01/5e/d7/ac/single-room-without-en.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The sink in the image on the right is not mounted onto a counter.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The sink in the image on the right is not mounted onto a counter.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

