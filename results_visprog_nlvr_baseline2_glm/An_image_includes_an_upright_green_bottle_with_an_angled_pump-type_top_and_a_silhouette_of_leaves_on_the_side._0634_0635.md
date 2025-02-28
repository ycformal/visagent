Question: An image includes an upright green bottle with an angled pump-type top and a silhouette of leaves on the side.

Reference Answer: False

Left image URL: http://i01.i.aliimg.com/wsphoto/v0/1925243779_1/golden-snail-sunscreen-moisturizing-skin-rejuvenation-resurm.jpg_350x350.jpg

Right image URL: http://68.media.tumblr.com/tumblr_mbvdwdEhxR1qddvqy.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image includes an upright green bottle with an angled pump-type top and a silhouette of leaves on the side.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image includes an upright green bottle with an angled pump-type top and a silhouette of leaves on the side.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

