Question: Is this a park?

Reference Answer: no

Image path: ./sampled_GQA/256250.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is this a park?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is this a park?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDaEWO1KI6sBKXZXq8x5vKV9lOEdWAlLso5gsVhHzS+XVnZRso5gsV/L9qNntVnZR5dHMFits9qTZVry6PLp8wWKmykMdWygzjIz6Uhjo5hWKnl0VZ8uijmHYlC07ZSg04GufmNuUbtoxT6KXMHKIFpdtOFLnAp8wco3bRtpwOaM0cwco3bSYFV4LiZ724hkCbIwpDKT3zx+QB/GpbiQRQSSH+FSaXtNLj9nrYypIfN1aCWB5sJOzygScYC4GR6Fu3sa0yw9KztPkVp7o8DYIwTn/ZJ+lXiyhdxYBeu4nisqErx5u5rViua3YduHpRSbSKK25jPlRwy+Lb4Ox8xDlsgEDj2HFTf8JXfEEho/wDvkVlxR26sGS+lDA5H7vAz9avZQId19LzzgDd+lcKlLudDS7FgeLL45/1PHpipl8U6g2cQIR6haof2TbyATBpCzc7tm3+tK2nfKwtJ8NjaCzDj6Zo5phaJpx+JNQx80GT/ALuP6UreINRcqUgcD2UHP6ViDQruOylzNJO3LL+8wT7cc1Fpmm6lNawpdpKCc/vDKVGM8cE5ovPzHaJuHW9TdjhbgAjGFVePf7vWlbV9VI6XS46/Kv8A8TUKaPHHiN7rnHGJmFK+kxpKpNzlcjP71yaT57XEuVsrHXb611WfzJJUMkKSMGCgcEqO1W4danuh+9nZoS2D8nI/LtWz/YdhLdsLtkkuJFZo9x/urnA9OM1z4e0zqAAUmCNWCqRknJzx24x9K53UnJWOpQjF3KGpQ/2nNcHfdrbF9qiI4U7QBnp6g1ClkUtVtkuNQMI5CMykfliq+nzl7UyM0gWSRnEYkOFBPcfnVlnhixuhZ+M5Em0VadtDJq7uRf2QT/y21L/vof4UU9tRt0O1YZMD/ppn+lFO6Fys00tdNUD98WI/6a1Zj+yQsAkzcdvMrmv7RhEh8uIFOgzgZqvPeSTPuVI17YzkmunngtkY8kmdk89s4+abqMZ8w1nm10+KXzXeXg5GZjt/nXLnL4yc47AcU/y2bG/kDpn/AAqHVi+hSptdTsFurQxDbcAovP3ulQNqlpGxRJ2J3d2zz+Vc0tuTgBRyc5pyxfKcjj6Ue38h+y8zdk162Z1BaQ7XDAqDxj1FR3niFEikaOOSQAEk9KyViUAYxn0HFKkCuNjDIJwcn1qXWbKVJI19SvJJWtbuNfNUxqNzk8HHb34NVLCOR1uorfyYpbkLbh9pJXewzk9egNMkDzwW5kkZj5YBz0JUsAcDvin2yeV5ewMv75T8vHIB/wAawvaJtbUpx6k0EMcIvYlVQFHABpXuJJV+e73Ke3GKmitCVCLEMY4+WrSaTcSMONoP8WMgVXMyeVGUWjP/AC0z7hRRWsdNuUOFRiPVVODRSuOxhrajC5UDP9408QMGIG0jvzUqyMvyjGMkfdFWIpH+z53HrS5gsV0ibOFIJ9PSpEtpSnKnOfTOatLNIXjQudrDnFWBCgdiNwwSRhj7UXCxTFhO+DglcZOARzUv2KSIgOMDH8RAB/WtO3iSXbvXOMgc1qw2luImfyk3LwDjpQOxiRWdtJGob5iBhijH8+BVxdOhjdX+ZCrDB27t304p1xM8c5jQhV5GAoHao4JpWRQZG9evfNK4WHfYX+zxx/ZnKozHzGQDAJzjr+tPNqoiQb9ihw+52XIx/dA/mfSr1nbxXgiNwDISxzuY+tbcWlWEdv5i2kQfJ520IDlBBas7FriXDsxAXgKeuAaj/s+xdiTNfv7K7j+tdTqO2CFPKjiXgniNf8K1nRTZQyFRvwOfqKd2BwMejae6A+ReH/gUporrBIz5LHJyR0ooux2R/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this a park?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

