import requests

def main():
	url = 'https://w1.v2dns.xyz/user/checkin'

	# headers = {
	#   'Connection': 'keep-alive',
	#   'Content-Length': '0',
	#   'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
	#   'Accept': 'application/json, text/javascript, */*; q=0.01',
	#   'X-Requested-With': 'XMLHttpRequest',
	#   'sec-ch-ua-mobile': '?0',
	#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
	#   'Origin': 'https://w1.v2free.xyz',
	#   'Sec-Fetch-Site': 'same-origin',
	#   'Sec-Fetch-Mode': 'cors',
	#   'Sec-Fetch-Dest': 'empty',
	#   'Referer': 'https://w1.v2free.xyz/user',
	#   'Accept-Language': 'zh-CN,zh;q=0.9',
	#   'Cookie': '_ga=GA1.1.1097224415.1644561485; _gcl_au=1.1.1299104476.1644561485; uid=31219; email=shenjie8278%40126.com; key=772b4f245432c928abc93ac4257dbcb1b486aa43ba89d; ip=873971ac1430cbeeed56b9b0a3781c88; expire_in=1676105429; _ga_NC10VPE6SR=GS1.1.1644803702.3.0.1644803704.0; crisp-client%2Fsession%2Fa47ae3dd-53d8-4b15-afae-fb4577f7bcd0=session_625114a8-61e3-4a99-a820-2d65e0b44b67; crisp-client%2Fsocket%2Fa47ae3dd-53d8-4b15-afae-fb4577f7bcd0=0'
	# }

	headers = {
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'keep-alive',
		'Content-Length': '0',
		'Cookie': '_ga=GA1.1.1097224415.1644561485; _gcl_au=1.1.1299104476.1644561485; uid=31219; email=shenjie8278%40126.com; key=772b4f245432c928abc93ac4257dbcb1b486aa43ba89d; ip=873971ac1430cbeeed56b9b0a3781c88; expire_in=1676105429; _ga_NC10VPE6SR=GS1.1.1644803702.3.0.1644803704.0; crisp-client%2Fsession%2Fa47ae3dd-53d8-4b15-afae-fb4577f7bcd0=session_625114a8-61e3-4a99-a820-2d65e0b44b67; crisp-client%2Fsocket%2Fa47ae3dd-53d8-4b15-afae-fb4577f7bcd0=0',
		'Host': 'w1.v2dns.xyz',
		'Origin': 'https://w1.v2dns.xyz',
		'Referer': 'https://w1.v2dns.xyz/user/',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"macOS"',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
	}

	response = requests.post(url=url, data={}, headers=headers).json()
	# print(response)

	msg = response['msg']
	if response['ret'] == 1:
		msg += '剩余流量:'+str(response['msg']['trafficInfo']['unUsedTraffic'])

	return msg

def ftqq(push_message):
    requests.post(
        url="https://sctapi.ftqq.com/SCT120106TH2m0FnDpblkDP2sFLVreNvXq.send",
        data={
            "title": "V2free自动签到脚本已执行！",
            "desp": push_message
        }
    )

if __name__ == "__main__":
	msg = main()
	# print(msg)
	ftqq(msg)
pass