Question: There are four or five zebras running on the land.

Reference Answer: False

Left image URL: http://medias.photodeck.com/d8219e40-38bd-11df-95f0-afddbe2d886f/nami0914_xgaplus.jpg

Right image URL: https://i.ytimg.com/vi/c9f9fi4WZSM/maxresdefault.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are four or five zebras running on the land.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are four or five zebras running on the land.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

