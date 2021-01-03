import datetime
import threading
import time
import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
DELAY_TIME = 2
IMG_BASE_PATH = './res/images/sgs/'


def calculate_time():
    def wrapper(function):
        def execute(*args, **kwargs):
            beg = time.time()
            result = function(*args, **kwargs)
            end = time.time()
            seconds = end - beg
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            print(f'run function {function.__name__} took time:', '%d:%02d:%02d' % (h, m, s))
            return result

        return execute

    return wrapper


def flag_match_img(img_src, try_time=3, confidence=0.7):
    for i in range(try_time):
        pos = pyautogui.locateOnScreen(img_src, confidence=confidence)
        if pos:
            return pos
        elif i == try_time - 1:
            return None
        time.sleep(1)


@calculate_time()
def zhulu_tianxia():
    time.sleep(DELAY_TIME)
    print('\nsubprogram zhu_lu is start...')
    # 冒险 -> 进入逐鹿
    pyautogui.click(1263, 527)
    time.sleep(1)
    pyautogui.click(790, 539)
    pyautogui.click(1027, 175, interval=1, clicks=2)  # 可能弹出动画.
    pos1 = flag_match_img(IMG_BASE_PATH + 'kaishi_tiaozhan.png', try_time=6)
    pos2 = flag_match_img(IMG_BASE_PATH + 'fanhui.png', try_time=1)
    if pos1 and pos2:
        for i in range(5):
            # 英雄模式 -> 101-125关卡 -> 105关卡 -> 挑战 -> 确定阵容, 挑战 -> 等待进入挑战界面
            pyautogui.click(1027, 175)
            pyautogui.click(387, 430)
            pyautogui.click(681, 433)
            pyautogui.click(1619, 645)
            pyautogui.click(1419, 851)
            time.sleep(5)
            count_time = 50
            for j in range(count_time):
                pyautogui.click(959, 892)  # 继续对话框
                pos3 = flag_match_img(IMG_BASE_PATH + 'kaishi_tiaozhan.png', try_time=3)
                if pos3:
                    break
                else:
                    if j == count_time - 1:
                        print('out of the max_time, now can not address it by current program.')
                        exit()
                    pass
            print('zhulu challenge completed once.')
        pyautogui.click(pyautogui.center(pos2), clicks=2, interval=2)
    else:
        print('out of expected, may something error in here.')
    print('subprogram zhu_lu is over...')


def login_sgs():
    time.sleep(DELAY_TIME)
    print('\nsubprogram login_sgs is starting...')
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite("https://web.sanguosha.com/login/index.html")
    pyautogui.press('enter', presses=2)
    pos1 = flag_match_img(IMG_BASE_PATH + 'denglu_youxi.png', try_time=3)
    if pos1:
        pyautogui.click(pyautogui.center(pos1))
    pos2 = flag_match_img(IMG_BASE_PATH + 'jinru_youxi.png', try_time=6)
    if pos2:
        pyautogui.click(pyautogui.center(pos2))
    else:
        exit()
    time.sleep(2)
    pyautogui.click(1000, 570)
    print('loading game, please be patient')
    time.sleep(15)
    pyautogui.click(1733, 124, clicks=4, interval=3)  # click as much as possible, to make sure show quit activity.
    pos3 = flag_match_img(IMG_BASE_PATH + 'quxiao.png', confidence=0.7)
    if pos3:
        pyautogui.click(pyautogui.center(pos3))
    else:
        pyautogui.click(1415, 320)
        pyautogui.click(1600, 250)
        pyautogui.click(1733, 124, clicks=3, interval=2)
        pos3 = flag_match_img(IMG_BASE_PATH + 'quxiao.png', confidence=0.7, try_time=2)
        if pos3:
            pyautogui.click(pyautogui.center(pos3))
        else:
            print('out of the program excepted, this condition should be exist, make sure to be safe, quit it !!!')
            exit()
    print('subprogram login_sgs is over...')


def gonghui_leigu():
    time.sleep(DELAY_TIME)
    print('\nsubprogram gonghui_leigu is start...')
    # 进入公会->擂鼓*3->为了防止已经擂鼓过出现元宝擂鼓界面（增加取消）->返回主界面
    pyautogui.click(1220, 968)
    pos = flag_match_img(IMG_BASE_PATH + 'gonghui_leigu.png', try_time=7)
    if pos:
        pyautogui.click(pyautogui.center(pos), interval=2, clicks=3)
        pos2 = flag_match_img(IMG_BASE_PATH + 'quxiao.png', try_time=1)
        if pos2:
            pyautogui.click(pyautogui.center(pos2))
        for i in range(3):
            pos3 = flag_match_img(IMG_BASE_PATH + 'linqu_jiangli.png', confidence=0.7, try_time=2)
            if pos3:
                pyautogui.click(pyautogui.center(pos3))
        pos4 = flag_match_img(IMG_BASE_PATH + 'fanhui.png', confidence=0.7, try_time=2)
        if pos4:
            pyautogui.click(pyautogui.center(pos4))
        else:
            print('out of expected in here, some errors in here.')
    else:
        print('out of expected, may not in gonghui_leigu activity.')
    print('subprogram gonghui_leigu is over...')


