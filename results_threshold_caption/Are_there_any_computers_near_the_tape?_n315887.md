Question: Are there any computers near the tape?

Reference Answer: Yes, there is a computer near the tape.

Image path: ./sampled_GQA/n315887.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tape')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='computer')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='tape')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAsACYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDi/Dmk/ZrA3c0M3mzYOxWAPXAHrzkfma5nxNfQvrZhgLGK2+Q7nzlv4uOwzx+FdHqktrpzmSCCBbyb5llVNrAEctnccE9j9a1tEuLKBYraONVVgCI0ReeM/dPLcVU5W0JhG+p53IArhkIw3PDZxU8bbgDu5HYV7RJ4Y0vUYP32n2rkjO4RAHB9CMGvNfE/hw+HtRQRZNpPkx5OSpHVSe/UGpTvsamRGRjpRU0KZHGBRSuNGZqGqfatXa6RVWIHaqqu0FfX6mi8DxFLuB2Vhhtyk8Ecg1mnAJCnjtx1FaenXSbDBOAyjoD3GelN9yY9j6G0RzNp0LuMM0YYj0PXH5k1yvxQhj/4R1JeN6XMe0/UMDVvR9eifT4pY5PlZevoe+fxrnvF+q2+toNMN1HFMpEoB6MOQPp3qKejKZw8EgYcnFFRSWl5ZNiaFuejKNyn6EUVVg0MLGR/nmnozIQwOGHP0pqncoPr2o96CWdPo2pny2hWcRk8lCcZPqM1BeWJSY3DSSMWJJcnOfrXP9QM8/WlP17UWC/c1ItVu7QBYLhzjjbwQPzorMJ24x+tFAro/9k="></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAsACYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDi/Dmk/ZrA3c0M3mzYOxWAPXAHrzkfma5nxNfQvrZhgLGK2+Q7nzlv4uOwzx+FdHqktrpzmSCCBbyb5llVNrAEctnccE9j9a1tEuLKBYraONVVgCI0ReeM/dPLcVU5W0JhG+p53IArhkIw3PDZxU8bbgDu5HYV7RJ4Y0vUYP32n2rkjO4RAHB9CMGvNfE/hw+HtRQRZNpPkx5OSpHVSe/UGpTvsamRGRjpRU0KZHGBRSuNGZqGqfatXa6RVWIHaqqu0FfX6mi8DxFLuB2Vhhtyk8Ecg1mnAJCnjtx1FaenXSbDBOAyjoD3GelN9yY9j6G0RzNp0LuMM0YYj0PXH5k1yvxQhj/4R1JeN6XMe0/UMDVvR9eifT4pY5PlZevoe+fxrnvF+q2+toNMN1HFMpEoB6MOQPp3qKejKZw8EgYcnFFRSWl5ZNiaFuejKNyn6EUVVg0MLGR/nmnozIQwOGHP0pqncoPr2o96CWdPo2pny2hWcRk8lCcZPqM1BeWJSY3DSSMWJJcnOfrXP9QM8/WlP17UWC/c1ItVu7QBYLhzjjbwQPzorMJ24x+tFAro/9k=">, <b><span style='color: darkorange;'>object</span></b>='computer')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAsACYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDj4oXmJEY3EDOO55AwPfJrE8RPssYWPQTDP5GtC7umtIfMjA8wnajnqhx1B7HGRn3rW0eVI74CQbg6lQoAOeh6Hr06V4tGKTpy6ts/Tc1r1J0sXRe0Yxt873/I8/kAVwyEYbnhs4qeNtwB3cjsK9ok8MaXqMH77T7VyRncIgDg+hGDXmvifw4fD2ooIsm0nyY8nJUjqpPfqDXtJ32PzUyIyMdKKmhTI4wKKVxo1by2N0iKsmza4YnGcjBGP1qj4hkkisIpYmZHSZWDKcYwDz+dc2dQvNxxeXGO37w8ir1jqDSqYbp2lXOcOScj0rgp4ScJRbd0j6zGcQ4bEUqsYU2pVEk3ftsfQeiOZtOhdxhmjDEeh64/MmuV+KEMf/COpLxvS5j2n6hgat6Pr0T6fFLHJ8rL19D3z+Nc94v1W31tBphuo4plIlAPRhyB9O9dtPRnybOHgkDDk4oqKS0vLJsTQtz0ZRuU/QiiqsGhhYyP8809GZCGBww5+lNU7lB9e1HvQSzp9G1M+W0KziMnkoTjJ9RmoLyxKTG4aSRixJLk5z9a5/qBnn60p+vaiwX7mpFqt3aALBcOccbeCB+dFZhO3GP1ooFdH//Z"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAsACYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDj4oXmJEY3EDOO55AwPfJrE8RPssYWPQTDP5GtC7umtIfMjA8wnajnqhx1B7HGRn3rW0eVI74CQbg6lQoAOeh6Hr06V4tGKTpy6ts/Tc1r1J0sXRe0Yxt873/I8/kAVwyEYbnhs4qeNtwB3cjsK9ok8MaXqMH77T7VyRncIgDg+hGDXmvifw4fD2ooIsm0nyY8nJUjqpPfqDXtJ32PzUyIyMdKKmhTI4wKKVxo1by2N0iKsmza4YnGcjBGP1qj4hkkisIpYmZHSZWDKcYwDz+dc2dQvNxxeXGO37w8ir1jqDSqYbp2lXOcOScj0rgp4ScJRbd0j6zGcQ4bEUqsYU2pVEk3ftsfQeiOZtOhdxhmjDEeh64/MmuV+KEMf/COpLxvS5j2n6hgat6Pr0T6fFLHJ8rL19D3z+Nc94v1W31tBphuo4plIlAPRhyB9O9dtPRnybOHgkDDk4oqKS0vLJsTQtz0ZRuU/QiiqsGhhYyP8809GZCGBww5+lNU7lB9e1HvQSzp9G1M+W0KziMnkoTjJ9RmoLyxKTG4aSRixJLk5z9a5/qBnn60p+vaiwX7mpFqt3aALBcOccbeCB+dFZhO3GP1ooFdH//Z">)=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 1 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
