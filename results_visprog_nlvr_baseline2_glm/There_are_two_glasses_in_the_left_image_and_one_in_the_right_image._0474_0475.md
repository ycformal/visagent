Question: There are two glasses in the left image and one in the right image.

Reference Answer: False

Left image URL: http://wineenthusiast.scene7.com/is/image/WineEnthusiast/f/n/w/1500/35512.jpg

Right image URL: https://www.uncommongoods.com/images/items/22200/22244_2_1200px.jpg

Original program:

```
Statement: There are two glasses in the left image and one in the right image.
Program:
ANSWER0=VQA(image=LEFT,question='How many glasses are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many glasses are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == 2 and {ANSWER1} == 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two glasses in the left image and one in the right image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iioL26jsbGe7mYJHDGXZj0AAzQA5pxvKKMlevtQ06ohdwQB1xzWfpuoWOoRE2d3FcbeX2MCQfUir2M0rjaadmT0VDbnAaP+4cD6dRU1MRh3mrmyv5laQCNSMhhwMgflV+01S3ul+8Fb68GsnxJpJlja4trVrhpSI7iEN99CMZA9Rx6etc54G8G3OlPe/a7uS4s3dlhWUkSp04Jz25+tYXmpWOrlpyp8zdmejUVQsori0domlEtuB+7J++vsfX61eVgy56Vsnc5mrPQWimeYMD3pVfc2Mds0xDqKKKACoLy0hv7GezuE3wTxtFIvqrDBH5Gp6KAPmfXtHv8A4X6vGLldQ+wA4tNTsnHI7K4PRgO2cHqK7rwh8VJNcvYtNtI7nVbhgMj7KY2Qf3nbO0D3Neqalp1pqunz2N7BHPbzoUeORdwIPtWH4H8N6X4b8PRwabapCJWLyPjLOcnG49TgcVKilsbSrSmve1OiiQovzY3Hk4qSiiqMQpjfeH0Jp9c94w0C713Sgun381lfQNvhkjkKhuMFWx2P6GkyopNpN2NjAV87vwziqmsammjaJqGoSRtIltEZSinBbA6A14IZvHza2NGFzrH2zftEe4jj+9u6bffOK9p0Lwq1r4Vn0rWLya/mvEYXUjuW+8MbVJ6ADp+dSpN9Doq4eNKzck79uxylx8Z9GijidtOviZFztXYcfrVzw78VLDxF4jtNLttNuojPuAlldcDCk9B9K8p8YeBdT8L33lPFLc2bn9zcomQ3oD6N7flXonwt+HtxpEya9q0RhufLK29s33oww5ZvQ44x2yc1ClNux11aOEjSc4u99j1eiiitjygooooAQ9Pxqjohzo1qf9j+tIdWheSWFIrvzEB62sgUkejFcGqGmaj/AGdo9nBeW14Jwu1hFaySAEH1VaAN+ikVgyhhnBGeRg0tABRRSMSFJAyfSgCp5af2uJNi7/I27tozjd0z6VcqofN+0CURHIG3HtVpSSoLLtPpQBV1FEe2XeqsBKhwwBGdw9at1WuBJKuzyztznsenSpYmkYfOm38aAJKKKKACiiigA70UUUAFFFFABRRRQAUUUUAFFFFABRRRQB//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two glasses in the left image and one in the right image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

