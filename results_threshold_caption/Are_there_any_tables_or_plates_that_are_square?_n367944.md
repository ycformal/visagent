Question: Are there any tables or plates that are square?

Reference Answer: Yes, the table is square.

Image path: ./sampled_GQA/n367944.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='table')
BOX1=LOC(image=IMAGE,object='plate')
ANSWER0=VQA(image=IMAGE,question='Are there any square objects?',objects=[BOX0,BOX1])
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDxVpSZDJJJvZzkkjvUn2ZbyRVVgrAEgvwMVCzkDgEY9hQtyyuGC49+ntWVuxRqLo0ixbzPbbEOdjSn5j24x1qXRbYW8k4XHzBenTv61PaXzyaSyfa7O3yM5KNJK30OMLTtLiEaTSbi5Zsbj1OKUW+pVl0LwHHtWdfzhFViPl5P/wBaprtyZVUcYBqGaP7RYPG4LY+YdjVbluFlzFDUJ4ldXEAhKMpKdeD/APrqTzYpbGRgARtOQT1qmwgZTu4CkZ5p4Ma52kEgZI9BUtE3Kkqw3UzLGzRRr68g1bi0q8huoSH8y2RgwdemPp2qJYEdWkjTKgYJB4rSsJblm2lnEITOD0x0FO/RCtvcvrp91MjXEQXy/UybcYpP7LvgDm3VvrOv+NdTpcO2whBHUZNQaQZrgXkr6jb3SGXEQQDEY5+U8e4r6inSUYxj5Hkyqtts5htMvcnNp+Uw/wDiqK7QwOTyIc/h/hRV+wX9f8MR7ZnlckYOQGJ9AMmmIypu3RqzFWGWPTI4I9xW7Bp73Kh4IUUMMgu5J/QVmX9lJaTbZwgcgEBW4IzivlT1zY0m4DWDRRW9ukhLZdoA/B5Az171PDIVskkPV13Ee5qlpt9DpW6KSNnbpIAchWB4OfQjH5VOrhrKFl6EnA9smotqWi7tSRAwAYEZyahVEWMeUBz0PaoYV22wbdw2Rg9uf/rU5B5i7A3U888iixd2ZGobBczJGkZ6ZGep71E5/evtRcFO55Psa0raGM3F0JEjYpJgllz2qnfzW7LiBIeTgsnXFO+tiWupDG+ISmQpIHA5FaWmKJHAXdnCqcnPU9vasVTjjtXQaTmyKTPEGw+/YTjP1q4JcyvsZtu2h3mwwWhEaZZI/lTpk44FVNFgMOlqJNMS1d3LNChJ9gfxArkL+4vLi4LWty9rCUC+SjMV9yc5zTYtQ1y3ULFqTFB0BCn+Yr3/AO0KPMed9Vqcp6KsSbchWGexJorhE8Qa6EGb23J75gB/kaK1+v0f6t/mZ/VahUhntIIn3ZJRmHDfiKxLm4S7YlEw+7dknt0A/D+tSXaSzTNsCKhOcA9T61nsDGT0Prjoa+csepclUSJ/HGPq1X7XUVEIhf8AhORVGKK9lJeGDaGHXGB+tP8A7MvZGLEAufRqTt1KV+hshjKkbx7QHX+tOIKD51JPqCR/SqluTDaQwyEq65BB+tXvOTZgsAenepNVsZeoSNFcSRodqSIpYDvxWezYHAz7CrmqH/TM/wDTNf61n+eYpUYZyDnimkZSepuafp5AWa4XD9VT0+vvWk59T+lYkWtL/E7D/eXNWl1WKT+OM/jinZhoWyPemEY70wXSN/D+RzTTdQg4Zip91NUIfx/s/jRTRNCRkSp/31RT0EZE1yXyqHC9z61Jp0cbzM0uDtHAPrVFTV+yQqDLjIPAFRJjjuar4EZZWAA71nQ6g0e9GbcwPFTNMNuEwcg5FVobdTKpIAOc5rL1Nb9i9Cv2xv3gYBOpJx+tWZo4448qgxjHHP41DJc5+X061GZy/Y9aEmNsr6gm+J5AOip+n/66xJASa6C7YrZSnrxjmsM81pEynuQYNFS7RSbKu5BGGK9CR9KmW7uE6TN+JzTChpCh9DTAsDUJu4jJ9StFVcUUAWreMzShB36n0Fbe1QoVRgDisKKV4slGwTS/bbnP+taoabKTsbflr1xzTWjz0rFa/uv+ezUhvLn/AJ7P+dLkY+Y1/Jlz97I9xU8cWOpyfesH7XcY/wBdJ/31Si8uV6Tv/wB9UcjDmRt3w/0GX6f1rCzT2vLiVdjysVPUVHTSsJu4tGaSjvVEjhS54ptBoASikPWigD//2Q==">, <b><span style='color: darkorange;'>object</span></b>='table')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='plate')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there any square objects?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
