Question: The right image contains no more than one dead water buffalo.

Reference Answer: True

Left image URL: https://t4.ftcdn.net/jpg/00/89/26/03/240_F_89260355_syk4xthMGLqbRBsckmBamylex0SPgD0P.jpg

Right image URL: http://news.bbcimg.co.uk/media/images/63144000/jpg/_63144802_c2f2fdc7-b417-46e8-907c-ebf579a45bd2.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image contains no more than one dead water buffalo.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image contains no more than one dead water buffalo.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