def wujiang_jiangyin():
    time.sleep(DELAY_TIME)
    print('\nsubprogram wujiang_jiangyin is start...')
    # 点击武将->判断名将堂是否出现->点击将印打开抽取界面->开启一次->关闭抽取界面->返回主界面
    wujiang_icon = flag_match_img(IMG_BASE_PATH + 'wujiang_icon.png', confidence=0.75)
    if wujiang_icon:
        pyautogui.click(pyautogui.center(wujiang_icon))
    else:
        print('not found wujiang icon in current activity, end of subprogram')
        return False
    pos1 = flag_match_img(IMG_BASE_PATH + 'minjiang_tang.png', try_time=7)
    pos2 = flag_match_img(IMG_BASE_PATH + 'fanhui.png', try_time=2)
    if pos1 and pos2:
        pyautogui.click(pyautogui.center(pos1))
        max_time = 15
        while max_time:
            re_pos1 = flag_match_img(IMG_BASE_PATH + 'minjiang_tang.png', try_time=1)
            if re_pos1 is None:
                pyautogui.click(308, 499)
                pyautogui.click(1240, 849)
                pyautogui.click(1564, 248)
                break
            else:
                max_time = max_time - 1
                if max_time == 0:
                    print('out of max try time. some errors in here, end of subprogram')
                    return False
        pyautogui.click(pyautogui.center(pos2))
    else:
        print('out of expected, may some errors in here.')
    print('subprogram wujiang_jiangin is over...')


def sanguo_xiu():
    time.sleep(DELAY_TIME)
    print('\nsubprogram sanguo_xiu is starting... ')
    # 三国秀->三国秀坊(用返回按键来判断是否进入三国秀界面)->开启->开启三国秀后先返回抽取界面,再返回主界面故两次.
    sanguoxiu_icon = flag_match_img(IMG_BASE_PATH + 'sanguoxiu_icon.png', confidence=0.75)
    if sanguoxiu_icon:
        pyautogui.click(pyautogui.center(sanguoxiu_icon))
    else:
        print('not found sanguoxiu icon in current activity, end of subprogram')
        return False
    pos = flag_match_img(IMG_BASE_PATH + 'fanhui.png', try_time=6)
    if pos:
        pyautogui.click(1679, 810, interval=2)
        pyautogui.click(729, 627, interval=2)
        pyautogui.click(pyautogui.center(pos), clicks=2, interval=2)
    else:
        print('out of expected, the program may have some errors')
    print('subprogram sanguo_xiu is over... ')


def jianglin():
    time.sleep(DELAY_TIME)
    print('\nsubprogram jianglin is start...')
    max_time = 30
    while max_time:
        pyautogui.click(924, 867)
        pos = flag_match_img(IMG_BASE_PATH + 'fanhui.png', try_time=1)
        if pos:
            break
        elif max_time == 1:
            print('out of max try times, may some errors in here. end of subprogram.')
            return False
        max_time = max_time - 1
    pos = flag_match_img(IMG_BASE_PATH + 'fanhui.png', try_time=1)
    if pos:
        # 聚宝盆->领取奖励->关闭
        pyautogui.click(1449, 870)
        pyautogui.click(1170, 683)
        pyautogui.click(1323, 376)
        # 将灵出征部分,包括领取奖励和领取完毕后出征两部分.
        pyautogui.click(1559, 883), time.sleep(3)
        pyautogui.click(962, 813), time.sleep(3)
        pyautogui.click(1146, 787), time.sleep(1)
        pyautogui.click(710, 831, interval=3, clicks=2)
        pyautogui.click(856, 672)
        pyautogui.click(1564, 249)
        time.sleep(1)
        pyautogui.click(pyautogui.center(pos))
    else:
        print(f'out of expected, may not into jianglin activity, some errors in here.')
        pyautogui.click(924, 867, clicks=2, interval=2)  # 没有进入到将灵界面
    print('subprogram jianglin is over...')


def open_browser(key='2'):
    print('start to open browser')
    pyautogui.hotkey('winleft', 'd')
    time.sleep(1)
    if key == '1':
        pos1 = flag_match_img(IMG_BASE_PATH + 'edge.png')
        if pos1:
            pyautogui.click(pyautogui.center(pos1), clicks=2)
        else:
            exit()
    elif key == '2':
        pos2 = flag_match_img(IMG_BASE_PATH + 'chrome.png')
        if pos2:
            pyautogui.click(pyautogui.center(pos2), clicks=2)
        else:
            exit()


def start_game():
    open_browser()
    login_sgs()
    sanguo_xiu()
    wujiang_jiangyin()
    jianglin()
    zhulu_tianxia()
    gonghui_leigu()
    # pyautogui.click(1892, 15)  # 关闭浏览器


def timer():
    now_time = datetime.datetime.now()
    print(f'现在时间:{now_time}')
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 00:01:00",
                                           "%Y-%m-%d %H:%M:%S")
    timer_start_time = (next_time - now_time).total_seconds()
    print(f'距离运行还有{timer_start_time}秒.')
    m_timer = threading.Timer(timer_start_time, start_game)
    m_timer.start()


def with_start():
    def m_execute(m_argv):
        for x in m_argv:
            if x == '1':
                zhulu_tianxia()
            if x == '2':
                jianglin()

    print('第一参数:1.启动Edge. 2启动Chrome. 3.在游戏主界面. t.定时00:01:00运行')
    print('第二参数(可多选):1.逐鹿天下 2.将灵')
    string = input('输入参数: ')
    argv1 = string[:1]
    argv2 = string[1:]
    if argv1 == '1':
        open_browser(key='1')
        login_sgs()
        if not argv2:
            sanguo_xiu()
            wujiang_jiangyin()
            jianglin()
            zhulu_tianxia()
            gonghui_leigu()
        else:
            m_execute(argv2)
    elif argv1 == '2':
        open_browser(key='2')
        login_sgs()
        m_execute(argv2)
    elif argv1 == '3':
        m_execute(argv2)
    elif argv1 == 't':
        timer()
    else:
        start_game()


if __name__ == '__main__':
    with_start()
