Question: In each image, at least one pelican perches on some kind of platform in front of the same double-peaked building in the background.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/05/2c/0d/f5/the-holiday-court.jpg

Right image URL: http://diversionswithdoreen.files.wordpress.com/2011/04/img_3601.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In each image, at least one pelican perches on some kind of platform in front of the same double-peaked building in the background.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In each image, at least one pelican perches on some kind of platform in front of the same double-peaked building in the background.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

