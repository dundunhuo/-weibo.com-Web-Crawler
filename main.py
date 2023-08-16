from argparse import ArgumentParser
from login_windows import WeiboClient
from search import search

parser = ArgumentParser()
parser.add_argument('--login', action='store_true',
                    help='(Action) Log in https://weibo.com and save cookies to database.')
parser.add_argument('--db', type=str, default='./posts.db',
                    help='The path of the database, where to store the cookies and fetched posts. If blank, data is '
                         'saved at posts.db of this program\'s root directory.')
parser.add_argument('--chrome_user_data', type=str,
                    help='The \'User Data\' file under the installation path of Google Chrome. If blank, assume'
                         'Google Chrome\'s installed at default directory.')
parser.add_argument('--search', action='store_true',
                    help='Search posts with a word and a specific time period.')
parser.add_argument('--query', type=str,
                    help='Search query submitted to https://weibo.com All posts containing this string will be '
                         'recorded, 50 pages at most.')
parser.add_argument('--start_time', type=str,
                    help='Format code: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format'
                         '-codes\n'
                         'Posts from this hour will be collected. The time zone is the same as https://weibo.com '
                         'server. Date format is \'%Y-%m-%d-%H\'.')
parser.add_argument('--end_time', type=str,
                    help='Posts till this hour will be collected. The format is the same as \'start_time\'.')
parser.add_argument('--max_page', type=int,
                    help='The maximum page to collect. If existed pages are less than this number, the result will be '
                         'fewer.')
parser.add_argument('--cookies', type=str,
                    help='Cookies to log in https://weibo.com site.')
command, _ = parser.parse_known_args()

# if command.login:
#     weibo_client = WeiboClient(chrome_user_data=command.chrome_user_data, db=command.db)
#     weibo_client.login()
# elif command.search:
search(db=command.db, query=command.query, start_time=command.start_time, end_time=command.end_time,
       max_page=command.max_page, cookies=command.cookies)
