Question: Are the shorts small and white?

Reference Answer: No, the shorts are small but black.

Image path: ./sampled_GQA/n244826.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='shorts')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What size are the shorts?')
ANSWER1=VQA(image=IMAGE0,question='What color are the shorts?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'small' and {ANSWER1} == 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='shorts')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA2AFoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwBUxjJXbjuSRtH+fShjGNz5JY9TnJ+vTmsoXb7SVTJ3YIXOR6EYH8qs200rvl/MBY7cDcQfXg49q4DM4jxXeG41mWLBCQgRqpGMdzx9SaxVTPzDj8Mj8alvmZ72Yy/NKZGLkjJJyc0WkEckoVneNz90xxFifwBz/OkfU0ocsYwS2RFsz0JjJ98qf8KTDI2HBNbdvbQyAK9u84H8aQyIT9eoP5VXurjTrGfyZbadW6+U8uwr+YP8x9KlNvRI6JQjBc0pWQmmASTrGvVj0rqvJCSeXJ8m3BKnIJHqK5a1v7GG6juLaDGzkiS6U5yOwAzWhNreoTkzhYobZAf3jKGZiCPlxnjPI9amOHdSWx108yw+Fpe/K78tzto4iLdMjK7dvPIIx7HkVkaQX03xFEjfLiQD6g9K0NNmjmsIYraVSI0CMjqQ4xxk5HJzn86g1e3Kyw3Sh90bBXYgDjqPfrn86vladmfNYbF/7TUvtNv89DtfF2Be2U2Dl7bGQfQ//Xrmj5ZOctz7ium8WCWTS9KuYV3EKRwccEA9ce1cnuuP7g/7+L/hQ029DzcRG1RltbbyQdigbjz1/wAOKkWBWZNhk3cE8D17ZqIQx43eSQ2OSnp/31/Kn7FLEMGIHGT83507mJ5JcjbcylskmRvqTk1ApzJgHLDkkdFx3z7e1S3f7nWpbA7xsuWgLnrjfjP9aqWOoGx1a3uJAXhhl+eNONydGH1Kkjn1raFFvVnv1MfTjH3NS7dazdS26xx6kUj5D4ch8exPJH4/lVe2huwwMaWd/Ap4L4YD6/xL+PFWbvTIdOvFVJFuLUr5sE2zIliPAb+hH8LAg9Kc+n6aSjOgi3oWSSNyBkdvauqFOMFaKPMr4irXlzVHcbLbweRKihrbYrbkk6xtlSFz/EMZwe9S24LQrGSRhi/H3mOe3+P/ANaoNSsZLfTYbuKSSSDdsO5vf5fqAcj8arWNyTguxZsY5PQVZgdx4dWGDUo8xoHlHloQ7Zy3Y57Z4ro9Rb/iW3BQM+MFgi44yD0/z0rnNDtLq7gWYeXb2j8C4uH8uM/7vdz7KGrrBcLIxKOxIyNzRsmcHn5WGRk84PbFc+IjZqQX5ZKSH6Lrcup6ra6PfSmfTDGHVpAE2nG0fMvTk4Hsa6Y+FEDEDVSoB+60WSPYnd1rlvD1tPHqj3zx+RHkFjKABEMjqo+8T6ds5rp21zWHYvbeH5JIGOY3JALL2PT0rB2PRnCFWzsjl3bzerJ93j5+34inLsdQCQp6ErIOopyOhdsOMgbu4OKcxUc/e4BDelY3PJPL/FlmbDxTNeA/unRblWAB+bpjg4++P61jQ6Deyxo7+TCHGVFxMEZh6hT82PcivTtb0NdXltZ1mhtpoCxDmHeMHHzY6FgeRnjn2rEbT20yeSKQlnJ3ea2cyZ/iOecmu2nVXKl1NYLmdjCsrHW7CDyFisr20Zt/2d5ldQ3TcvzKyH3UjPfNdBpOg3WpbYl0K7XOcrFewyKCe+JBn/x6mmZh3/Wt/wALaq9rqSxlsLJ796p1LK9jeNJN7he/DHUE8OamFVbcCBpxDLtO51G75djsAflx2rl9E8JR6fNFd6mI7lsBhbjlB6bv7306fWvoBJBdW21uVddh+hGP6145bSF7GONwRJFmJgfVfl/pWTrSbOmlh4u9z0Dw/qMbASIqJIwALqMNgdBnrgenSr/iazF5p63ylvNh4Zg3JT3PsefzrhtEuzFceXnvmvStOkS5tCj8qy4I9QetZu99R1YJxPPPlVMGUFeScj5fqPerK3d8ihYtRdI1GFXz2GB2GM0l9GbC7nt5FJ8lyhYkDcO36YqtuDcgkA84BBqLs8puSdhsrCMpExyzAYyoI+vrT0idI2KSYXvgYP8AX/JooqUIhyLfEIJVS20Y5weveqOsxC4tDKceZEN2QuMjoRRRTi9SoP3kc4Tg4qW2mMU6SL1Ug0UV0HdE9l0O5Nzp6kjGVzXmGtEWfjbWbRR8hmEwx23qGI/MmiiskdkHqJHK0Uyup6GvTvDlwzxqT6UUVb6ES6md4tgEWoxzA/66LDDA5KkD+o/KuaaS2VyrQEsDg4Y4zRRWb3PKraTP/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What size are the shorts?')=<b><span style='color: green;'>small</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color are the shorts?')=<b><span style='color: green;'>black</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'small' and ANSWER1 == 'white' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'small' == 'small' and 'black' == 'white' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
