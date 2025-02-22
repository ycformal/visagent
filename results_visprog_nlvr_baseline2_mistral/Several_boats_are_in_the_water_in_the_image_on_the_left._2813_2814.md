Question: Several boats are in the water in the image on the left.

Reference Answer: True

Left image URL: http://www.loveachill.com/images/achillinfo/standard/Sport/achill-yawl.jpg

Right image URL: http://www.advertiser.ie/images/2008/08/859.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are there several boats in the water?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are there several boats in the water?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDIh058gEHPtWhFp8iAfIa1rK1kA+4fxrVisnYdBXvvEST0R5vs4taswoLB3x8taEWleprZgtSDjH4VeSzz1Wm67MeQy9DsPK8XaSeCoE5+h2df510Hiy28/ULYAciA9v8AaqlHavb6/pVzGxAikYOueGVhg/l1/CtzWE8zVWwc7IkUj3yT/UV5rm3ieb+tjsUf3Fjkv7Pcdv0ppsiBymfqK6PyCfamtZhxhuRXZ7c5fZnMvYb/APlkKrvpAPVMV1ws1A4UVG9suOTj6U/rD6D9kcVNo8YydvNUJtLU/wAJ+mK7eeGNQTj8TWTeoBEWHI9quNZsfIkcZLpsAc54PtRWpLFmTO/P4UVXtUHIzoLdLlzzGQM9h0rTiVo2X93I+e1RvrFtaf6x0VQM7pGC/wA6sWWv6fqCXjWVzFcPZW5nk8olsDv09ga8+VS251KF+hoRQiVdwjKn/aq3Hb4HGK41/iZ4a8sOWu3I6KsJH8yKhHxZ0dSRHp96w9S6D+tYuvHuUqMux2z24a+tcjq2PzyP61JBJ9ra4uWxiSY7f90AAfyrktO+IVtrE9v5FhPG7XKwR5cNhiC2TjsMVJrvjS28MX8enyWUs5EKyeYsgXGcjoe/FYqoubmNPZvlsdM6nzeVO3oMVH9qw7hY2x/DmufsPiJpt/FPIsdzClvH5sxePdsXcFzxnPJFWYfG+hXAyNQtiO+TtP5EVvGpF9TJwkuhpySpHFzGd386z55blovkZhnvjmrA8R6A/TU7L8ZRQda0luI722c/7Eqn+taRnFESjIzfO8uPMqF29SKx7y7dhgRtjPpiullvbZk3IjSg8fJg/wAjUUtvG2CVIz0BFaxaWpLvscVIUZ84Ye1FdNNpqLIQ0Kg+9FVzxFaR4C08s7bpXd29XYt/OvXPgnbCUa88h+RoFiPpg7ua8XF7Apx5q9cHrxXqXw31/wDsWy1qCRrcpcWEk6PHICVKIeTjthv0FeMr3PRb0ODSNjjJGBwKnUc4BB46DpToV06WORUvN8ibdiscbh+HcfjTQ/lF1khmYdA6INoPryeRUXKueh/DSw88zzLt8y2mEiA/dJKFeo6HBNQfFG2kXxPBKMlXtlGR/skj+tdF8OrRbTQftDpiSZt2QMZHb9MVQ+ICJObOV5lTEhQyMpOAQD0/Cr6E31M7wZpq3HhbxbK2VIsGUYPtu/mBXLeH9Im1XX7LT1Xi4mVXIbkLnJP5Zrp9Avzp/g7xLZO8T3FzHhBGCPlyAck+xqf4cwWNt40guZJgCiS7YiAcZXjnPJ/Co5k7IfdmX4p8OfZ/EGqJaZVG1VLS2QNgAsu9vwGQK5C6S5tLia3mU74pGjbcQeQSD/KvSXkTUPEnhzzpwu7UZdSnDNkne+Vz/wAAUAVwGqWkNzqd/fw3wcySvK3mxthtzZO0AdBu6n0/GmmK5SaSWFIpTuTzM7SGweP/ANdWrXxJq1iQ1tqd5ERyB5hYfkcimatbRzfYoo5NywQhdxBIYnknpWd9ikjXb56hScgBelEZSauXVUVLlX9d/wATXl8ZeIJXLvrN0WPfI/worFazhdtz3MoY9dpIH5AUVfNPzItHyJTpzKFaJndgfus4UEfXFb2j2eq/2bqFratYQR3cJhlMzknYSCQpxwTgCsKO6mz8kQLZ/u1q2kupNGwiMcW7+8OldTow3SMlVklYo6hptrYrJGlg0k2wkFIywA78iqH9qj+zojb+cZQgWSJQSqHPp05HPNXNWhuHZTP5UrqfvgEEfQ1ixeHZZFDszKp9sVM4Ny0QoVOXdnZWXi9tLsJYrC+uY8zmRFbeAqFR8oHThsj9av6f4gbXtNVb6aaS8jcmQlgI2BJ24X1A6muQs/DtmzETPJkdMuQM/lW7baXaacuYI1SQrgsGYmqp2U1dEyvy2ua9jptpCxDTXjptwoeUlBz6Ac01rWzjuVmkj3MoxtLMBj1OD7ms7Y0YDshclufU/wD16DiJmHkykHBBTHA/PiutQitLaGPNK97mheC0YxiOBT5QAjDN93HTqeKpSlAxJRQSM4OaY63ckAUJIgzyCo/Dv1qncRmPmWN9xzzwCapWWxNrkx8hJAqoGJXcfSqkxiJ+ZEB+mKQru+VozgjPDZH41WmmURKWRdynIyuc+4pNotIRgoY/u/yFFVnlVnJJyfp0oqOZDsOilfzANxxnpU0E8v2xYfMbymkAKZ4NFFQUat2gAJy2ckZLE8UwxriMnJ2k4yx9KKK0sZF2zAYAHoE6DirMzsFYA9qKK5V8Zu/hKci7o5YSz7BJjAYjjA79afeKILhUj+VTtBA78UUV1o52TSxIsqbQRhCeCR2rDvbmaHzSkjDHIzzjj3oopS2HHcoRXU8quXlY4XjnpUUU0srOHlkIDHgMRRRWV3oakc7sspAYgUUUVDepaP/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there several boats in the water?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

