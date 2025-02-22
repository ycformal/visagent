Question: Three wine bottles with gold foil tops are stacked on a red mat.

Reference Answer: False

Left image URL: https://i.ebayimg.com/images/g/XHkAAOSwDNdVmHmW/s-l300.jpg

Right image URL: http://img.auctiva.com/imgdata/1/9/0/7/5/2/4/webimg/843289095_tp.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Are there three wine bottles with gold foil tops stacked on a red mat?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABQAFADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAorE1DVV06GS4uJbjy/P8pVhVCeme/41m/8JlYf39R/79xUAdbRXJf8JlYf39R/79xVPB4lhusCBNUbPGRFFigDpqKyZ7yS3tGuZBeiNRlsrGGH4Vkf8JlYf39R/wC/cVAHW0VQsrlrh42EjtFLAsqhwARn6VfoAKKhuWdLaR4/vAZGa4rxV4xTQLtbRrSa7maMSK8kmyPBzyAOvf0oA0PEFtLf2DW9svmSm837R127SM1hN4disUEmr6jb2inkBnAJ+n/6q5O/8d69egpHcrZxH+C1XZ+vX9a52SR5XMkjs7tyWY5JoA9Bm8TeFdLyLO1m1GUfxEbE/Xn9KyL34h6zcBksxBYRnj9wmWI92Of6VydFAHW+C9ZuJPFIjvbmSb7bG0BaV93PVevuB+dXLyA213LCRjaSMHrXEwTSW1xFPE2JI2DqfQjmvSfEGy5a11OEYivIlkA9M8/4/lQB2uj/AOpsv+vCKtesjR/9TZf9eEVa9ACEZGDyDXmvxJ03fo9regZezlMD+pQ8r/T869LrE17ThqVje2BH/H3AQhP/AD0Xlf6flQB4FRQQVYgjBHGD1BooAKKKKACu/wBAn/tTwNLbk5m06U45/gb5gf8A0MVwkFvPdSiK3hklkPRI13E/gK9F8C+GdbsLu4lu7XyLW4hKFZGAbd1U7fw7460Adxo/+psv+vCKteszTkWM28anIS0ReevHFadABVa8GIhKOsTBuBzjvVmmsAykHoRjFAHhPjfTv7N8V3iKuIpj58eOhDc/zzWRZade6jJ5dlazTv3EaFsV7o2haZqcsU1/ZRXE9sDEDJyMD26H8a14YY4IxHDGkaDoqLgCgDyDTfhjrN3ta8eGyQ9cne/5Dj9RXX6b8NNDswGufNvZB/z0bav5D/69dpSEgDJOAKAK9pY2tjF5VpbRQR/3Y0Cj9Ks1WN5FnEe6U+kYz/8AWpC13J0VIhnqTuP+FAEUCFNTmHbZlfxOf55q/VeK32Sea8jSSFduTwMVYoAKKKKAKhdbe8YuQqSrnJOOR/kU43it/qUeXtlRx+dTNGj43orY9RnFPoAq4u5OrJCPQfMf8KUWcR5k3SEHIMjZ/TpVmigBFAUYAAHtS0UUAFFFFAH/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there three wine bottles with gold foil tops stacked on a red mat?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

