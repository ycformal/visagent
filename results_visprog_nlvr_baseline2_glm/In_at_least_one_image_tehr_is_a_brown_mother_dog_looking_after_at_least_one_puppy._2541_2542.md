Question: In at least one image tehr is a brown mother dog looking after at least one puppy.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/kv9fHzVcu0M/hqdefault.jpg

Right image URL: http://2.bp.blogspot.com/-AzBPhXdksDU/UXBKMYztg8I/AAAAAAAAGTU/m7p-3phH5L8/s1600/IMG_0211+-+Version+2.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image tehr is a brown mother dog looking after at least one puppy.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image tehr is a brown mother dog looking after at least one puppy.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

