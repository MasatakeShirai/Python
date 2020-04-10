#便利なテクニック
# メタ文字を全角文字に対応
import re
pattern = re.compile(r'^\w+$',re.U)
print(pattern.search('xｘyｙzｚ'))
pattern = re.compile(r'^\s+$',re.U)
print(pattern.search(' \u3000'))
