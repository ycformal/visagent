Question: Both sets have an image with a dog with dark fur.

Reference Answer: False

Left image URL: http://moderndogmagazine.com/sites/default/files/images/photoentries/photos/baby%20tpod.jpg

Right image URL: https://img.buzzfeed.com/buzzfeed-static/static/2016-08/17/12/campaign_images/buzzfeed-prod-fastlane03/ollie-three-legged-golden-retriever-puppy-2-3608-1471449801-14_dblbig.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Both sets have an image with a dog with dark fur.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both sets have an image with a dog with dark fur.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

