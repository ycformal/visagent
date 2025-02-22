Question: The right image contains a blue chair with holes in the backrest in front of a small wooden desk.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/e25ehbB-5j0/maxresdefault.jpg

Right image URL: http://www.freestufffinder.com/wp-content/uploads/2015/01/Screen-Shot-2015-01-01-at-1.36.39-PM-450x281.png

Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image contain a blue chair with holes in the backrest in front of a small wooden desk?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA+AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD2jxJNLb6O8kMjRuHXDKcHrXmupeM/FcOqTW1ncw+Sm0KXhDH7oPJ+pr0bxV/yA3/31/nXCNBZC8LzMiuwUnc4HYVEr9AM7/hK/G7Hm8hH0gFA8TeNWOP7QQfSBa3QdMDYaaAY65lH+NVXRPtD+WQUzwQcjFQ79wM86/4xUq0mqYQ9cQr/AIV6b4ZuZ7vw/aT3UplmdSWc9Tya4G8j/wBGH1rvfC42+HbQegP8zVQvcDYr5Y8WeOvFdh4s1yC112+WGK8mWKLzjtUByAB6DFfU9fH3jFN/jXxB/wBfs/8A6MNWwGj4heNpDj+2rn/v+/8AjUL/ABC8YFxGNauXcnG1Z3Jz+dZYXy1LnoBmqmioZ9esvVp16+5pN2Q0jffxv412N5l5ebcc7nkxj/vqu7+DHjfxDrPjy30y+1KaWyMErGJmJGQvHUmtjxb4WgtbI2kF7ZkXKtuih+ZkOBk5yeOa4T4CnHxStPe2m/8AQaUW22mHS59Y0UUVYjD8Wf8AIDf/AH1ryXXLbT7q+cSR6iJlABeAoB90dMjOK9a8V/8AIDf/AH1rkrfSzPL5pVSGAP6CpkrgefppFmrq23W5NvTMyD+S1rWmo29gpjg0q7HPO64/+tXeDSB/dWse5so47qRSgyDWbjYDFOuPMRGdLl2nu1yf8K9R8Lyeb4dtJNgTcCdoOccnvXCTwIsAIUA5rvPDA2+HbQf7J/maqG4GvXx74ykWLxh4idiQBez/AHRk/wCsNfYVfH3i9A3jDxCCMg303/ow1bA5l9RheNkYTkEY+6KNM1GDS7+K8hW4MsR3IcqMH1HXmriWyHPyDp6VXu7cLCCFApbjN+T4l6nIhRpLl1P8MkisP/Qa1/gY1ufijYiGORT5E3LuD/AfYV5mR1r0b4E8fFSx/wCuE3/oBojFLYG29z6zoooqhGH4sONEb/rotc1BrNlZxrHLeWiOqjKu/wAw47iui8YHGhN/11WuF/4R+3vrlppN2XwTg+wpMRuP4v0tOuoWg+m4/wBKw7vxJokk7yNq0YLHOFhc/wBKsf8ACH6fjlGP41z174ftIrmVUUbQ2BUyvYZdfxLokn7pdVdj6C0avT/DMkcvh60kiJMbKSpZcEjJ7dq+UrrXLi21ZxD5ZjEjBBt7A8V9TeDDnwhppPUxZ/U0RTQXN2vkHxeceL9fOVH+nTck4H+sNfX1fJuu2VrqXj/WLS7Mohlv5wxhIDD52PGeO1WBzCXEan5riAf8DFMubm1lhCi6hB/H/CtHXvDVhYSqLJ58KAJBMwJyQSCMAcEA8VhyWCRxbs55oAq+Vbjrex/gjH+leg/BBYk+KeneXOJCYphgKR/AfWvNnUAkV6F8DP8Akqunf9cpv/RZpAfW9FFFMDnPG7bfDzH/AKap/Ws/TWgFrCWI3bBnj2rrrm3hu7aS3njEkUi7WU9xVKDQ7SCJIxvIUAAluaAM1rm2A+8PwFcPq8dy4uGhgZ3YMV2+vavURploP+WZP1Y04WFqOkK/jSauB8hS+Gtc+1h20i+wuQSIGPNfVfhGNovCunxsCrLHggjBHNawtoF6RIP+A09I0jXaihVznAFMSVh1fKGoAp8TdWDhlIv7jjGCPmbFfV9cj4l+HOheKNXg1O7SWG5jUpI8BCmZccBuO3Y9e1Az5x8ROBrV3BnhrVJFHurn+hNc7cZMAABr6iX4QeEDL5stnPM+MbnuG6fhirsfwv8ABkQA/sKFv993b+ZoA+Nishz8pNehfA5SPirpuQR+6m/9FmvpOHwF4Tt/9X4e04fWAH+daNt4f0aznintdKsoJoiSkkUCqy5GDggehoA0qKKKAP/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image contain a blue chair with holes in the backrest in front of a small wooden desk?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

