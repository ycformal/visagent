Question: What color is the shoe, white or blue?

Reference Answer: The shoe is white.

Image path: ./sampled_GQA/n66756.jpg

Program:

```
 What color is A, B or C?
Program:
BOX0=LOC(image=IMAGE,object='shoe')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the shoe?')
ANSWER1=EVAL(expr="'white' if {ANSWER0} == 'white' else 'blue'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='shoe')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAaAC4DASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzrxDdSWviKaWOWXyyoXIGMADlR2wDXS/D2yk8Q3E0l7eLFEFKKzkk/KMhR1AyT/8AWqrf6JJcyMoaPlvvBWz+fQ81SvtCOi+HTqkWolZzcCDyVyGJIBBBByvyhyfoPWsqVSL06mtSEk79C94qvo9O1m5tYZJoo4NiFhhsSbcsM49SPyrlTrF7Lcxo2pSJC332wDgd+MVd017a50+5tb6NHlky8Mm/BRjwMnuM8kd857VmPpd4FmkFpNLFCN0joh2qPXcOgrZGR3ulWUenxvJBctcLNgmVlADgdwMDrWml1IWZYwCc5IUE4/SuH07UpksljikkSKJcHCkqpPO0tjGTVlddvFjBinl9ssAcf5xXHOMr6nTGUeU3hqLpG2Pm5zWHqmnnUrhpZFbJIPI4AHHHOavH7p/3qF5Jzzyazi3F3RrKKkrM5z+wpiW2ZTk/fzg8dqedGvUVVadTGOqK7YI9OOx9q6EABWwAKfbjdforcqeoPStPbSRm6ETEkN2s/lQWiQo7BjDbROsIx0Owk5b3PNags5pcube2YnsVb86t9c57A1bThOOOT0+tRKq5FRpqLsf/2Q=="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAaAC4DASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzrxDdSWviKaWOWXyyoXIGMADlR2wDXS/D2yk8Q3E0l7eLFEFKKzkk/KMhR1AyT/8AWqrf6JJcyMoaPlvvBWz+fQ81SvtCOi+HTqkWolZzcCDyVyGJIBBBByvyhyfoPWsqVSL06mtSEk79C94qvo9O1m5tYZJoo4NiFhhsSbcsM49SPyrlTrF7Lcxo2pSJC332wDgd+MVd017a50+5tb6NHlky8Mm/BRjwMnuM8kd857VmPpd4FmkFpNLFCN0joh2qPXcOgrZGR3ulWUenxvJBctcLNgmVlADgdwMDrWml1IWZYwCc5IUE4/SuH07UpksljikkSKJcHCkqpPO0tjGTVlddvFjBinl9ssAcf5xXHOMr6nTGUeU3hqLpG2Pm5zWHqmnnUrhpZFbJIPI4AHHHOavH7p/3qF5Jzzyazi3F3RrKKkrM5z+wpiW2ZTk/fzg8dqedGvUVVadTGOqK7YI9OOx9q6EABWwAKfbjdforcqeoPStPbSRm6ETEkN2s/lQWiQo7BjDbROsIx0Owk5b3PNags5pcube2YnsVb86t9c57A1bThOOOT0+tRKq5FRpqLsf/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the shoe?')=<b><span style='color: green;'>black</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'white' if ANSWER0 == 'white' else 'blue'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'white' if 'black' == 'white' else 'blue'")=<b><span style='color: green;'>blue</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>blue</span></b></div><hr>

Answer: blue
