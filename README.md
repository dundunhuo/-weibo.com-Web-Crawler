# "weibo.com" Web Crawler

 The toolbox to collect posts from https://weibo.com

![](https://shields.io/badge/OS-Windows_10_64--bit-lightgray)
![](https://shields.io/badge/dependencies-Google_Chrome>=96-blue)
![](https://shields.io/badge/dependencies-Python_3.11-blue)
![](https://shields.io/badge/tests-Google_Chrome_113_✔-brightgreen)

## Usage

1. Run the following script.
   ```bash
   pip install -r requirements.txt
   ```

2. Login https://weibo.com/ in Google Chrome, and don't close it. <br>
   *We assume Google Chrome is installed in default path. Otherwise, please modify Line 34 and 37 and assign these two variables to your customized cookies and encryption key respectively.*

3. Run `login_windows` function, referring to the usage in `Functions > login_windows` section.

4. Close the browser.

5. The following functions work for you now.

## Functions

### login_windows

Log in https://weibo.com and save logged-in status, with Windows platform.

**Parameters**:

`db`: str

The path of the database, where you'll store the cookies and fetched posts in future.

---

### search

This script searches for a word and a specific time period.  It records all the searching result in SQLite database.

**Parameters:**

`db`: str

The path of the database, where you have stored the cookies and would store fetched posts.

`table`: str (valid sqlite3 table name)

The table name in the database, where you store fetched posts.

`query`: str

Search query submitted to "weibo"

All posts containing this string will be recorded, 50 pages at most.

`start_time`: tuple[int], length=4, GMT+8

The tuple of length 4, where each element is integer. The 4 integers represent year, month, day, hour of the starting time. Posts from this hour will be collected. The time zone is the same has "weibo" server.

`end_time`: tuple[int], length=4, GMT+8

The tuple of length 4, where each element is integer. The 4 integers represent year, month, day, hour of the end time. Posts till this hour will be collected. The time zone is the same has "weibo" server.

---
