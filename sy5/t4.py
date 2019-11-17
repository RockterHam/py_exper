def text_creat(name, msg):
    desktop_path = "/Users/rockter/"
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()

text_creat('Test', '何奥 541713460411')
