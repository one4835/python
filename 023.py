import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

string = "홀짝홀짝홀짝"
#print(string[0],string[2],string[4])
print(string[::2]) #홀홀홀
print(string[1::2]) #짝짝짝
