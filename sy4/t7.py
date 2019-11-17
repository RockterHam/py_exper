import re
htmlString = '''<ul id="TopNav"><li><a href="/EditPosts.aspx" id="TabPosts">随笔</a></li>
        <li><a href="/EditArticles.aspx" id="TabArticles">文章</a></li>
        <li><a href="/EditDiary.aspx" id="TabDiary">日记</a></li>
        <li><a href="/Feedback.aspx" id="TabFeedback">评论</a></li>
        <li><a href="/EditLinks.aspx" id="TabLinks">链接</a></li>
        <li id="GalleryTab"><a href="/EditGalleries.aspx" id="TabGalleries">相册</a></li>
        <li id="FilesTab"><a href="Files.aspx" id="TabFiles">文件</a></li>
        <li><a href="/Configure.aspx" id="TabConfigure">设置</a></li>
        <li><a href="/Preferences.aspx" id="TabPreferences">选项</a></li></ul>'''
pre = re.compile('>(.*?)<')
s1 = ''.join(pre.findall(htmlString))
print(s1)
