Question: Is it indoors?

Reference Answer: No, it is outdoors.

Image path: ./sampled_GQA/n130638.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is it indoors?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDx7Siwl4G72rpRFJsEojZeOQ3asPw1Zz32ppBBC0shBIVBk8Dniux/4R3WYy0rQzKB8xJjIAFaNmMoOT0MOXzwE2xnkA8elSJ54XLD5T0Xbkj8K2bS2SS6hjuLsRI+1FKAMCfcZp7waRhnbxBgxv5eDbnOc+3brzRdvZEuizGTlc7XwD6HrTZXRULOSvGcZ610s1tpaq8R16HzEj8wgRMeMZyCOO/Sufuoi0Za3SSZSwKzKp+cfT6ii73F7OxVW9VvlEZLE4A5rRisryS2FxF5IBBb5pQCAOvBrNVJ1ZMRS5yP4DxzXaWcEaaAMtAJZEdypUmQn5sDpwOP1qdjSnTTepy9lqAS4LOwBx3HWtTUrtHYKHX51Vmx/DkdPrWAu4R58oZIx930pbyQy3Ui79rIgI9+BxTsLVRsPuy9uu4PuU8Zqu+9owXcD2xVpomW3HnSw7WXgFg35gdKzpDudlD89vpTuzOwxshiC+Mds0Vp2lrazxF5sb92PvYoq1JDsUvA2rJoviOC7eMuuChAbbgMME5r2C58YRfZJwluZFdfLOLogjf8obBUZ+92Pqa8e8C2v23xLb2+xX3BsBsY6e9eur4TZutrA31I/wAK551lB2Z1xjJrRMrx/DiVTbRGWAyRzktKVYh0A6bc8fXrms7UfAlx9pZI7q1hSJ/LAWIksc5yfX72Pw+lbi+D2U5FtED7SEVIPCJzn7PB/wB/T/j/AJ/KoliYtaDjSknrHQ5248DXumyBZbq3uGkDEboWTGFx3HI5B/Cr1t4G1OOKHUrWe33TSHZEI2TGcnHIxj/61ax8JlvvQwt9ZmNFvpbWV8n2J4vtaNsxHOSY8jknPQYP6+9NYmN2OVJuCSi7rqYGp+E9YgsZ7yWaVUijLyANlT+p/SsZ/wC1IbFULk26rxjBC/jj3r0e7sNUurWa3kvN0cq7XXzRyPxrNXwpGBkwwknrulGT9a0ji6VtUYSoVHqi4virR7ZbUSQXEbSRLIq/u23LjOcZzjg81LpS21/aWVzbS4IUs8TAc7iWUHKnsR3qn/YLKwYJaAgYB3ICB6dKgvpdS0jTSLJJbjysAW9tPjC9z9BULExbskXKjpsyebym1C6SVYIVNy8a4C4zgE/h6cVx/ivULOfyLOBAZbdm8yQIoVuABgjk8Dv3rqTpc8x859hlkO9iLvOWIGTnP61Uk8KRyyF2tIWc8k+eCT+tafXKdrWZlKhUb2PJCDuOCQM9qK9RPgu1z/yDoj/23H/xVFR9bh2NPZS7M8y8DM0fiWAqxB2tyDjsa9W8+bvK+fUua82+GLMnje0ZQDhXzkZ42ntXvLWNheDMlrGjY5MY2n/P+exrnrpORrGjKcbpnICab++T9WNZuo6zNC/kQSYmV1D5Utx6Y7k5H511mp6Rp2n6dcXr3kkUcKFiGQH6D+X+cV5DfS6obtN1rci9ZI7ncufunkPt7Z4608NSpuV6mxnKjOJ6HHemWNXA+VhkZzWro1vHqLyW0cVtA8rZeR03M7YwuGzx78Vm+H401mCQC5QXER/fK0ZXax6geuDkV1GnwppUFykZD30y/JIBgKnsT3zWcEozd9jSFGqm0ldHMyOIpWjf5XQlWHoR1pnnR555rTj0k3KCVLmNg/O7B59acfD8/aWI/nWFkL6tVWtjLMqEHbgfUA1VkeXeGDqMdguM/X2rabQLnOA8WfTJ/wAKYdAvuyo3/Av/AK1CRqlVj/y7X3GN5su7krj02U7zx2D/AIVq/wBg356xx/8AfYpf7Avu/kr/AMDFOyJkqkvsL7jG+0H+69FbP/CP3HeSH86KrQy+r1f5TyP4an/is7U/7L98fwmvc2aYf6soCPUf5/z+NeAeB7yax8SwXMDAOqtgkZxxXrP/AAmOoYH7u3b6xDFbYhXkdVCvCnG0i7remX+tW8VtJPGsAlV5ECn5wOxqvdaJfXF6159pj8wxiMBlOFGc5Hvz3zVZvF2oHjZZ5/64imf8JNfSAbksx/2yzn9aw97ua/W6PYsaXo99pF+stutuEZSJtzZ3EnO7Hc8963t9yJmmDjcV2/KMDHt6VzB16+Ixttx7rFzUL67eRxlnljUf3jGtDcnuwjjKMdkdcdSkgX95GW9wSKlGvB12negHRV5rkG1HUdgZpCikcHywM/pTG1XUOgum/AAfrSV+43jKX8rO1XU426PIPqp/wpXvoFjLvOiJ/eY4FcBPf3IieSe6lZFGSC/X0ridS1K6mlYvO5BG6Mk/dPpjtWkKSluxfW7q8Ue4tqOnBQ0mpWiqRnIkDZ/LNQ/25ocZyLnz25wDkL+Pc15Po19Nd2gimAcRrw+3HfpVq4lhghkmbcQik4UZpunGMrGLxdS9ju5dZtd/yXqhe2D/APWorzOLXfPMjww7It5CAY6e/vRWiwy7mn1qoc34Yx/ay5IHy55+orvxtcZziuE8Jf8AIWbIB/dn+Yr0LykB4ReoHSnWV5HJGF1cYvljuGPpT9xbOM/lTk4mGOMtjj8Kp6tNJBqtvDG5VGPI9fxqI0uYp0ktyd22DJX8Miq7TqsySyKQU5jyeN3+P+FaVzbQqQQp5Xn5jWdqcEUmnXKMgIKZ9OnSolRv7pcKFrTQ6216aaUwvktJ8u09CahFw0hGG2+vOfzri9Fu7g63axmZyhfBBbtivQg7AqoOF44FKOG9nuylTjV1ZSkE7CFNm+MvmQEdVx157VzeoGFtRKysEQcbl6Cut1J2G1QcAL2H0rjdTGGMg4bd1r0qeHUVqc1SfK+VGxpMsUaeXazEq3LEr8h9Axq5qDvIxFsIzMT1l+VSO/A6/wBa5axmkLqpc43jiugtP3jSM+SUPy89OM1006NKT95HJWqVUlyv7zKfwprsjs58kZOeZgv6UVpfaZjyZWJPvRV+ygV7WR//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it indoors?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
