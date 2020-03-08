import json,os
import requests

def response(flow):
    #分析数据发现这是抖音旧的视频请求地址（估计是防爬取定时换的吧）
    #url='https://api.amemv.com/aweme/v1/aweme/post/'
    url='https://api3-normal-c-lq.amemv.com/aweme/v1/aweme/post/'
    #筛选出以上面url为开头的url
    if flow.request.url.startswith(url):
        text=flow.response.text
        #将已编码的json字符串解码为python对象
        data=json.loads(text)

        #在charles中刚刚看到每一个视频的所有信息
        #都在aweme_list中
        video_url=data['aweme_list']
        print(video_url)
        path='G:/Others/Douyin'
		#path='D:\crawler_data\douyin'
        if not os.path.exists(path):
            os.mkdir(path)
        for each in video_url:
            #视频描述
            desc=each['desc']
            url=each['video']['play_addr']['url_list'][0]
            # print(desc,url)
            filename=path+'/'+desc+'.mp4'
            # print(filename)
            req=requests.get(url=url,verify=False)
            with open(filename,'ab') as f:
                f.write(req.content)
                # 在文件关闭前，将缓存区的内容刷新到硬盘
                f.flush()
                print(filename,'下载完毕')