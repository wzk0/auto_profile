import requests
import json
import os
import random

username=input('请输入你的用户名(不是昵称！！):')
print('程度0: 无\n程度1: 显示full_name,\n程度2: 显示description,\n程度3: 显示language,\n程度4: 显示stargazers_count,forks_count,\n程度5: 显示license\n可叠加')
degree=input('0~5,请输入你想要的信息展示程度(单个仓库):')
raw='https://api.github.com/users/'
url_ls=[username,username+'/repos']
degree=int(degree)
data=[]
for l in url_ls:
	r=requests.get(raw+l)
	data.append(json.loads(r.text))
me=data[0]
repo=data[1]
bio=me['bio']
t=[me['name'],me['company'],me['blog'],me['email'],me['location'],me['followers'],me['following'],me['twitter_username'],me['public_repos'],me['created_at'],me['public_gists'],me['type']]
ttt=[]
for tt in t:
	if tt==None:
		ttt.append('不告诉你！')
	elif tt=='User':
		ttt.append('普通用户！')
	else:
		ttt.append(str(tt))
t=ttt

if os.path.exists('profile.md'):
	with open('profile.md','w')as f:
		f.write('')

def wt(sth):
	with open('profile.md','a+')as f:
		f.write(sth+'\n')

wt('<h3 align="center">%s</h3>\n'%bio)

wt("<img align='center' src='https://i0.hdslb.com/bfs/article/02db465212d3c374a43c60fa2625cc1caeaab796.png'>")

wt('\n<h3 align="center">💯 关于我！👇</h3>\n\n---\n')

wt("<img align='left' src='https://github-readme-stats.vercel.app/api?username=%s&theme=tokyonight&show_icons=true'>"%username+'\n')

wt("<img align='right' src='https://github-readme-stats.vercel.app/api/top-langs/?username=%s&layout=compact&theme=tokyonight'>"%username+'\n')

wt('<br><br><br><br><br><br><br><br><hr>\n')

wt('* 👉 **头像 (本人照片🔮)**\n')

wt("<img align='right' src='%s'>"%me['avatar_url'])

wt('\n* 😘 **昵称 (实名认证👑) ——** *%s！*\n'%t[0])

wt('* 👁️‍🗨️ **身份 (已发布的🆔) ——** *%s* \n'%t[11])

wt('* 🏠 **公司 (另一个家💢) ——** *%s！*\n'%t[1])

wt('* 📋 **博客 (网络小窝🛸) ——** *[点我！](%s)*\n'%t[2])

wt('* 📮 **邮箱 (有事常联📧) ——** *%s*\n'%t[3])

wt('* 🏩 **在哪 (真实地址🏛️) ——** *%s！*\n'%t[4])

wt('* 🔥 **粉丝 (不可以吃🐻) ——** *%s个* \n'%t[5])

wt('* 🦄 **关注 (被粉丝的🚀) ——** *%s个*\n'%t[6])
 
wt('* 💕 **推特 (记得关注💘) ——** *[点我！](https://twitter.com/%s)*\n'%t[7])

wt('* 🎖 **仓库 (已公开的✨) ——** *%s个* \n'%t[8])

wt('* 💎 **片段 (已发布的🪄) ——** *%s个* \n'%t[10])

wt('* 🏆 **日期 (初来乍到✅) ——** *%s*\n'%t[9])

wt("<img align='center' src='https://i0.hdslb.com/bfs/article/02db465212d3c374a43c60fa2625cc1caeaab796.png'>")

wt('\n<h3 align="center">💯 关于我的仓库！👇</h3>\n\n---\n')

def rt_ht():
	st='🧡💛💚💙💜🤎🖤🤍'
	i=random.randint(0,len(st)-1)
	return st[i]

def bt_wt(dic,degree):
	url=dic['html_url']
	name1=dic['full_name']
	if dic['description']==None:
		description='*不告诉你！*'
	else:
		description=dic['description']
	name2=dic['full_name']+' - '+description
	language=dic['language']
	if language==None:
		language='*不告诉你！*'
	else:
		language=language
	count='✨ Star数: '+str(dic['stargazers_count'])+' —— '+'⚓ Fork数: '+str(dic['forks_count'])
	if dic['license']==None:
		license='*不告诉你！*'
	else:
		license=dic['license']['name']
	if degree==0:
		pass
	else:
		if degree==1:
			wt(rt_ht()+" [%s](%s)"%(name1,url)+'\n')
		if degree==2:
			wt(rt_ht()+" [%s](%s)"%(name2,url)+'\n')
		if degree==3:
			wt(rt_ht()+" [%s](%s)"%(name2,url)+'\n')
			wt('> 💬 语言: '+language+'\n')
		if degree==4:
			wt(rt_ht()+" [%s](%s)"%(name2,url)+'\n')
			wt('> 💬 语言: '+language+' —— '+count+'\n')
		if degree==5:
			wt(rt_ht()+" [%s](%s)"%(name2,url)+'\n')
			wt('> 💬 语言: %s —— %s —— 📚 许可证: %s\n'%(language,count,license))
		wt("---\n")
for r in repo:
	bt_wt(r,degree)
wt("<img align='center' src='https://i0.hdslb.com/bfs/article/02db465212d3c374a43c60fa2625cc1caeaab796.png'>")