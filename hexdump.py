

'''
Simple implementation of hexdump
https://gist.github.com/JonathonReinhart/509f9a8094177d050daa84efcd4486cb
'''
# def hexdump(self, data, length=16):
#     filter = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
#     lines = []
#     digits = 4 if isinstance(data, str) else 2
#     for c in range(0, len(data), length):
#         chars = data[c:c+length]
#         hex = ' '.join(["%0*x" % (digits, (x)) for x in chars])
#         printable = ''.join(["%s" % (((x) <= 127 and filter[(x)]) or '.') for x in chars])
#         lines.append("%04x  %-*s  %s\n" % (c, length*3, hex, printable))
#     print(''.join(lines))


import string

def hexdump(src, length=16, sep='.'):
	DISPLAY = string.digits + string.letters + string.punctuation
	FILTER = ''.join(((x if x in DISPLAY else '.') for x in map(chr, range(256))))
	lines = []
	for c in xrange(0, len(src), length):
		chars = src[c:c+length]
		hex = ' '.join(["%02x" % ord(x) for x in chars])
		if len(hex) > 24:
			hex = "%s %s" % (hex[:24], hex[24:])
		printable = ''.join(["%s" % FILTER[ord(x)] for x in chars])
		lines.append("%08x:  %-*s  |%s|\n" % (c, length*3, hex, printable))
	print ''.join(lines)
	
if __name__ == '__main__':
	data = ''.join(chr(x) for x in range(256))
	hexdump(data)
