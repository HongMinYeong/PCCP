# Press ⌃R to execute it or replace it with your code.

def print_hi(name):
    print(f'Hi, {name}')

def func(x):
    y = x + 1
    return print(y)
#for clean code -> 변수를 지을 때는 걔에 맞는 역할을 보여해서 이름을 짓는게 좋음.
# func 이따위로 지으면 안됨
def add(x,y):  #input : x,y
    z = x + y
    return z #output : z

result = add(1,2)

print(result)
if __name__ == '__main__':
    print_hi('PyCharm')
