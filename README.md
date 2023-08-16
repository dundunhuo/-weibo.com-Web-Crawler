# "weibo.com" Web Crawler

 The toolbox to collect posts from https://weibo.com
![](https://shields.io/badge/dependencies-Python_3.11-blue)

## News

[2023-08-17] New version of Google Chrome forbids to open cookies database while it is running, therefore we cannot retrieve cookies automatically in Windows. As a temporary workaround, please log into weibo.com and paste cookies manually.

## Usage

1. Run the following command.
   ```bash
   pip install -r requirements.txt
   ```

2. Login https://weibo.com/ in Google Chrome. Press F12 to open the developer's tool, refresh this web page and paste the cookies of the first request. (Used in step 4. This is a temporary workaround because of News 2023-08-17.)

3. Activate Python environment, and use `cd` in Linux/macOS or `dir` in Windows, to set the program's root directory as current directory. 

4. For example, you want to search posts containing 'Genshin Impact' on August 15, 2023 from 11:00-12:00, run the following command.

   ```
   python main.py --query="Genshin Impact" --start_time=2023-08-15-11 --end_time=2023-08-15-12 --max_page=2 --cookies=*************************
   ```

   *To keep data privacy, cookies string is masked. This value is pasted from Google Chrome when you visited the website. See step 2.*

5. The result is saved in `posts.db`  in the program's root directory. Open the `search` table to find the table name of your queries, then open the corresponding table to view results.

For more details, run the following command in step 4.

```
python main.py --help
```

The data structure of searching results are as follows.

| Name        | Type | Description                                                  |
| ----------- | ---- | ------------------------------------------------------------ |
| avatar      | text | Link to the avatar of the post author.                       |
| nickname    | text | Username of the post author.                                 |
| user_id     | text | User ID of the post author. His/her profile is at https://weibo.com/u/user_id where `user_id` should be replaced with the value from this column. |
| posted_time | text | The time when the post published. Its format can be either "seconds/hours/days ago" or an exact datetime with or without years. It also contains Chinese character which represents "month", "day", "second", "ago", ... |
| source      | text | How the post author visit "weibo". It can be either the device name or the topic (tag) name. |
| weibo_id    | text | The post can be accessed at https://weibo.com/user_id/weibo_id where `user_id` and `weibo_id` should be replaced with values from the columns. |
| content     | text | The text of the post.                                        |
| reposts     | text | Number of reposts. If the number exceeds 10 thousands, it will be ended with the Chinese character "万". The character "万" is a unit, which means 10 thousands. (The same will happen in "comments" and "likes".) |
| comments    | text | Number of comments.                                          |
| likes       | text | Number of likes.                                             |

