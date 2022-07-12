from ProxyCloud import ProxyCloud
import ProxyCloud

from draft_to_calendar import send_calendar


#pr = 'socks5://KIGDJHYGJKLDFJYIKIIFCDYHJEKGEDRDKHKDFILELH'
#p = ProxyCloud.parse(pr)

##print(p)
host = 'a'
user = 'asd'
passw = 'asdsa'
nuevo = 'asdasd'
proxy = 'socks5://KIGDJHYGJKLDFJYIKIIFCDYHJEKGEDRDKHKDFILELH'
asyncio.run(send_calendar(host,user,passw,nuevo,proxy))